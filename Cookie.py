import flask
from flask import *

web = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    template_folder='../templates'
)


@web.route('/a')
def a():
    response = flask.make_response('success!')
    response.set_cookie('user_id', '10', max_age=150)
    response.set_cookie('vip', '0', max_age=150)
    return response


@web.route('/b')
def b():
    user_id = request.cookies.get('user_id')
    vip = request.cookies.get('vip')
    return flask.render_template('tempa.html', vip=vip, user_id=user_id)


@web.route('/logout')
def logout():
    response = flask.make_response('退出')
    response.delete_cookie('user_id')
    response.delete_cookie('vip')
    return response


if __name__ == '__main__':
    web.run(host="0.0.0.0", port=8888, debug=True)
