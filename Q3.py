class Search:
    def selection_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if arr[j].lower() < arr[min_index].lower():
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    def binary_search(self, arr, key):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid].lower() == key.lower():
                return mid
            elif arr[mid].lower() < key.lower():
                low = mid + 1
            else:
                high = mid - 1

        return -1
n = int(input("Enter number of strings: "))
arr = []
for i in range(n):
    arr.append(input("Enter string: "))
obj = Search()
obj.selection_sort(arr)
print("Sorted list:", arr)
key = input("Enter string to search: ")
result = obj.binary_search(arr, key)
if result != -1:
    print("String found at index", result)
else:
    print("String not found")