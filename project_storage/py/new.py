def g_task():
    n1 = yield "value 1"
    print(n1)
    n2 = yield "value 2"
    print(n2)
    n3 = yield "value 3"
    print(n3)


g = g_task()

v1 = next(g) # [1]
print(v1)    # [2]
v2 = next(g) # [3]
print(v2)    # [4]