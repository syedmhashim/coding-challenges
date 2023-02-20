def countingSort(arr):
    n = len(arr)
    freq_arr = [0] * (max(arr)+1)
    for i in range(n):
        freq_arr[arr[i]] += 1
    sorted_arr = []
    for i in range(len(freq_arr)):
        sorted_arr = sorted_arr + ([i] * freq_arr[i])
    return sorted_arr

if __name__ == "__main__":
    arr = [1, 20, 16, 17, 7, 14, 2, 5, 8, 15, 4, 18, 19, 3, 11, 9, 10, 13, 6, 12]

    print(countingSort(arr))