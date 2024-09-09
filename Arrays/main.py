o1d_array = [1, 2, 3, 4, 5]
print(o1d_array[0]) # Expected 1

o2d_array = [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 9]]

print(o2d_array[1][1]) # Expected 5

#Slices
print(o2d_array[0]) # Expected [1, 2, 3]
print(o2d_array[1]) # Expected [4, 5, 6]
print(o2d_array[2]) # Expected [7, 8, 9]
print(o2d_array[0][0:2]) # Expected [1, 2]
print(o2d_array[0:3]) # Expected [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(o2d_array[0:]) # Expected [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(o2d_array[0:3:2]) # Expected [[1, 2, 3], [7, 8, 9]]
print(o2d_array[0:2]) # Expected [[1, 2, 3], [4, 5, 6]]
print(o2d_array[0:2][0:2]) # Not possible to print [[1, 2], [4, 5]]
print(o2d_array[::-1]) # Expected [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
