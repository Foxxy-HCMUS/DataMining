# DataMining-Lab2
Khai thác luật kết hợp trên tập phổ biến  

## Tiền xử lý dữ liệu
- File churn.txt có dư ra 1 dấu phẩy ở đâu đó
- Phải format lại thành file churn.csv hoặc file churn.arff (tất nhiên là sau khi xoá dấu phẩy bị dư đi) để Weka có thể đọc được 
- Xoá một vài thuộc tính ID, thuộc tính 'rác' và các thuộc tính bị phụ thuộc tuyến tính vào các thuộc tính khác. Tại mục này, file Churn.pdf có hướng dẫn khá chi tiết nhưng nói một các gắn gọn thì chúng ta sẽ phải xác định các thuộc tính ID, các thuộc tính có ít ý nghĩa, và tìm ra hàm tuyến tính giữa các thuộc tính để biết liệu chúng có phụ thuộc nhau hay không, sau đó xoá đống đó đi

## Phân tích sơ bộ tập dữ liệu
- Trong file Churn.pdf có hướng dẫn khá chi tiết về vấn đề này
- Nói một cách ngắn gọn thì bước này cho ta phân tích tổng quan cũng như một vài dữ đoán về dữ liệu để đánh giá các luật sau này
- Ví dụ: Trong tập dữ liệu có thuộc tính Customer Service Calls có ảnh hướng khá lớn đến việc phân lớp Churn = True. Nhìn vào biểu đồ cột trong phân tích, ta sẽ thấy từ cuộc gọi thứ 3 của khách hàng là tỷ lệ từ chối dịch vụ tăng ngày càng lớn. Từ đó có thể kết luận là thuộc tính này có ảnh hưởng đến phân lớp Churn và dự đoán rằng các luận rút ra sau này nên được bao gồm thuộc tính này

## Rút trích luật
- Trước khi rút trích luật, nhóm phải tiền xử lý với các nội dung nêu trên và tiến hành rời rạc hoá dữ liệu (ở đây nhóm chia ra 25 khoảng cho thuộc tính liên tục) để có thể áp dụng thuật toán Apriori
- Khi áp dụng thuật toán này, cần lưu ý về thông số đánh giá. Nhóm chọn `confidence` làm thông số đánh giá luật với mức `min_confidence` cao và `min_support` thấp. Các thông số được trình bày chi tiết trong báo cáo 
- Lý do phải chọn như vậy bởi vì tập dữ liệu bị lệch hẳn về phía Churn = False. Trong khi mục tiêu của việc rút trích luật là tìm hiểu sự tác động của các thuộc tính đến việc người dùng từ chối dịch vụ (Churn = True). Do đó, phải hạ mức support xuống để có thể rút trích được các luật cho kết quả True
