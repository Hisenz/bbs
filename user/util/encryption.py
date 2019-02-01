from hashlib import sha1


def encryption(passsword):
    sh = sha1()
    sh.update(passsword.encode())
    return sh.hexdigest()