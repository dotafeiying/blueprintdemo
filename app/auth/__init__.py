# coding=utf-8

from flask import Blueprint
from flask import render_template

#: 初始化Main蓝图. 注意静态文件和模板文件夹路径
#: 模板路径是 root_path + template_folder
#: root_path 是 blueprintdemo的路径

auth = Blueprint('auth', __name__, static_folder='static',
                     template_folder='templates')
from . import views

