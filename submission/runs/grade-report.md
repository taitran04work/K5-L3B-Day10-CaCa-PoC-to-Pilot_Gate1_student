# Tự kiểm tra sự cố S5 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S5-grade-20261119-163830-88979b` · bàn: `K5-L3B-DAY10-CaCa-PoCtoPilotGate1` · grader `lab10-1.0` · 0.488s
- Ba mốc: base `R-S5-before-20261119-163831-88979b` · prepared `R-S5-prepared-20261119-163831-88979b` · after `R-S5-after-20261119-163831-88979b` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `f8eab615`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `88979b3fb538`
- Hash Bản tiêu chí chấp nhận: `669579799373` · đã ký: `669579799373` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S5` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: (trống) · chưa ghi (ghi đúng số đã bốc vào dòng `Thẻ đã bốc:` ở đầu `templates/form-c-incident.md`)

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ❌ | file khoá bị đổi: ['data/tickets.jsonl', 'data/world.json', 'incidents/S5/card.json', 'incidents/S5/card.md', 'incidents/S5/tickets.jsonl', 'incidents/S5/world_patch.json', 'lab10/__init__.py', 'lab10/_gradectx.py', 'lab10/_noop_guards.py', 'lab10/agent.py', 'lab10/check_submission.py', 'lab10/checkpoint.py', 'lab10/criteria.py', 'lab10/eval.py', 'lab10/gate.py', 'lab10/grade.py', 'lab10/helpers.py', 'lab10/mock_llm.py', 'lab10/ops.py', 'lab10/tools.py', 'lab10/trace.py', 'lab10/world.py', 'tests/test_public.py'] |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['source_of_truth_conflicts', 'duplicate_refund_attempts']; sáng đèn: [('source_of_truth_conflicts', 'before', 5.0, 0.0), ('source_of_truth_conflicts', 'after', 1.0, 0.0), ('duplicate_refund_attempts', 'after', 0.0, 10.0)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.4 | 0.3 | 0.375 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 2 · 12 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 6083 · 10000 | 9594 · 10000 | 8027 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 2412 · 1500 | 768 · 1500 | 764 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -60486 | -65939 | 15786 |
| ROI | -0.33 | -0.69 | 0.25 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 196000 · 2000000 | 75000 · 2000000 | 43000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 178000 · 2000000 | 70000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.3333 | 0.2667 |
| số kho đắt hơn làm tay | 1 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 20 | 15 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.6667; hoàn sai 50000; oan 0; PII 0; chi phí 664đ | — | — |
| kho DN | pass 0.8; hoàn sai 490000; oan 5; PII 0; chi phí 663đ | — | — |
| kho HCM | pass 0.5; hoàn sai 100000; oan 5; PII 0; chi phí 662đ | pass 0.5; hoàn sai 100000; oan 5; PII 0; chi phí 762đ | — |
| kho HCM-B2B | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 11326đ > làm tay | — | — |
| kho HN | pass 0.75; hoàn sai 250000; oan 10; PII 0; chi phí 1244đ | pass 0.75; hoàn sai 250000; oan 10; PII 0; chi phí 4302đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4277đ |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng GHSH | pass 0.8; hoàn sai 250000; oan 10; PII 0 | pass 0.6667; hoàn sai 250000; oan 10; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng MKD | pass 0.8333; hoàn sai 50000; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.75; hoàn sai 590000; oan 10; PII 0 | pass 0.6667; hoàn sai 100000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.3077 | 0.25 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 2 · 12 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 7948 · 10000 | 6864 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 26673 | 25087 |
| ROI | 1.34 | 0.26 | 0.46 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5909 | 0.3636 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3683đ | — |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | — |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2462 | 0.25 | +0.0227 |
| visible | pass_rate | 0.8333 | 0.7 | 1.0 | +0.1667 |
| visible | pass_k | 0.8333 | 0.7 | 1.0 | +0.1667 |
| visible | wrongful_refund_vnd | 890000 | 350000 | 0 | -890000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 20 | 15 | 0 | -20 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.4 | 0.3 | 0.375 | -0.025 |
