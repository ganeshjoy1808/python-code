if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        arg=(input()).split()
        x=arg[0]
        if x == "append":
            list1.append(int(arg[1]))
        elif x=="insert":
            list1.insert(int(arg[1]),int(arg[2]))
        elif x=="print":
            print(list1)
        elif x=="sort":
            list1.sort()
        elif x=="pop":
            list1.pop()
        elif x=="reverse":
            list1.reverse()
        elif x=="remove":
            list1.remove(int(arg[1]))
