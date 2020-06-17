from flask import Flask , render_template
from dao import post_dao
import user_app

app = Flask (__name__)

#메인페이지
@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_page.html')
def admin_page():

    return render_template('admin_page.html')


@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/quick_move.html')
def quick_move():
    return render_template('quick_move.html')

@app.route('/user_info.html')
def user_info():
    return render_template('user_info.html')

@app.route('/user_info_find.html')
def user_info_find():
    return render_template('user_info_find.html')

@app.route('/user_join.html')
def user_join():
    return render_template('user_join.html')

@app.route('/user_login.html')
def user_login():
    return render_template('user_login.html')

@app.route('/img_test.html')
def img_test():

    return render_template('img_test.html')




if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5104", debug=True)

