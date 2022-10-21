### SELECTION SORT ALGORITHM

# find the lowest value.

# so basically, we are looking for the lowest number is the unsorted array and arranging it in the sorted array

A = [7, 4, 10, 8, 3, 1]

values = []

def get_lowest(L):
    min = L[0]

    for i in range(len(L)):
        if min > L[i]:
            min = L[i]
    
    return min

copy_array = A.copy()

for i in range(len(A)):

    num_array = copy_array[:]

    min = get_lowest(num_array)

    copy_array.remove(min)

    values.append(min)

print(f"The sorted version of: {A} is {values}, This was done using selection sort.")

