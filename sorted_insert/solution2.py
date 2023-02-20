# With Recursion
def sorted_insert(elem, arr):
    n = len(arr)
    if n == 1:
        return arr + [elem] if arr[0] <= elem else [elem] + arr
    if elem <= arr[0]:
        return [elem] + arr
    return [arr[0]] + sorted_insert(elem, arr[1:])

if __name__ == "__main__":
    sorted_arr = [-2,1,5,6,9]

    print(sorted_insert(4, sorted_arr))