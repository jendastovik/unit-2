from matplotlib import pyplot as plt
def procedure(n, m, s):
    import random
    random.seed(1234)
    Ys = []
    Xs = []
    out = "/    x   /   y(x)  /"
    for _ in range(n):
        x = random.randint(0, 100)
        yx = x**(0.5*(m/s)**2)
        Xs.append(x)
        Ys.append(yx)
        yx = f"{yx:.2f}"
        out += f"\n/{str(x).center(8)}/ {str(yx).center(8)}/"
    return out, Xs, Ys
out, x, y = procedure(5, 3, 2)
print(out)

plt.style.use('ggplot')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.plot(x, y)
plt.show()

