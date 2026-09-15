from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route("/")
def hello():
    return "Hello, Flask!"

#http://127.0.0.1:5000/greet/your_name
#escape() 函数用于转义用户输入的内容，防止 XSS 攻击。
#url_for: Flask 提供了一个 url_for 函数来生成 URL，它接受的第一个参数就是端点值，默认为视图函数的名称
@app.route("/greet/<name>")
def url_for(name):
    return f"Hello, {escape(name)}!" 


