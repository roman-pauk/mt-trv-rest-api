from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'pauk83258325@gmail.com', '8325')
]

useremail_mapping = {u.email: u for u in users}

userid_mapping = {u.id: u for u in users}

def autenticate(useremail, password):
    user = useremail_mapping.get(useremail, None)
    if user and safe_str_cmp(user.password, password):
        return user
    return None

def identity(payload):
    userid = payload['identity']
    return userid_mapping.get(userid, None)