import random



class Dynamic:
    array = None
    dp = None

    def __init__(this):
        this.array = []
        this.dp = []

    
    def add_to_array(this):
        this.array = [random.randint(25) for i in range(10)]

    def reset(this):
        this.array = []
        this.dp = []


    def memoization(this):


    def tabulation(this):
        this.dp[0] = this.array[0]
        this.dp[1] = this.array[1]

        length = len(this.array)

        for i in range(2, length):
            this.dp = max(this.array[i - 1], this.array[i - 2] + this.array[i])

        return this.dp


