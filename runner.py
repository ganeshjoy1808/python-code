if __name__ == '__main__':
    n = int(input())
    arr=list(map(int,input().split()))
    f=-float('inf')
    s=-float('inf')
    for i in range(n):
        if(arr[i]>f):
            s=f
            f=arr[i]
        elif(arr[i]>s and arr[i]!=f):
            s=arr[i]
    print(s)
