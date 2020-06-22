from dao import db
import time

def get_date():
    # 출력 형식은 20200617 등의 해당 날짜 문자열이다.
    return time.strftime("%Y%m%d", time.localtime(time.time()))

def get_last_no():
    return db.select_one('''SELECT post_no FROM post ORDER BY post_no DESC LIMIT 1''')['post_no']

def insert_post(post_site_name, post_title, post_cnts, post_date):
    return db.excute_commit('''
            INSERT INTO post (post_site_name, post_title, post_cnts, post_date) 
            VALUES (?, ?, ?, ?)
            ''', (post_site_name, post_title, post_cnts, post_date))

def select_posts(page=1):
    # 페이지 숫자를 전달하면 끝에서부터 15개의 포스트를 순서에 맞게 반환한다.
    page_last_post_no = get_last_no()
    page_start_post_no = page_last_post_no - 15
    page_last_post_no = page_last_post_no - (page-1) * 15
    page_start_post_no = page_start_post_no - (page-1) * 15
    return reversed(db.select_all('''SELECT * FROM post where post_no BETWEEN ? AND ?''', (page_start_post_no, page_last_post_no)))

def select_post(no):
    return db.select_one('''SELECT * FROM post WHERE post_no=?''', (no,))

def update_post(no, post_site_name, post_title, post_cnts, post_date):
    # 업데이트 기능이 필요 없다고 판단하여 아직 건들지 않음.
    # 추후 필요 여부에 따라 작성하길 바람.
    # 삭제된 게시물입니다. 형식으로 변경
    return db.excute_commit('''
            UPDATE post 
            SET post_site_name=?, post_title=?, post_cnts=?, post_date=? 
            WHERE no=?            
            ''', (post_site_name, post_title, post_cnts, post_date, no))

# def delete_post(no):
#     return db.excute_commit('''DELETE FROM post WHERE post_no=?''', (no, ))