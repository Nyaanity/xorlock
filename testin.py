from main import *


x = xorEncrypt("Hello World!", "key", to_hex=True, salt=1)
y = xorDecrypt(x, "key", from_hex=True, salt=1)


print(x, y)
