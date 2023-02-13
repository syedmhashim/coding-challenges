def countingSort(arr):
    n = len(arr)
    freq_arr = [0] * (100)
    for i in range(n):
        freq_arr[arr[i]] += 1
    print(freq_arr)
