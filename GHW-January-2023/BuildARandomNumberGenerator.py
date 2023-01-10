import time

now = int(time.time()) % 10
now *= int(time.time()) % 1234 + int(time.time()
                                     ) % 1214 / int(time.time()) % 2182 + int(time.time()) % 17894
now = int(now % 10)

print(now)
