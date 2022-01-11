def compare(arr, i, j) :
    if j > i:
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        compare(arr, i+1, j)
        compare(arr,i,j-1)
bubble = lambda array, start, end : array if compare(array, start, end) == 0 else compare(array,start,end)

### TEST CODE ###
#if __name__ == "__main__":
#    arr = [7,6,5,4,6,9,7,3,6,6,6,3,6,2,1]
#    bubble(arr,0,len(arr)-1)
#    print(arr)
