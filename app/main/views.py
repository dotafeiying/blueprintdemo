# coding=utf-8
from flask import Flask, request, redirect, session,url_for,render_template,flash,jsonify
from app import app
from app.decorators import admin_required,permission_required
from app.models import Permission
from app.models import User
from flask_login import login_required,LoginManager,login_user,UserMixin,logout_user,current_user
from .. import login_manager
from . import main

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/admin',methods=['GET','POST'])
@login_required
@admin_required
def admin():
    return '''Hello admin!
            <a href="/logout" style="color: red">退出</a>
        '''
    # return render_template("example.html")

@main.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/usr')
@login_required
def usr():
    return '你好，老-_-'

@main.errorhandler(403)
def page_not_found(e):
    return render_template('404.html'), 403

@main.route('/forbid',methods=['GET','POST'])
@login_required
@permission_required(Permission.FORBID)
def forbid():
    return 'Hello forbid'

@main.route('/user/<username>')
def main_index(username):
    return render_template('main_index.html', content='Hello Main App!',username=username)