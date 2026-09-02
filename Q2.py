class StringSorter:
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j].lower() < arr[min_idx].lower():
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
        return arr
n = int(input("Enter the number of strings: "))
strings_list = []
for i in range(n):
    strings_list.append(input(f"Enter string {i+1}: "))
sorter = StringSorter()
sorted_strings = sorter.selection_sort(strings_list)
print("Sorted list:", sorted_strings)