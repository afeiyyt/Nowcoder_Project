# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

# 定义一个应用
app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.secret_key = 'newcoder'  # flask message传递需要secret key


@app.route('/index/')
@app.route('/')
def index():
    res = ''
    for category, msg in get_flashed_messages(with_categories=True):
        res = res + category + msg + '<br>'
    res += 'hello'
    return get_flashed_messages()


@app.route('/profile/<int:uid>/', methods=['GET', 'POST'])  # 定义支持的方法
def profile(uid):
    colors = ('red', 'green')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)


@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'  # /request?key=value 不传key的话默认为defaultkey
    res = res + request.url + '++' + request.path + '<br>'
    for property in dir(request):
        res = res + str(property) + '||<br>' + str(eval('request.' + property)) + '<br>===========<br>'
    response = make_response(res)
    response.set_cookie('nowcoderid', key)
    response.status = '404'
    response.headers['nowcoder'] = 'hello~~'
    return response


@app.route('/newpath')
def newpath():
    return 'newpath'


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', url=request.url), 404


@app.errorhandler(400)
def exception_page(error):
    response = make_response('出错啦~')
    return response


@app.route('/admin')
def admin():
    key = request.args.get('key')
    if key == 'admin':
        return 'hello admin'
    else:
        # raise Exception()
        return 'Exception'


@app.route('/login')
def login():
    app.logger.info('login success')  # log的使用
    flash('登录成功', 'info')
    return 'ok'
    # return redirect('/')  # 跳转到首页显示flask信息


def set_logger():
    info_file_handler = RotatingFileHandler('D:\\GitHub\\Nowcoder_Project\\Primary\\C2\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('D:\\GitHub\\Nowcoder_Project\\Primary\\C2\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('D:\\GitHub\\Nowcoder_Project\\Primary\\C2\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


@app.route('/log/<level>/<msg>/')
def log(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)
    return 'logged : ' + msg


if __name__ == '__main__':
    set_logger()  # 系统启动时配置logA
    app.run(debug=True)  # 启用debug
