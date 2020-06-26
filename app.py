from flask import Flask , render_template, request, url_for, redirect
from dao import crowler, post_dao, users_dao



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


@app.route('/post.html',)
def post():
    posts = post_dao.select_posts()
    return render_template('post.html', posts=posts, date=post_dao.get_date())

@app.route('/quick_move.html')
def quick_move():
    return render_template('quick_move.html')

@app.route('/user_info.html')
def user_info():
    return render_template('user_info.html')

@app.route('/user_info_find.html')
def user_info_find():
    return render_template('user_info_find.html')

@app.route('/user_join.html', methods=['POST', 'GET'])
def user_join():
    if request.method == 'POST':            
        user_id = request.form.get('user_id')
        user_nick = request.form.get('user_nick')
        user_pw = request.form.get('user_pw')        
        user_reg_date = users_dao.get_date()
      
       

        users_dao.insert_users(user_id, user_nick, user_pw, user_reg_date)
        
        
        return redirect('/')
        
    else:                               
        return render_template('user_join.html')        
        

@app.route('/user_login.html')
def user_login():
    return render_template('user_login.html')

@app.route('/img_test.html')
def img_test():
    return render_template('img_test.html')

if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0")
    app.run(port="5000", host= "127.0.0.1", debug=True)  