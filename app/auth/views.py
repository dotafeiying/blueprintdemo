# coding=utf-8
from flask import Flask, request, redirect, session,url_for,render_template,flash,jsonify
from app import app
from app.decorators import admin_required,permission_required
from app.models import Permission
from app.models import User
from flask_login import login_required,LoginManager,login_user,UserMixin,logout_user,current_user
from .. import login_manager
from . import auth

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route("/",methods=["POST","GET"])
@auth.route("/login",methods=["POST","GET"])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        print(username,password)
        user = User.query.filter_by(username=username).first()
        print(user)
        if user is not None and user.verify_password(password):
            print('a')
            #login_user() 函数，在用户会话中把用户标记为已登录
            login_user(user)
        # session['username']=request.form['username']
        # session['password']=request.form['password']
            return redirect(request.args.get("next") or url_for('main.index'))
        flash('用户名或密码错误！','error')
    return render_template('login.html')

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
