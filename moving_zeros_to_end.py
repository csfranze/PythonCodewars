# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


def move_zeros(arr):
    print(arr)
    new_arr = []
    for index in range(0, len(arr)):
        if type(arr[index]) == bool or arr[index] != 0:
            new_arr.append(arr[index])
    for _ in range(0, len(arr) - len(new_arr)):
        new_arr.append(0)
    return new_arr
