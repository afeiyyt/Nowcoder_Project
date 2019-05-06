# -*- coding: utf-8 -*-

from flask import Flask, render_template

# 定义一个应用
app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'


@app.route('/index/')
@app.route('/')
def index():
    return 'hello'


@app.route('/profile/<int:uid>/', methods=['GET', 'POST'])  # 定义支持的方法
def profile(uid):
    colors = ('red', 'green')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)


if __name__ == '__main__':
    app.run(debug=True)  # 启用debug
