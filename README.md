# ML-FastApi
Đây là project nhỏ về việc triển khai mô hình deep learning nhằm đưa ra một mô hình sản phẩm thực tế cho người dùng thực tế có thể tương tác với mô hình. 
Bạn có thể tìm thấy model tôi train và file lưu trọng số của tôi tại đây: https://drive.google.com/drive/folders/1qz3f9lOVA0YQbWfD7xNYEspmnCBbCZxc?usp=drive_link
## Sau đó bạn hãy tạo thư mục weight trong thư mục model và thêm file weight như dưới đây
root/  
├── config/  
│ ├── catdog.cfg.py  
│ └── logging.cfg  
├── logs/  
├── middleware/  
│ ├── init.py  
│ ├── cors.py  
│ └── http.py  
├── models/  
│ ├── weights/  
│ │ └── catdog_weights.pt  
│ ├── catdog_model.py  
│ └── catdog_predictor.py  
├── routes/  
│ ├── base.py  
│ └── catdog_route.py  
├── schemas/   
│ └── catdog_schema.py  
├── utils/  
│ └── logger.py  
├── app.py  
├── requirements.txt  
└── server.py  
### Install 
pip install -r requirements .txt
### Run with python
python server .py
### Result
