class Stack:
    
    def __init__(self, size):
        self.size = size
        self.stack = [0]*size
        self.top = -1
        
    def stack_push(self, item):
        self.top += 1
        if self.top == self.size:
            self.top -= 1
            print('overflow!')
        else:
            self.stack[self.top] = item

    def stack_pop(self):
        if self.top == -1:
            print('underflow')
            return 0
        else:
            self.top -= 1
            return self.stack[self.top+1]
        
    def stack_isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def stack_isFull(self):
        if self.top == self.size -1:
            return True
        else: 
            return False
    
    def stack_peek(self):
        if self.top == -1:
            return 0
        else:
            return self.stack[self.top]
        
# print(S) 했을때 S.stack이 프린트 되게 하고싶은데 이 부분은 생각이 안나네요

S = Stack(3)
S.stack_push(1)
print('after push 1', S.stack, S.top)
S.stack_push(3)
print('after push 3', S.stack, S.top)
print('pop:', S.stack_pop())
print('after first pop', S.stack, S.top)
print('pop:', S.stack_pop())
print('pop:', S.stack_pop())
S.stack_push(1)
print('after push 1', S.stack, S.top)
S.stack_push(2)
print('after push 2', S.stack, S.top)
S.stack_push(3)
print('after push 3', S.stack, S.top)
S.stack_push(4)
print('after push 4', S.stack, S.top)
print('peek', S.stack_peek())
print('final stack', S.stack, S.top)