import numpy as np
lst = [1,2,3,4,5]
arr = np.array(lst)
#print(arr)
#print(arr.shape)
#lst1 = [1,2,3,4,5]
#lst2 = [2,3,4,5,6]
#lst3 = [4,5,6,7,8]
#arr1 = np.array([lst1,lst2,lst3])
#print(arr1)
#print(arr1.shape)

arr3 = np.array(lst)
arr3[2] = 5
#print(arr3[2])
lst4 = [1,2,3,4,5,6,7,8,9,10]
arr4 = np.array(lst4)
#print(arr4[1:])
#print(arr4[:-1])
#print(arr4[::])
#print(arr4[::-1])
#print(arr4[::-2])

lst1 = [1,2,3,4,5]
lst2 = [2,3,4,5,6]
lst3 = [4,5,6,7,8]
arr1 = np.array([lst1,lst2,lst3])
#print(arr1)
#print(arr1.shape)

## slicing 
#print(arr1[:,1])
#print(arr1[0:2,1:3])
#print(arr1[1:,3:])
#print(arr1[:,3:].shape)
#print(arr1[:,::4])

## using conditions 
 
arr5 = np.array(lst1)
#print(arr5<2) 
#print(arr5[arr5<2])

# changin the array 
#print(arr1.reshape(5,3))
#print(arr1)

# another way to create an array
#### rem np.arrange(start,stop,step)
arr6 = np.arange(1,21,1).reshape(2,10)
#print(arr6)

# Operations 
#print(arr1 *2)
#print(arr1 * arr1)

# ones and zeros 
#print(np.ones((5,5)))
#print(np.zeros((5,5)))

# random

print(np.random.randint(1,10,4).reshape(2,2))
print(np.random.randn(1,2))
print(np.random.random_sample((2,8)))