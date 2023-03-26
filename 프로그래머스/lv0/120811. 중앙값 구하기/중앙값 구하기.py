def solution(array):
    array = sorted(array)
    centerIndex = len(array)//2
    return (array[centerIndex ] + array[-centerIndex - 1])/2