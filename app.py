from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Khởi tạo SQLAlchemy
db = SQLAlchemy(app)

# Khởi tạo Flask-Admin
admin = Admin(app, name="Admin Panel", template_mode="bootstrap3")


# Hàm khởi tạo để tránh circular import
def init_admin():
    from flask_admin.contrib.sqla import ModelView
    from models.user import User

    class UserView(ModelView):
        column_list = ("id", "username", "email")
        form_columns = ("username", "email")
        can_delete = True
        can_create = True

    admin.add_view(UserView(User, db.session))


# Tạo cơ sở dữ liệu và khởi tạo admin
with app.app_context():
    db.create_all()
    init_admin()

if __name__ == "__main__":
    app.run(debug=True)
