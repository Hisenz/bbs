from user.models import User
from .encryption import encryption

ERROR = -1
SUCCESS = 1


def add_user(email, password, nickname):
    try:
        user = User()
        user.email = email
        user.password = encryption(password)
        user.nickname = nickname
        user.save()
    except Exception as e:
        print(e)
        return False
    return True


def select_email(email):
    if len(User.objects.filter(email=email)):
        return True
    else:
        return False


def select_nickname(nickname):
    if len(User.objects.filter(nickname=nickname)):
        return True
    else:
        return False


def login(email, password):
    if select_email(email):
        user = User.objects.get(email=email)
        if user.password == encryption(password):
            return user
    return None


def get_user(user_id):
    try:
        return User.objects.get(pk=user_id)
    except Exception as e:
        return None


def get_user_for_email(email):
    try:
        return User.objects.get(email=email)
    except Exception as e:
        return None


def modify_information(kwargs):
    if login(kwargs['email'], kwargs['password']):
        user = User.objects.get(email=kwargs['email'])
        user.nickname = kwargs['nickname']
        user.description = kwargs['description']
        if kwargs['avatar']:
            user.avatar = kwargs['avatar']
        user.email = kwargs['email']
        user.gender = kwargs['gender']
        user.save()

        return SUCCESS
    return ERROR
