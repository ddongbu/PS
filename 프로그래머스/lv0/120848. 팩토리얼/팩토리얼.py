import math
def solution(n):
    for i in range(1,12):
        if n < math.factorial(i):
            return i-1