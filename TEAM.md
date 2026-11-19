# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `CaCa`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-CaCa-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S5`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trần Hữu Tài | 2A202603944 | Kỹ sư cổng | ✓ |
|   2 | Nguyễn Thành Công | 2A202618577 | Sản phẩm và kinh doanh | |
|   3 | Đồng Văn Quyến | 2A202678465 | Vận hành và pháp lý | |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranHuuTai-2A202603944

### Phần việc phụ trách

Kỹ sư cổng: các mục B1, B2, B7.1–B7.3 và C2, C5–C9; `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

Viết cổng kiểm quyền lợi theo tracking, cổng chống hoàn lặp theo sổ cái và hai monitor; chạy trace T-002@55, S5-01/S5-02 và kiểm public tests.

### Bằng chứng

`1b6ee1d`, `e969c63`; `R-base-prepared-20261119-161937-4347e1`, `R-S5-after-20261119-163830-88979b`; Phiếu B B1–B2, B7 và Phiếu C C2/C7/C8.

### Exit ticket

Cổng an toàn cần dựa vào nguồn sự thật ngoài model; còn cần kiểm tra độ trễ đồng bộ ledger khi pilot thật.

## NguyenThanhCong-2A202618577

### Phần việc phụ trách

Sản phẩm và kinh doanh: Phiếu A, B3, B6–B8 và quyết định Gate 1; `config/acceptance_criteria.json` và mục `business` của `config/operating_gates.json`.

### Đóng góp cụ thể

Đặt ngưỡng tiêu chí trước khi đo, đọc chi phí/ROI theo kho, quyết định giảm phạm vi pilot từ HN/HCM còn HN sau S5.

### Bằng chứng

`1b6ee1d`; `R-base-before-20261119-161811-692781`, `R-S5-after-20261119-163830-88979b`; Phiếu A, B3/B6/B8 và C3/C12.

### Exit ticket

Không chỉ nhìn pass rate: quyết định pilot phải chịu được chi phí người trực và ROI theo từng phân khúc.

## DongVanQuyen-2A202678465

### Phần việc phụ trách

Vận hành và pháp lý: Phiếu A1.2/A2 production, B4–B5, B7.5–B7.6, C10–C12; mục `operations` và `legal` của `config/operating_gates.json`.

### Đóng góp cụ thể

Thiết kế hàng chờ người duyệt, điều kiện dừng, danh sách PII cấm gửi hãng và runbook ứng phó hoàn lặp.

### Bằng chứng

`e969c63`; `R-S5-grade-20261119-163830-88979b`; Phiếu A1.2/A2, B4/B5/B7.5–B7.6 và C4/C10/C11.

### Exit ticket

Một cổng kỹ thuật vẫn cần PIC và thao tác dừng rõ ràng, nếu không tín hiệu đỏ không tạo ra hành động.
