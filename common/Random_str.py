import string
import random

def Ran_str(S):
    ran_str = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
    return ran_str

