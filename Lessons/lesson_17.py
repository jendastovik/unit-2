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
print(get_l3tt3rs("hello world"))
print(get_l3tt3rs("Why did I choose CS?"))
print(get_l3tt3rs("Remember the Figure Caption"))