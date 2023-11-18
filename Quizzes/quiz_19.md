# Quiz 19
## Python code
```python
def equatation():
    out = ""
    A = 4*[False] + 4*[True]
    B = 2*[False,False,True,True]
    C = 4*[False, True]
    res = []
    for n in range(len(A)):
        res.append((A[n] and B[n]) or (not B[n]) or (not(C[n] and B[n])))
    out += (f"| A | B | C |AB + not B + not CB|\n")
    for n in range(len(A)):
        out += (f"| {int(A[n])} | {int(B[n])} | {int(C[n])} |         {int(res[n])}         |\n")
    return out
```

## Output
![](/assets/q19.png)

