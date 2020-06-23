from flask import Flask , render_template, request, url_for
from dao import post_dao, crowler
import user_app

app = Flask (__name__)

@app.route('/index.html')
@app.route('/')
def index():
    posts = post_dao.select_posts()
    return render_template('index.html', posts=posts, date=post_dao.get_date())

@app.route('/admin_page.html', methods=['POST', 'GET'])
def admin_page(title_list=None, link_list=None, for_num=0):
    if request.method == 'POST':
        site_name = request.form['site_name']
        cro = crowler.Crowler()
        if site_name is not None:
            title_list, link_list = cro.site(site_name).get_board()
            return render_template('admin_page.html', title_list=title_list, link_list=link_list, for_num=len(title_list))
        else:
            return render_template('admin_page.html', title_list=None, link_list=None, for_num=0)
    elif request.method == 'GET':
        return render_template('admin_page.html', title_list=None, link_list=None, for_num=0)



@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/post_comment.html')
def post_comment():
    return render_template('/post_comment.html')

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

@app.route('/user_comment.html')
def user_commnet():
    return render_template('user_comment.html')

@app.route('/img_test.html')
def img_test():
    return render_template('img_test.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  