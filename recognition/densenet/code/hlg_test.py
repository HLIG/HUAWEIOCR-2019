import numpy as np

a=np.zeros([2,2,3])
a[0::]=np.array([[1,2,3],[1,2,4]])
a[1::]=np.array([[2,5,3],[2,5,3]])


print a
a=a.max(0)
print '============================'
print a