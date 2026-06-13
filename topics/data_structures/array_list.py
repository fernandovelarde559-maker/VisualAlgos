
class ArrayList:
    size = None
    data = None

    def __init__(this, size):
        this.data = []
        this.size == size


    def isEmpty(this):
        return this.size == 0
    
    def append(this, value):
        if(this.size < len(this.data)):
            this.data.append(value)
        else:
            print("Cannot append, List is full")

    def insert(this, value, index):
        if(this.size >= len(this.data)):
            print("Cannot insert, List is full")
        elif(index >= 0 and index <= this.size):
            for i in range(this.size, index, -1):
                this.data[i] = this.data[i - 1]
            this.data[index] = value
            this.size += 1
        else:
            print("Invalid index")

    def delete(this):
        if(this.isEmpty()):
            print("Array already empty")
        else:
            this.size = this.size - 1
            this.data.pop()
    
    def delete(this, index):
        if(this.isEmpty()):
            print("Cannot delete index, array already empty")
        elif(index < 0 or index >= this.size):
            print("Index out of bounds")
        else:
            for i in range(index, this.size, 1):
                this.data[i] = this.data[i + 1]
            this.data[this.size - 1] = 0
            this.size = this.size - 1
    
    def __str__(this):
        if(this.isEmpty()):
            print("List is empty, cannot print")
        else:
            string = ""
            for i in range(this.size):
                string += str(this.data[i]) + " "
            return string.strip()
        
if __name__ == "main":
    arraylist = ArrayList()

    


        


