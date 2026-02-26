import math

a = input("a: ")
b = input("b: ")

print(f"a: {a}, b: {b}")

#You already know the basics, e.g. power, exponentials

math.pow(a, b) #a to the power of b

#HCF & LCM
hcf = math.gcd(a, b)
lcm = math.lcm(a, b)

print(f"HCF: {hcf}, LCM: {lcm}")

#Integer Sqrt -> for prime checks
aisqrt, bisqrt = math.isqrt(a), math.isqrt(b) 

print(f"rooted: {aisqrt}, {bisqrt}")