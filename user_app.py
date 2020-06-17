from flask import Blueprint, request, render_template, redirect, url_for, session, abort



app = Blueprint('user', __name__, url_prefix='/user')

@app.route('/user_login.html')
def user_login():
    
    return render_template('user/user_login.html')

@app.route('/user_info.html')
def user_info():
    
    return render_template('user/user_info.html')

@app.route('/user_login_find.html')
def user_login_find():
    
    return render_template('user/user_login_find.html')

@app.route('/user_join.html')
def user_join():
    
    return render_template('user/user_join.html')

@app.route('/user_login.html')
def user_login():
    
    return render_template('user/user_login.html')



