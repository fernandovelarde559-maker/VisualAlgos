import random
import time

class BogoSort:

    bogo = None

    def __init__(this):
        this.bogo = []

    def add_random(this):
        for i in range(10):
            this.bogo.append(random.randint(1, 50))

    def is_sorted(this):
        for i in range(len(this.bogo) - 1):
            if this.bogo[i] > this.bogo[i + 1]:
                return False
        return True

    def bogo_sort(this):
        start_time = time.perf_counter()
        while not this.is_sorted():
            random.shuffle(this.bogo)
        end_time = time.perf_counter()
        result_time = end_time - start_time
        print("Finished Sorting!\nTime: " + str(result_time))
            

    def __str__(this):
        string = ""
        for i in range(len(this.bogo)):
            string += str(this.bogo[i]) + " "
        return string
    
if __name__ == "__main__":
    bogo = BogoSort()
    bogo.add_random()

    print(bogo)

    bogo.bogo_sort()

    print(bogo)