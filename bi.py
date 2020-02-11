# Python3 program to implement Binary
# Search for strings

# Returns index of x if it is present
# in arr[], else return -1
def binarySearch(arr, x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)

        res = (x == arr[m])

        # Check if x is present at mid
        if (res == 0):
            return m - 1

        # If x greater, ignore left half
        if (res > 0):
            l = m + 1

        # If x is smaller, ignore right half
        else:
            r = m - 1

    return -1


# Driver Code
if __name__ == "__main__":

    arr = ["contribute", "geeks",
           "ide", "practice"];
    x = "ide"
    result = binarySearch(arr, x)

    if (result == -1):
        print("Element not present")
    else:
        print("Element found at index",
              result)
