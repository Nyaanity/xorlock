from main import *


x = xorEncrypt("Hello World!", "key45", to_uid=True, salt=5)
y = xorDecrypt(x, "key45", from_uid=True, salt=5)


print(x, y)
