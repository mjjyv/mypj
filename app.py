from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def init_admin():
    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    from models.user import User

    admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
    class UserView(ModelView):
        column_list = ('username', 'email')
        form_columns = ('username', 'email')
    admin.add_view(UserView(User, db.session))

with app.app_context():
    db.create_all()
    init_admin()

if __name__ == '__main__':
    app.run(debug=True)