from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models.user import User

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo SQLAlchemy và Flask-Admin
db = SQLAlchemy(app)
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

# Tùy chỉnh giao diện quản lý cho model User
class UserView(ModelView):
    column_list = ('id', 'username', 'email')  # Hiển thị các cột
    form_columns = ('username', 'email')       # Cột có thể chỉnh sửa
    can_delete = True                          # Cho phép xóa
    can_create = True                          # Cho phép tạo mới

# Thêm model vào Flask-Admin
admin.add_view(UserView(User, db.session))

# Tạo cơ sở dữ liệu nếu chưa tồn tại
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    