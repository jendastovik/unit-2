# Quiz 28
## Python code
```python
def sel_sort(x, keys):
    for i in range(len(x)-1):
        for n in range(i + 1, len(x)):
            if x[i] > x[n]:
                x[i], x[n] = x[n], x[i]
                keys[i], keys[n] = keys[n], keys[i]
    return x, keys

def dic_sort(dic):
    keys = list(dic.keys())
    vals = list(dic.values())
    vals, keys = sel_sort(vals, keys)
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = vals[i]
    return dic
```

## Output
![](/assets/qx.png)

## B part
![](/assets/bpart/qx.png)