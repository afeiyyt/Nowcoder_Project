# -*- coding: utf-8 -*-
# 脚本工作

from flask_script import Manager
from c2 import app

manager = Manager(app)


@manager.command
def hello1(name):  # python manager.py hello name
    print 'hello', name


@manager.option('-n','--name',dest='name',default='nowcoder')
def hello2(name):
    print 'hello', name


@manager.command
def initialize_database():
    'initialize database'
    print 'database ...'


if __name__ == '__main__':
    manager.run()
