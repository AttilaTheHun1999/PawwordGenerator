import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&*()."

string = lower + upper + numbers + symbol
length = 20
password = "".join(random.sample(string, length))

print("Password:" + password)

