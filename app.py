from flask import Flask , render_template, request, url_for
from dao import post_dao, crowler
import user_app

app = Flask (__name__)

@app.route('/index.html', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        if request.args.get('page'):
            page_num = int(request.args.get('page'))
            start_num = (page_num + 4) // 5
            page_num_list = [n for n in range((start_num-1)*5+1, ((start_num-1)*5)+6)]
            if min(page_num_list) <= 0:
                page_num_list = [1, 2, 3, 4, 5]
            posts = post_dao.select_posts(page_num)
            return render_template('index.html', posts=posts, date=post_dao.get_date(), page=None, page_num_list=page_num_list)
        else:
            posts = post_dao.select_posts()
            page_num_list = [1, 2, 3, 4, 5]
            return render_template('index.html', posts=posts, date=post_dao.get_date(), page=None, page_num_list=page_num_list)
    if request.method == 'POST':
        posts = post_dao.select_posts()
        return render_template('index.html', posts=posts, date=post_dao.get_date(), page=None, page_num_list=None)

@app.route('/admin_page.html', methods=['POST', 'GET'])
def admin_page(title_list=None, link_list=None, for_num=0):
    if request.method == 'POST':
        if request.form.get('check'):
            checked_links = request.form.getlist('check')
            site_name = request.form.get('site_name')
            cro = crowler.Crowler()
            for link in checked_links:
                title, cnt = cro.site(site_name).get_post(link)
                post_dao.insert_post(site_name, title.__str__(), cnt.__str__(), str(post_dao.get_date()))
            cro = crowler.Crowler()
            title_list, link_list = cro.site(site_name).get_board()
            return render_template('admin_page.html', title_list=title_list, link_list=link_list, for_num=len(title_list), site_name=site_name)
        if request.form.get('site_name'):
            site = request.form['site_name']
            cro = crowler.Crowler()
            title_list, link_list = cro.site(site).get_board()
            return render_template('admin_page.html', title_list=title_list, link_list=link_list, for_num=len(title_list), site_name=site)
        else:
            return render_template('admin_page.html', title_list=None, link_list=None, for_num=0)
    elif request.method == 'GET':
        return render_template('admin_page.html', title_list=None, link_list=None, for_num=0)

@app.route('/post.html')
def post():
    posts = post_dao.select_posts()
    if request.method == 'POST':
        print("!!! POST 진입")
        return render_template('post.html', post = post, posts=posts, date=post_dao.get_date())
    elif request.method == 'GET':
        if request.args.get('post_no'):
            print("!!! POST 진입, post_no 발견.")
            post = post_dao.select_post(request.args.get("post_no"))
            print(post)
            return render_template('post.html', post=post, posts=posts, date=post_dao.get_date())
    else:
        print("Error")

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

@app.route('/testing.html')
def get_context_data(self, **kwargs):
    context = super(PostLV, self).get_context_data(**kwargs)
    paginator = context['paginator']
    page_numbers_range = 10 
    max_index = len(paginator.page_range)

    page = self.request.GET.get('page')
    current_page = int(page) if page else 1

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    context['page_range'] = page_range
    return context

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # , , port="5114"