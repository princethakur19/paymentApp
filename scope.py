# username = "princethakur"

# def func():
#     username = "prince"
#     print(username)

# print(username)
# func()

def pycoder(n):
    def actual(x):
        return n ** x
    return actual

f = pycoder(2)
g = pycoder(3)

print(f(3))
print(g(3))