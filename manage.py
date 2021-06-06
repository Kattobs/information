# 导入Flask类
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session


# 创建配置类
class Config(object):
    DEBUG = True
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/manager22"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SECRET_KEY = "DKAJLFHKLJH"
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=1)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400

# 创建app对象
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
CSRFProtect(app)

Session(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

# 创建视图函数，并且将url路由和视图函数绑定到一起
@app.route('/')
def index():
    return "hello world!"


# 运行flask项目
if __name__ == '__main__':
    manager.run()
