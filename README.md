# ML-FastApi
Đây là project nhỏ về việc triển khai mô hình deep learning nhằm đưa ra một mô hình sản phẩm thực tế cho người dùng thực tế có thể tương tác với mô hình. 
Bạn có thể tìm thấy model tôi train và file lưu trọng số của tôi tại đây: https://drive.google.com/drive/folders/1qz3f9lOVA0YQbWfD7xNYEspmnCBbCZxc?usp=drive_link
## Sau đó bạn hãy tạo thư mục weight trong thư mục model và thêm file weight như dưới đây
|_ root/  
|  	|_ config/  
|       |_ catdog.cfg.py  
|       |_ logging.cfg-pУ  
|   |_ logs/  
|   |_ middleware/  
|       |_ __init__.py  
|       |_ cors.py  
|       |_ http.py  
|   |_ models/  
|       |_ weights/  
|           |_ catdog_weights.pt  
|       |_ catdog_model.py  
|       |_ catdog_predictor.py  
|   |_ routes/  
|       |_ base.py  
|       |_ catdog_route.py  
|   |_ schemas/  
|       |_ catdog_schema.py  
|   |_ utils/  
|       |_ Llogger.py  
|   |_ app.py  
|   |_ requirements.txt  
|   |_ server.py  
### Install 
pip install -r requirements .txt
### Run with python
python server .py
### Result
