def sorted_insert(elem, arr):
    n = len(arr)
    if n == 1:
        return arr + [elem] if arr[0] <= elem else [elem] + arr
    for i in range(n-1):
        if elem >= arr[i] and elem <= arr[i+1]:
            return arr[:i+1] + [elem] + arr[i+1:]
    return arr + [elem]

if __name__ == "__main__":
    sorted_arr = [-2,1,5,6,9]

    print(sorted_insert(4, sorted_arr))