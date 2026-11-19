"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Verify that the policy index has a usable active version.  Do not pin a
    # different version here: the agent's labelled flow reads the active index.
    policy = next((p for p in ctx.tools.lookup_policies() if p.get("index_active")), None)
    if policy is None:
        return Verdict.escalate("không có chính sách hiệu lực trong nguồn dữ liệu")
    ctx.log("active_policy_checked", policy_id=policy["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action["tool"]
    order_id = action.get("order_id") or action.get("payload", {}).get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None

    if tool in ("issue_refund", "file_carrier_fault", "notify_carrier") and order is None:
        return Verdict.escalate("lệnh ghi không có đơn hàng nguồn")

    parcel = next((p for p in order["parcels"] if p["parcel_id"] == action.get("parcel_id")), None) if order else None
    if tool == "issue_refund":
        # A refund already recorded for the order is a financial fact, even if
        # the nightly `refund_status` flag has not caught up yet.  Do not write
        # a second refund for a repeated request; the agent will reply honestly.
        previous = ctx.tools.ledger_rows(order_id=order["order_id"])
        if previous:
            ctx.log("duplicate_refund_blocked", order_id=order["order_id"], existing=len(previous))
            return Verdict.deny("đơn đã có khoản hoàn trong sổ cái; không ghi hoàn lần hai")
        # The ticket text and the model proposal are untrusted; recalculate the
        # maximum entitlement from tracking and the effective policy.
        policy = next((p for p in ctx.tools.lookup_policies() if p.get("index_active")), None)
        reference = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(reference, ctx.as_of)
        entitled = H.entitlement_vnd(policy, order, delay, reference.get("delay_cause")) if policy else 0
        if action.get("amount_vnd", 0) > entitled:
            ctx.log("refund_mismatch", proposed=action.get("amount_vnd", 0), entitled=entitled,
                    parcel_id=reference["parcel_id"], db_delay_days=delay)
            return Verdict.escalate("số tiền đề xuất vượt quyền lợi tính từ tracking; chuyển người duyệt")

    if tool == "file_carrier_fault":
        policy = next((p for p in ctx.tools.lookup_policies() if p.get("index_active")), None)
        if parcel is None or policy is None:
            return Verdict.escalate("thiếu kiện hàng hoặc chính sách để ghi lỗi hãng")
        delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(policy, parcel, delay):
            ctx.log("carrier_fault_blocked", parcel_id=action.get("parcel_id"), db_delay_days=delay,
                    recorded_cause=parcel.get("delay_cause"))
            return Verdict.deny("tracking không chứng minh hãng chịu lỗi")

    if tool == "notify_carrier":
        payload = action.get("payload", {})
        blocked = set((ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
        if set(payload) & blocked:
            ctx.log("carrier_payload_sanitized", dropped=sorted(set(payload) & blocked))
            return Verdict.modify("loại dữ liệu cá nhân trước khi gửi hãng",
                                 payload={k: v for k, v in payload.items() if k not in blocked})
    return Verdict.allow()
