from flask import Flask, render_template

app = Flask(__name__)

#我们把包含变量和运算逻辑的 HTML 或其他格式的文本叫做模板（template）
#执行这些变量替换和逻辑计算工作的过程被称为渲染（rendering）
#这个工作由模板渲染引擎——Jinja2来完成
#Jinja2要解决的问题：网页复杂后直接把大量 HTML 写进 Python 字符串会很难维护

#Jinja2的语法（代码写在templates/index.html里）
#{{ ... }} 用来标记变量。
#{% ... %} 用来标记语句，比如 if 语句，for 语句等。
#{# ... #} 用来写注释。
#为了方便对变量进行处理，Jinja2 提供了一些过滤器，语法形式如下：
#{{ 变量|过滤器 }}

#定义虚拟数据
name = 'Wangge'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

#http://127.0.0.1:5000/
#在传入render_template()函数的关键字参数中，左边的 movies 是模板中使用的变量名称，右边的 movies 则是该变量指向的实际对象。
#这里传入模板的 name 是字符串，movies 是列表
#render_template()函数在调用时会识别并执行 index.html 里所有的 Jinja2 语句
#在返回的页面中，变量会被替换为实际的值（包括定界符），语句（及定界符）则会在执行后被移除（注释也会一并移除）。
@app.route("/")
def index():
    return render_template('index.html', name=name, movies=movies)




