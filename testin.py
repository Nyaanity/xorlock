from main import *


x = xorEncrypt("Hello World!", "key34423423234", to_bytes=True)

y = xorDecrypt(x, "key34423423234", from_bytes=True)


print(x)
