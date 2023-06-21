if __name__ == '__main__':
    
    n = int(input())
    arr = map(int, input().split())
    arr_set = list(set(arr))
    arr_set.sort()
    print(arr_set[-2])
    
