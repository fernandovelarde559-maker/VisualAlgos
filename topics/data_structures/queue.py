


class Queue:
    front = None
    back = None
    queue = None

    def __init__(this):
        this.front = 0
        this.back = 0
        this.queue = []

    def isEmpty(this):
        return this.front == this.back
    
    def enqueue(this, value):
        new_back = (this.back + 1) % len(this.queue)
        
        this.queue[this.back] = value
        this.back = new_back

    def dequeue(this):
        if(Queue.isEmpty):
            print("The queue is Empty")
        else:
            this.front = (this.front + 1) % len(this.queue)

    def __str__(this):
        for i in len(this.queue):
            print(str(this.queue[i]) + " ")

if __name__ == "__main__":
    queue = Queue()



    