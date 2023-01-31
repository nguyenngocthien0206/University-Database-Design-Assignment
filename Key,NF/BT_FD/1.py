def check_contain(a,b):
    flag = 0
    for i in a:
        for j in b:
            if i == j:
                flag += 1
    if flag < len(a):
        return False
    else:
        return True

def get_key(r):
    r = sorted(r, key=len)
    key = r.copy()
    for i in range(0,len(r)):
        for j in range(0,len(r)):
            if check_contain(r[i],r[j]) and len(r[i]) < len(r[j]) and r[j] in key:
                key.remove(r[j])
    return key

r = ['ABE', 'BCE', 'BDE', 'ABCE', 'ABDE', 'BCDE', 'ABCDE']

print(get_key(r))