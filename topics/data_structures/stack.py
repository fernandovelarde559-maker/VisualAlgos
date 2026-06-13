

class Stack:
    top = None
    stack = None

    def __init__(this):
        this.stack = []
        this.top = -1


    def isEmpty(this):
        return this.top == -1
    
    def push(this, value):
        this.stack.append(value)
        this.top += 1

    def pop(this):
        if(this.isEmpty()):
            print("Stack already empty")
        else:
            this.top = this.top - 1
            this.stack.pop()

    def size(this):
        return this.top + 1
    
    def __str__(this):
        if(this.isEmpty()):
            return "Stack is empty"
        else:
            string = ""
            for i in range(this.top + 1):
                string += str(this.stack[i]) + " "
            return string.strip()
            


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack)

    stack.pop()
    stack.pop()
    stack.pop()

    stack.pop()