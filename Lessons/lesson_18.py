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

#print(equatation())

def truth_table():
    out = ""
    A = 4*[False] + 4*[True]
    B = 2*[False,False,True,True]
    C = 4*[False, True]
    out += (f"|  A  |  B  |  C  |\n")
    for n in range(len(A)):
        out += (f"|  {int(A[n])}  |  {int(B[n])}  |  {int(C[n])}  |\n")
    return out
print(truth_table())

def truth_table_sized(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = letters[:n]
    collums = {}
    for x in range(n):
        collums[letters[x]] = (2**(x))*((2**(n-x-1))*[False] + (2**(n-x-1))*[True])
    return letters, collums

def print_truth_table(letters, collums):
    for let in letters:
        print(f"|  {let}  ", end="")
    print("|")

    for row in range(2**len(letters)):
        for val in range(len(letters)):
            print(f"|  {int(collums[letters[val]][row])}  ", end="")
        print("|")

    

letters, collums = truth_table_sized(5)
print_truth_table(letters, collums)