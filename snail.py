Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

def snail(snail_map):
    s = []
    L = len(snail_map)
    if L == 1 and snail_map != [[]]:
        s.append(snail_map[0][0])
    if L % 2 == 1 and L > 1:
        for c in range(1,(L+1)//2):
            for j in range(c,L-c+2):
                s.append(snail_map[c-1][j-1])
            for i in range(c+1,L-c+2):
                s.append(snail_map[i-1][L-c])
            for j in range(1,L-2*c+2):
                s.append(snail_map[L-c][L-c-j])
            for i in range(1,L-2*c+1):
                s.append(snail_map[L-c-i][c-1])
        s.append(snail_map[(L-1)//2][(L-1)//2])
    if L % 2 == 0 and L > 1:
        for c in range(1,(L+2)//2):
            for j in range(c,L-c+2):
                s.append(snail_map[c-1][j-1])
            for i in range(c+1,L-c+2):
                s.append(snail_map[i-1][L-c])
            for j in range(1,L-2*c+2):
                s.append(snail_map[L-c][L-c-j])
            for i in range(1,L-2*c+1):
                s.append(snail_map[L-c-i][c-1])
    return s
