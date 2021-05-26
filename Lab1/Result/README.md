# Kết quả chạy chương trình của mục 3  

## 0. Giải thích 1 chút về cú pháp chung  

- `method`: tên phương thức cần truyền vào  
- `filein`: tên file input cần truyền vào  
- `fileout`: tên file output chứa kết quả sau khi thực hiện lệnh  
- `rate`: tỷ lệ  

## 1. Liệt kê các cột bị thiếu dữ liệu  

- Cú pháp: `python main.py -type listmissingdata -filein <fileName>`  

## 2. Đếm số dòng bị thiếu dữ liệu  

- Cú pháp: `python main.py -type countmissingdata -filein <fileName>`  

## 3. Điền giá trị thiếu  

- Cú pháp:  
    - `python main.py -type fillmissingdata -method mean -filein <fileName> -fileout <fileName>`  
    - `python main.py -type fillmissingdata -method median -filein <fileName> -fileout <fileName>`  
    - `mean`: điền giá trị thiếu bằng phương pháp mean (áp dụng cho thuộc tính số)  
    - `median`: điền giá trị thiếu bằng phương pháp median (áp dụng cho thuộc tính số)  
    - Cả 2 lệnh trên đều điền dữ liệu thiếu cho thuộc tính định danh bằng cách lấy mode  

## 4. Xoá các dòng bị thiếu dữ liệu  

- Cú pháp: `python main.py -type eraserow -rate <rate> -filein <fileName> -fileout <fileName>`  

## 5. Xoá các cột bị thiếu dữ liệu  

- Cú pháp: `python main.py -type erasecolumn -rate <rate> -filein <fileName> -fileout <fileName>`  

## 6. Xoá các mẫu bị trùng lặp  

- Cú pháp: `python main.py -type eraseduplicaterow -filein <fileName> -fileout <fileName>`  

## 7. Chuẩn hoá một thuộc tính  

- Cú pháp:  
    - `python main.py -type standardize -method minmax -attribute <attribute> -filein<fileName> -fileout <fileName>`  
    - `python main.py -type standardize -method zscore -attribute <attribute> -filein <fileName> -fileout <fileName>`  

## 8. Tính giá trị biểu thức  

- Cú pháp: `python main.py -type expression`  
- Sau đó người dùng nhập biểu thức cần tính  

## 9. File kết quả  

- Điền dữ liệu thiếu:  
    - Sử dụng phương pháp mean: `mean.csv`  
    - Sử dụng phương pháp median: `median.csv`  
- Xoá dòng thiếu dữ liệu:  
    - Ngưỡng `0.1`: `eraseRow_1.csv`  
    - Ngưỡng `0.9`: `eraseRow_2.csv`  
- Xoá cột thiếu dữ liệu:  
    - Ngưỡng `0.1`: `eraseColumn_1.csv`  
    - Ngưỡng `0.9`: `eraseColumn_2.csv`  
- Xoá dữ liệu trùng lặp: `eraseDuplicateRow.csv`  
- Chuuẩn hoá dữ liệu  
    - Sử dụng phương pháp min-max cho cột `SalePrice`: `SalePrice.csv`  
    - Sử dụng phương pháp z-score cho cột `OpenPorchSF`: `OpenPorchSF.csv`  
- Tính giá trị biểu thức  
    - Biểu thức: YrSold-MoSold -> `e1.csv`  
    - Biểu thức: MSSubClass*LotArea -> `e2.csv`  