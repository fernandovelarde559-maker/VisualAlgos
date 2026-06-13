

class Node:
    val = None
    next = None

    def __init__(this, value):
        this.val = value
        this.next = None

    def getNext(this):
        return this.next
    
    def hasNext(this):
        return this.next != None
    
    def setNext(this, n):
        this.next = n

    def getData(this):
        return this.val
    
    def setData(this, v):
        this.val = v

    def __str__(this):
        return str(this.val) + " "
    
class LinkedList:
    first = None

    def __init__(this):
        this.first = Node

    
