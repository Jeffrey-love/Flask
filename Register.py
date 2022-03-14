from flask import *
import pymysql

# 创建flask程序
web = Flask(
    __name__,
    static_url_path='/static',  # 静态文件路径
    static_folder='static',
    template_folder='../templates'  # 模板文件,这里一定要填到目录下才可以
)


@web.route('/a')
def send():
    return render_template('send.html')


@web.route('/chuli', methods=['POST'])
def chuli():
    username = None
    password = None
    if request.method == "POST":
        username = request.form.get('uname')
        password = request.form.get('passwd')
        print("用户名："+username+"----密码："+password)
    # 打开数据库
    db = pymysql.connect(host='localhost', user='root', password='root', db='haha')
    # 创建游标对象
    cursor = db.cursor()
    # sql语句
    sql = """
    INSERT INTO table1 (username,password) VALUES ('%s','%s')
    """ % (username, password)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 确认
        db.commit()
    except Exception as e:
        # 执行失败就回滚
        print(e)
        db.rollback()

    db.close()

    return render_template('chuli.html')


# 首页
@web.route('/')
def index():
    return "前往‘a’路由进行注册！"


@web.errorhandler(404)
def page_not_found(e):
    return "ERROR!!!NOT!!!FOUND!!!"


if __name__ == '__main__':
    web.run(host='0.0.0.0', port=8888, debug=True)
