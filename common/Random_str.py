import string
import random

def Ran_str(S):
    ran_str = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
    return ran_str

def Random_num():
    random_number = random.randint(1, 10)
    return random_number