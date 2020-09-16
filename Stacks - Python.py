#Stacks In Python
'''
1.Push : Insert at 
2.Pop : Delete 
3. Peek
4. Overflow
5. Underflow
'''
#Making a Function Of Stack

def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    top = len(stk)-1
def pop(stk):
    if isempty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def peek(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]
def display(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        print("Top Most Element : ", stk[top])
        for a in range(top-1,-1,-1):
            print(stk[a])

#Making Stack Program
stack = []
top = None

while True:
    print("-->Select any operation<---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Woah!! You Wanna Exit!!")
    ch = input("Select Your Choice(1,2,3,4,5) : ")
    
    if ch == "1":
        n = int(input("Enter The Element to be inserted : "))
        push(stack,n)
        
    if ch == "2":
        n = pop(stack)
        if stack == "underflow":
            print("Stack is Underflow ")
        else:
            print("Popped Element: ",n)
    if ch == "3":
        n = peek(stack)
        
        if stack == "underflow":
            print("Stack is Underflow ")
        else:
            print("peeked Element: ",n)
    if ch == "4":
        display(stack)
    if ch == "5":
        print("Thank You To Use this program!!  Visit Again")
        break
        
    

        
        
        
    
    
    
            
        
        







