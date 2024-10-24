from guard import AntiDDosGuard

a = AntiDDosGuard()
ip = "192.168.0.1"

print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))
print(a.check(ip))

b = AntiDDosGuard()
print('obj b')
print(b.check(ip))
print(b.check(ip))
print(b.check(ip))

print(id(a) == id(b))