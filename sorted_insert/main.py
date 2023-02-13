def sorted_insert(elem, arr):
    n = len(arr)
    if n == 1:
        return arr + [elem] if arr[0] <= elem else [elem] + arr
    for i in range(n-1):
        if elem >= arr[i] and elem <= arr[i+1]:
            return arr[:i+1] + [elem] + arr[i+1:]
    return arr + [elem]


def recursive_sorted_insert(elem, arr):
    n = len(arr)
    if n == 1:
        return arr + [elem] if arr[0] <= elem else [elem] + arr
    if elem <= arr[0]:
        return [elem] + arr
    return [arr[0]] + recursive_sorted_insert(elem, arr[1:])
