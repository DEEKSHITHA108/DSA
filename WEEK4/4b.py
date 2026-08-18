def quick_sort(a, low, high):
    if low < high:
        i = low
        j = high
        pivot = a[low]

        while i < j:
            while i < high and a[i] <= pivot:
                i = i + 1

            while a[j] > pivot:
                j = j - 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        a[low], a[j] = a[j], a[low]

        quick_sort(a, low, j - 1)
        quick_sort(a, j + 1, high)

n=int(input("Enter the number of elements: "))
arr=[]
print("Enter the elements:")
for i in range(n):
   arr.append(int(input()))
arr=quick_sort(arr)
print("Sorted array:")
for element in arr:
   print(element,end=" ")
