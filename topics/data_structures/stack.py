

class Stack:
    size = None
    stack = None

    def __init__(this, size):
        this.size = size
        this.stack = []


    def isEmpty(this):
        return this.size == -1
    
    def push(this, value):
        this.stack.append(value)

    def pop(this):
        this.stack

