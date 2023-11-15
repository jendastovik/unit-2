def procedure(n, m, s):
    import random
    random.seed(1234)
    out = "/    x   /   y(x)  /"
    for _ in range(n):
        x = random.randint(0, 100)
        yx = x*0.5*(m/s)**2
        out += f"\n/{str(x).center(8)}/ {str(yx).center(8)}/"
    return out
print(procedure(5, 3, 2))

def fromDec(num, base):
    res = []
    while num >= base:
        res.append(str(num % base))
        num //= base
    res.append(str(num))
    inLet = ""
    for n in res:
        inLet += toLet(int(n), base)
    return inLet[::-1]

def toLet(num, base):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num >= base:
        num -= base
        return letters[num]
    return str(num)

print(fromDec(10, 16))

