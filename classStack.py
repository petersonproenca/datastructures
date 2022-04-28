class Stack:
    def __init__(self,c):
        self.capacidade = c
        self.front,self.rear = 0,0
        self.stack = []
        
        return self.stack
    
    def push(self,x):
        if self.rear == self.capacidade:
            print("Erro StackOverflow")
        else:
            self.rear += 1
            self.stack.append(x)
        return self.stack
    
    
    def pop(self):
        if self.rear == 0:
            print("Erro Empty Stack")
        else:
            self.stack.pop()
            self.rear -= 1
        return self.stack
    
    def length(self):
        return self.rear
    
    def getHead(self):
        return self.stack[self.front]
    
    def __repr__(self):
        s = '['
        #print("[",end="")
        for i in self.stack:
            s += str(i)
            if not(i == self.stack[-1]):
                s += ','
        s += "]"
        return s
