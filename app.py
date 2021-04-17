from flask import Flask
from flask import escape,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return hello

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s page' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='zc')) # 传入user_page所需的参数
    print(url_for('user_page',name='xyh'))
    print(url_for('user_page',name=2)) # 这里换成num已经不行了
    return  'Test page'

