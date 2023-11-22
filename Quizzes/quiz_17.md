# Quiz 17
## Python code
```python
def get_l3tt3rs(msg):
    vowels = {'a': 4, 'e': 3, 'i': 1, 'o': 0}
    out = ""
    for l in msg:
        if l in vowels:
            out += str(vowels[l])
        elif l == " ":
            out += "_"
        else:
            out += l
    return out
```

## Output
![](/assets/q17.png)