binarysearch = lambda array, low, high, value : True if array[(high+low)//2] == value else binarysearch(array, low, (high+low)//2 -1, value) if array[(high+low)//2] > value else binarysearch(array, (high+low)//2 + 1, high, value) if high >= low else False

### TEST CODE ###
#if __name__ == "__main__":
#    arr = [1,2,3,4,5,6,7]
#    print(binarysearch(arr,0,len(arr)-1,2))
