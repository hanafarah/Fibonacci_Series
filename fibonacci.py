""" created a function called Fibonacci where it takes the sum of two numbers
Usually starts with a 0 and 1.
The Fibonacci sequence is shown as 0, 1, 1, 2, 5, 8, 13, 21, 34, 55......"""


class Fibonacci:
    """Iterator of the Fibonacci series for a given values"""

    def __init__(self, num=int) -> list[int]:
        self.num = num
        if not isinstance(self.num, int):
            raise ValueError('must be in integer')
        if num < 0:
            raise ValueError("postive number")

        self.first = 0   # first value in the Fibonacci sequence
        self.second = 1  # second value in the Fibonacci sequence

    def __iter__(self):

        return self

    def __next__(self):

        if self.num == 0:
            raise StopIteration('complete')
        self.num -= 1
        value = self.first + self.second
        self.first = self.second
        self.second = value
        return self.first


# to test functionality:
# my_list = [sequence for sequence in Fibonacci(10)]
# print(my_list)
