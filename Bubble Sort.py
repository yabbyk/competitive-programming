def countSwaps(a):
    n = len(a)
    numSwaps = 0
    
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] , a[j]
                numSwaps += 1
                
    return a , numSwaps
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    a , num_Swaps = countSwaps(a)
    
    print("Array is sorted in",num_Swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    countSwaps(a)
