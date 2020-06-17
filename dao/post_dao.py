from . import db

def select_posts():
    return db.select_all('SELECT * FROM post')

def select_post(no):
    return db.select_one('''
    SELECT * 
    FROM post 
    WHERE no=?
    ''', (no,))

def insert_post(subject, content, username, image_file):
    return db.excute_commit('''
            INSERT INTO post (subject, content, username, image_file) 
            VALUES (?, ?, ?, ?)
            ''', (subject, content, username, image_file))

def update_post(no, subject, content, username, image_path):
    return db.excute_commit('''
            UPDATE post 
            SET subject=?, content=?, username=?, image_path=? 
            WHERE no=?            
            ''', (subject, content, username, image_path, no))            

def delete_post(no):
    return db.excute_commit('''
            DELETE FROM post WHERE no=?                   
            ''', (no, ))