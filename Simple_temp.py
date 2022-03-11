import flask
from flask import Flask
from flask import Response


# 创建flask程序
web = Flask(__name__)


# 默认的首页
@web.route('/')
def index():
    return "HELLO INDEX!"


# 这是路由 /a 使用Response使得能方便的呈现出简单的html界面
@web.route('/a')
def index_a():
    return Response('<h1>haha nihao</h1>'
                    '<br><hr>'
                    '<h2>hahaha,I\'m a</h2>', 200)


# 来个页面跳转
@web.route('/redirect')
def rd_page():
    # 主动抛出异常,注释掉下面一行则会正常显示,在应急响应情况下不失为很好的方法
    flask.abort(404)
    # 站外跳转
    return flask.redirect('http://www.baidu.com')
    # 站内跳转，跳转到路由a中
    # return flask.redirect(flask.url_for('a'))


# 404重定向
@web.errorhandler(404)
def error(e):
    return "没有找到页面~请检查路由~~~"


if __name__ == '__main__':
    # 指定ip地址和端口，如果不填会默认127.0.0.1以及随机端口
    web.run(host='0.0.0.0', port=8888, debug=True)
