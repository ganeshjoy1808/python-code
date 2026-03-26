if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    order=sorted(list(set([x[1]for x in records])))
    s=order[1]
    sl= sorted([x[0] for x in records if x[1] == s])
    for name in sl:
        print(name)
