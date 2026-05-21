


class ArrayList:
    size = None
    array = None

    def __init__(this, size):
        this.size = size
        this.array = [size for i in range(size)]


    def isEmpty(this):
        return this.size == -1