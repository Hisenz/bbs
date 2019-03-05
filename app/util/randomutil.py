import random


def generate(length):
    str = 'qwertyuiopasdfghjklzxcvbnm1234568790'
    code = ""
    for i in range(length):
        code += random.choice(str)
    return code