if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range (N):
        n = list(input().split())
        if n[0] == 'insert':
            lists.insert(int(n[1]), int(n[2]))
        if n[0] == 'print':
            print(lists)
        if n[0] == 'remove':
            lists.remove(int(n[1]))
        if n[0] == 'append':
            lists.append (int(n[1]))
        if n[0] == 'sort':
            lists.sort()
        if n[0] == "pop":
            lists.pop()
        if n[0] == 'reverse':
            lists.reverse()
          
    
    
