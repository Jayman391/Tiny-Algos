def partition(arr, low, high):
    if high > low:
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        partition(arr, low, i)
        partition(arr, i+1, high)
quickSort = lambda array, low, high : partition(array,low,high) if low < high else 0

    ### TEST CODE ###
#if __name__ == "__main__":
#    arr = [1,7,5,3,2,1]
#    n = len(arr)
#    quickSort(arr,0,n-1)
#    print(arr)
