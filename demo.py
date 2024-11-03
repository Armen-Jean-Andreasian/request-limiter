from src import AntiDDosGuard

adg = AntiDDosGuard()

# Let's say we got a request from 192.168.0.1
ip = "192.168.0.1"

# Checking IP Before Proceeding the request
# Overloading...
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))
print(adg.check(ip))

# A new instance
b = AntiDDosGuard()
print(b.check(ip))
print(b.check(ip))
print(b.check(ip))

# Works well
print(id(adg) == id(b))
