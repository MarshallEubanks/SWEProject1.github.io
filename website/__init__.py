from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lmaolmaolmaolmao'

    from .views import views
    from .auth import register


    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(register, url_prefix ='/')

    return app