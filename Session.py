import flask
from flask import *
from datetime import timedelta


# 创建flask程序
web = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    template_folder='../templates'
)

# 配置加密字符串
web.config['SECRET_KEY'] = "key123"
# 设置7天有效期
web.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@web.route('/login')
def login():
    # 设置cookie
    session['user_id'] = '20'
    session['vip'] = '0'
    return 'success'


@web.route('/a')
def a():
    # 读取cookie
    user_id = session['user_id']
    vip = session['vip']
    return flask.render_template("tempa.html", user_id=user_id, vip=vip)


@web.route('/logout')
def logout():
    # session.pop('user_id',None)
    # session.pop('vip',None)
    # session['user_id']=False
    session.clear()
    return 'logout_success'


if __name__ == '__main__':
    web.run(host='0.0.0.0', port=8888, debug=True)
