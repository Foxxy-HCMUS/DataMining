# DataMining-Lab3

Another collaboration in DataMining - fit@hcmus

## Tiền xử lý tập dữ liệu hawk.csv

- Xóa những cột có dữ liệu thiếu trên 50%
- Xóa cột có giá trị tương tự như ID (mỗi dòng ứng với 1 giá trị của cột này)
- Điền đầy những cột có dữ liệu thiếu còn lại
	- Điền đầy các cột có kiểu dữ liệu nominal bằng mode
	- Điền đầy các cột có kiểu dữ liệu numeric bằng mean
- Sau khi tiền xử lý thì xuất ra file `AfterPreprocess.csv`. Mở file này bằng Weka sau đó chọn thuộc tính lớp là `Species` rồi lưu lại dưới định dạng `*.arff` (nếu thích)

## Phân lớp sử dụng Weka

- Mở file `AfterPreprocess.csv` (nhớ chọn lại thuộc tính lớp) hoặc file `AfterPreprocess.arff` nếu đã 'Save as...'
- Đối với thuật toán ID3 và NaiveBayesSimple và phiên bản Weka từ 3.8.4 trở lên, cần cài thêm gói [simpleEducationalLearningSchemes](https://stackoverflow.com/questions/48888463/weka-3-8-package-installation-what-are-the-steps-to-add-id3)
- Các hàm phân lớp (cùng phương thức đánh giá) có thể tìm thấy tại tab `Classify`, phần `Classifier` và phần `Test options`
- Phần `Experimenter` tự mò 
- Phần trả lời câu hỏi về các thuật toán phân lớp và các phương pháp đánh giá có thể xem chi tiết tại file [báo cáo](https://github.com/baolongnguyenmac/DataMining-Lab3/blob/main/Report/Report.pdf)

## Cluster

- Cài đặt 2 thuật toán K-Means và K-Medoids tại file `Lab03-Clustering.ipynb`
- Việc vài đặt thuật toán K-Means chắc là không có gì phải bàn (ngoại trừ việc code demo của thầy trong file jupyter notebook hơi gà)
- Việc cài đặt thuật toán K-Medoids: Ý tưởng thuật toán được tham khảo tại trang 457, sách [Data Mining - Concepts and Techniques của J.Han](https://github.com/XiaoqiMa/Books/blob/master/Data-Mining.-Concepts-and-Techniques.pdf) và [bài viết này](https://towardsdatascience.com/k-medoids-clustering-on-iris-data-set-1931bf781e05)
- Điểm khác nhau cơ bản giữa 2 thuật toán này là
	- Đối với K-Means: Tâm của mỗi cụm là giá trị trung bình của các điểm trong cụm đó
	- Đối với K-Medoids: Tân của mỗi cụm là 1 điểm xác định trong cụm đó
	- Các điểm khác nhau khác hoàn toàn có thể đọc file notebook trong repo này hoặc search các bài báo học thuật để có thông tin chi tiết hơn
- Ứng dụng 2 thuật toán trên để phân lớp đối với tập dữ liệu Hoa dương vĩ: Cần chú ý việc thuật toán sẽ tự động gắn nhãn cho các cụm mà nó gom được, các nhãn này có thứ tự không giống như các nhãn trong tập dữ liệu cung cấp. Do đó cần đổi tên lại nhãn để có thể đánh giá được model
