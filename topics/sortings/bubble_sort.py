import random 
import time

class Bubble:
    nums = None

    def __init__(this, nums):
        this.nums = []

    def load_array(this):
        this.nums = [this.nums.append(random.randint(1, 50)) for i in range(10) ]

    def bubble_sort(this):
        