from dao import db
import time

def get_date():
    # 출력 형식은 20200617 등의 해당 날짜 문자열이다.
    return time.strftime("%Y%m%d", time.localtime(time.time()))

def select_users():
    return db.select_all('SELECT * FROM user')

def select_users(user_no):
    return db.select_one('''
    SELECT * 
    FROM user 
    WHERE user_no=?
    ''', (user_no,))

def select_users_by_userid_and_userpw(user_id, user_pw):
    return db.select_one('''
    SELECT * 
    FROM user 
    WHERE user_id=? AND user_pw=?
    ''', (user_id, user_pw))

def insert_users(user_id, user_nick, user_pw, user_reg_date):
   

    return db.excute_commit('''
            INSERT INTO User (user_id, user_nick, user_pw, user_reg_date)
            VALUES (?, ?, ?, ?)                    
            ''', (user_id, user_nick, user_pw, user_reg_date))