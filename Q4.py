def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        print("Error: Matrix multiplication is not possible.")
        return None

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

A = []
print("Enter first matrix:")
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

B = []
print("Enter second matrix:")
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

result = matrix_multiply(A, B)

if result is not None:
    print("Result:")
    for row in result:
        print(*row)