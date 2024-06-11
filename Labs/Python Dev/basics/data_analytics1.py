data = [1,5,7,8,9,10,14,15,20,17,18,11,16]
def calculateMean(data):
    return sum(data)/len(data)
def calculateMedian(data = [5,2,3,1,4,5]):
    data.sort()
    print(data)
    size = len(data)
    print(size)
    if size%2 ==0:
        element = (size//2) + (size//2+1)
        print(size//2)
    else:
       element = size//2
       print(element)
       return  data[element]
    

print(calculateMean(data))
print(calculateMedian(data))
print(calculateMedian())