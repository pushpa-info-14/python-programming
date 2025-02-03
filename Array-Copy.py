array1 = [1,2,3,4]
array2 = array1
array2[0] = 10

print("----Array Assignment-------")
print(array1)
print(array2)

array1_copy = array1.copy()
array1_copy[0] = -1

print("----Shallow Copy-----------")
print(array1)
print(array1_copy)

array_2D = [[0,0],[0,0]]
array_2D_copy = array_2D.copy()
array_2D_copy[0][0] = 10

print("----2D-Shallow Copy--------")
print(array_2D)
print(array_2D_copy)
