from itertools import chain, combinations
import copy
from os import read

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def repeat():
    return input('End of list? (y/n) : ').lower().startswith('y')

def read_file(filename):
    temp = []
    with open(filename,'r') as f:
        temp = [[s for s in line.replace(' ','')] for line in f]

    new_temp = []

    for i in temp:
        if i==['\n']:
            continue
        new_temp.append(i)

    s_lst = []

    for i in new_temp:
        if '\n' in i:
            i.remove('\n')
        s = ''.join(i)
        s_lst.append(s)

    new_lst = []

    for i in s_lst:
        i = i.replace(';','')
        new_lst.append(i)

    new_str_lst = []

    for i in new_lst:
        i = i.split('-')
        new_str_lst.append(i)

    r = new_str_lst[0]
    new_str_lst.remove(r)
    r = r[0]

    dic = {}

    for i in new_str_lst:
        dic[i[0]] = i[1]

    return (r,dic)

def closure(r):
    dic ={}
    sub = powerset(r)

    temp = []
    for i in sub:
        temp.append(i)

    temp.remove(())

    new_temp = []

    for i in temp:
        i = ''.join(i)
        new_temp.append(i)

    for i in new_temp:
        dic[i] = i

    return dic

def find_closure(dic,fd):
    while True:
        temp_clos = copy.deepcopy(dic)
        for i in dic:
            for j in fd:
                if j in dic[i]:
                    dic[i] += fd[j]
                    subset = set(dic[i])
                    sorted_subset = sorted(subset)
                    sstring = ''.join(sorted_subset)
                    dic[i] = sstring

        if temp_clos == dic:
            break
    return dic

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

def main():
    input = read_file('C:\\Users\\84702\\Desktop\\BT_FD\\testcase\\testcase2.txt')
    print(input)
    r = input[0]
    fd = input[1]
    dic = closure(r)
    temp_fd_lst = []

    for i in fd:
        temp_fd_lst.append(i)
        temp_fd_lst.append(fd[i])

    s = ''.join(temp_fd_lst)

    st = set()

    for i in s:
        st.add(i)

    st = sorted(st)
    temp_fd_str = ''.join(st)
    if (temp_fd_str == r):
        clos = find_closure(dic,fd)

        key_lst = []

        for i in clos:
            if clos[i] == r:
                key_lst.append(i)

        key = get_key(key_lst)

        print(key)
    else:
        for i in st:
            if i not in r:
                print(i,'not in R')
        print('Please edit input.')

if __name__ == '__main__':
    main()