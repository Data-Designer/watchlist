from flask import Flask
from flask import escape,url_for,render_template

app = Flask(__name__)

name = 'Grey Li'
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





@app.route('/user/<name>')
def user_page(name):
    return 'User: %s page' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('user_page',name='zc')) # 传入user_page所需的参数，这里是批量创造页面好像
    print(url_for('user_page',name='xyh'))
    print(url_for('user_page',name=2)) # 这里换成num已经不行了
    return  'Test page'

@app.route('/')
def index():
    return render_template('./index.html',name=name,movies=movies) # 模板渲染

