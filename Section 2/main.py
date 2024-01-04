import numpy as np

mylist = [1, 2, 3, 4, 5]

print(type(mylist))
myarray = np.array(mylist)

print(type(myarray))

print(np.arange(1, 101, 1))

print(np.zeros(shape=(10, 10)))


np.random.seed(101)

arr = np.random.randint(0, 100, 10)
print(arr)


arr2 = np.random.randint(0, 100, 10)
print(arr2) 

print(arr.reshape(5, 2))