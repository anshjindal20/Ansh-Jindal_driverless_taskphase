n = int(input("Enter number of integers: "))
hash_table = [[] for _ in range(10)]
for i in range(n):
    num = int(input("Enter number: "))
    index = num % 10

    bucket = hash_table[index]
    low = 0
    high = len(bucket)

    while low < high:
        mid = (low + high) // 2

        if bucket[mid] < num:
            low = mid + 1
        else:
            high = mid

    bucket.insert(low, num)
print("Hash Table:")
for i in range(10):
    print(i, ":", hash_table[i])