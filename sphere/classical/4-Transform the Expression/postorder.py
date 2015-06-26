#!usr/bin/env python3

list_exp = []
tmp = []
def input_line():
    num = int(input())
    for i in range(num):
        exp = input()
        list_exp.extend(exp)
        list_exp.append(" ")
    #print(list_exp)

def postorder():
    for i in list_exp:
        if i.isalpha():
            print(i, end='')
        else:
            if i == " ":
                print("")
                continue

            tmp.append(i)
            if tmp[-1] == ')':
                tmp.pop()
                while tmp[-1] != '(':
                    print(tmp.pop(), end='')
                tmp.pop()

input_line()
postorder()

