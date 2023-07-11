class MyQueue:

    def __init__(self):
        self.que = deque()
   
    def push(self, x: int) -> None:
        self.que.appendleft(x)
        
    def pop(self) -> int:
        for i in range (len(self.que)-1):
            return self.que.pop()
        
    def peek(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return len(self.que) == 0
