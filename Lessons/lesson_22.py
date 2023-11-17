from matplotlib import pyplot as plt

def graphFun():
    Xs = []
    Ys = []
    for x in range(-100, 100, 2):
        Xs.append(x/10)
        Ys.append(2*(x/10 + 5)**2)
    return Xs, Ys

Xs, Ys = graphFun()
plt.style.use('ggplot')
plt.plot(Xs, Ys)
plt.xlabel("x")
yLabel = "f(x): 2(x + 5)^2"
plt.ylabel(yLabel)
plt.show()
