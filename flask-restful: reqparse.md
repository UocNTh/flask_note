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

    from flask_restful import reqparse

    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('foo', type=int, required=True)
    parser.add_argument('bar', type=int, required=True)

    # If a request comes in not containing both 'foo' and 'bar', the error that
    # will come back will look something like this.

    {
        "message":  {
            "foo": "foo error message",
            "bar": "bar error message"
        }
    }

    # The default behavior would only return the first error

    parser = RequestParser()
    parser.add_argument('foo', type=int, required=True)
    parser.add_argument('bar', type=int, required=True)

    {
        "message":  {
            "foo": "foo error message"
        }
    }
--> nếu không có bundle_errors thì sẽ mặc định trả về lỗi đầu tiên 

--> cấu hình khóa ứng dụng "BUNDLE_ERRORS" 

BUNDLE_ERROR = True 

- Thông báo lỗi 

--> Thông báo lỗi cho từng trường cụ thể có thể được tùy chỉnh bằng cách sử dụng tham số help 

from flask_restful import reqparse

    parser = reqparse.RequestParser()
    parser.add_argument(
        'foo',
        choices=('one', 'two'),
        help='Bad choice: {error_msg}'
    )

    # If a request comes in with a value of "three" for `foo`:

    {
        "message":  {
            "foo": "Bad choice: three is not a valid choice",
        }
    }



