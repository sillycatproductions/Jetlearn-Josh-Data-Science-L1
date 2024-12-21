import numpy as np #numpy 

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(type(numbers))
sand = np.array(numbers)
print(type(sand))

#finfinfin = np.array([1, 2, 3, 4], "rahhh")
#print(finfinfin)

numnumnum = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75])

numnumnum += 1
print(numnumnum)

#nothing = np.zeros(9999999999)
#print(nothing)

something = np.ones(9)
print(something)
oohoohaahaah = np.array([5,5,5,5,5], dtype= "f")
print(oohoohaahaah)

d2thing = np.array([[1,2,3],[4,5,6]])
print(d2thing)

print('Array Dimension fin fin fin fin fin',d2thing.ndim)
print('Number of rows - columns fin fin fin fin fin', d2thing.shape)
print('Number of elements fin fin fin fin fin', d2thing.size)
print('Array size fin fin fin fin fin', d2thing.nbytes)

numarr = np.arange(0,1001)
print(numarr)

numarreven = np.arange(0,1001, 2)
print(numarreven)

numarrodd = np.arange(1,1001, 2)
print(numarrodd)

randoms = np.random.permutation(np.arange(1,1001))
print(randoms)
randoms2 = np.random.randint(1,1001)
print(randoms2)
random3 = np.random.rand(1,20)
print(random3)
print(random3.shape)

reshape = np.arange(1,10).reshape(3,3)
print(reshape)

reshape2 = np.arange(1,37).reshape(6,6)
print(reshape2)
reshape3 = np.arange(1,37).reshape(1,36)
print(reshape3)
reshape4 = np.arange(1,37).reshape(2,18)
print(reshape4)
reshape5 = np.arange(1,37).reshape(3,12)
print(reshape5)
reshape6 = np.arange(1,37).reshape(4,9)
print(reshape6)

perm = np.random.permutation(np.arange(1,1001))
print(perm)

sort = np.sort(perm)
print(sort)
