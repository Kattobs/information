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
    # 开启数据库跟踪模式
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 配置redis数据库信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # 使用session，记得添加加密字符串对session_id进行加密处理
    SECRET_KEY = "DKAJLFHKLJH"
    # 指定要存储的数据库类型
    SESSION_TYPE = "redis"
    # 具体将session中的数据存储到哪个redis数据库
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=1)
    # session存储的数据后产生的session_id 需要加密
    SESSION_USE_SIGNER = True
    # 设置非永久存储
    SESSION_PERMANENT = False
    # 设置过期时常，默认过期时常为31天
    PERMANENT_SESSION_LIFETIME = 86400

# 创建app对象
app = Flask(__name__)
app.config.from_object(Config)
# 创建数据库对象
db = SQLAlchemy(app)
# 创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启后端的CSRF保护机制
CSRFProtect(app)
# 借助Session调整flask，session的存储位置到redis中存储
Session(app)
# 创建数据库管理对象，将app交给管理对象管理
manager = Manager(app)
# 数据库迁移初始化
Migrate(app, db)
# 添加迁移命令
manager.add_command("db", MigrateCommand)

# 创建视图函数，并且将url路由和视图函数绑定到一起
@app.route('/')
def index():
    return "hello world!"


# 运行flask项目
if __name__ == '__main__':
    # 使用manager对象启动flask项目，代替app.run()
    manager.run()
