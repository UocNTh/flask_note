# Phân tích yêu cầu

- Đối số cơ bản

parser = reqparse.RequestParser() 
parser.add_argument('rate', type=int, help='Rate cannot be converted')

--> help : hiển thị dưới dạng thông báo lỗi khi loại lỗi xuất hiện trong khi phân tích cú pháp 

- Đối số bắt buộc 

parser.add_argument('name', required=True,help="Name cannot be blank!")

--> thêm  required=True vào lệnh add_argument 

- Nhiều giá trị và danh sách 

parser.add_argument('name', action='append')

--> chấp nhận nhiều giá trị cho một khóa, chuyểnf vào action='append' 

- Xử lý lỗi 

--> các lỗi được nhóm lại với nahu và được gửi lại cùng một lúc 
--> chuyển vào đối số bundle_errors 

parser = reqparse.RequestParser(bundle_errors=True)

{
    "message":  {
        "foo": "foo error message",
        "bar": "bar error message"
    }
}

--> nếu không có bundle_errors thì sẽ mặc định trả về lỗi đầu tiên 

--> cấu hình khóa ứng dụng "BUNDLE_ERRORS" 

BUNDLE_ERROR = True 

- Th



