def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

selection_sort(arr)

print("Sorted array:")

for element in arr:
    print(element, end=" ")