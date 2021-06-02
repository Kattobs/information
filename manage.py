# 导入Flask类
from flask import Flask


# 创建app对象
app = Flask(__name__)


# 创建视图函数，并且将url路由和视图函数绑定到一起
@app.route('/')
def index():
    return "hello world!"


# 运行flask项目
if __name__ == '__main__':
    app.run(debug=True)
