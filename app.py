<<<<<<< HEAD
from flask import Flask , render_template, request, url_for, redirect ,flash
=======
from flask import Flask, render_template, request, url_for, redirect
>>>>>>> b8caceac858f6a4fda03f2274ee2e0c5a52fa452
from dao import crowler, post_dao, users_dao
from flask_wtf import FlaskForm
from form import Join_form
from flask_wtf.csrf import CSRFProtect
import re



app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def index():
    posts = post_dao.select_posts()
    return render_template('index.html', posts=posts, date=post_dao.get_date())

<<<<<<< HEAD
=======

@app.route('/admin_page.html', methods=['POST', 'GET'])
>>>>>>> b8caceac858f6a4fda03f2274ee2e0c5a52fa452
def admin_page(title_list=None, link_list=None, for_num=0):
    if request.method == 'POST':
        site_name = request.form['site_name']
        if (site_name is not None) and ('check' in request.form):
            post_links = request.form.getlist('check')
            print(post_links)
            cro = crowler.Crowler()
            title_list, link_list = cro.site(site_name).get_board()
            for link in post_links:
                print(link)
                title, cnt = cro.site(site_name).get_post(link)
                cro.edit_cnt(cnt)
                post_dao.insert_post(
                    site_name, str(title), str(cnt), post_dao.get_date())
            return render_template('admin_page.html', title_list=title_list, link_list=link_list, for_num=len(title_list), site_name=site_name)
        elif site_name is not None:
            cro = crowler.Crowler()
            title_list, link_list = cro.site(site_name).get_board()
            return render_template('admin_page.html', title_list=title_list, link_list=link_list, for_num=len(title_list), site_name=site_name)
        else:
            return render_template('admin_page.html', title_list=None, link_list=None, for_num=0, site_name=None)
    elif request.method == 'GET':
        return render_template('admin_page.html', title_list=None, link_list=None, for_num=0, site_name=None)


@app.route('/post.html', methods=['POST', 'GET'])
def post():
    if request.method == 'GET':
        post_no = request.args.get("post_no")
        posts = post_dao.select_posts()
        return render_template('post.html', posts=posts, date=post_dao.get_date(), post=post_dao.select_post(post_no))
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
<<<<<<< HEAD
    form = Join_form()
    
    if request.method == 'POST' :
        user_id = form.data.get('user_id')
        user_nick = form.data.get('user_nick')
        user_pw = form.data.get('user_pw')
        user_cpw = form.data.get('user_cpw')              
        user_reg_date = users_dao.get_date()
        pw = re.compile('^(?=.{8,}$)(?=.*[a-z])(?=.*[0-9])(?=.*\W).*$')    
        if pw.match(user_pw) == None:
            if user_pw != user_cpw:
                flash("비밀번호가 일치 하지 않습니다.")
                
            else:
                flash("비밀번호는 영문,특수문자,숫자 조합 8자리이상")
                
            return render_template('user_join.html', form = form)           
        else:
            users_dao.insert_users(user_id, user_nick, user_pw, user_reg_date)
        return redirect('/')                                   
    return render_template('user_join.html', form = form)  

    # if request.method == 'POST':            
    #     user_id = request.form.get('user_id')
    #     user_nick = request.form.get('user_nick')
    #     user_pw_get = request.form.get('user_pw')        
    #     user_reg_date = users_dao.get_date()
 
    #     users_dao.insert_users(user_id, user_nick, user_pw, user_reg_date)
  
    #     return redirect('/')
   
    # else:                               
    #     return render_template('user_join.html')        
        

@app.route('/user_login.html')
def user_login():
    return render_template('user_login.html')


@app.route('/img_test.html')
def img_test():
    return render_template('img_test.html')


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0")

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + cat_humor_schoool
    app.config['SECRET_KEY']='sdqfdsafjkledwq'
    csrf =  CSRFProtect()
    # cat_humor_schoool.init(app)
    app.run(port="5000", host= "0.0.0.0", debug=True)  
