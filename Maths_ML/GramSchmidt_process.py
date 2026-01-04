import numpy as np
import numpy.linalg as la 

verySmallNumber = 1e-14 # 0.000000000001

A = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,0,3,4],
              [7,5,4,2]])

# ------ Gram Schmidt Process ------- #

# def GramSchmidt_B4(A):
#     """Use of GramSchemidt process for getting orthogonal set of vectors and orthonormal set."""
#     B = np.array(A,dtype = np.float128)
#     # Column 0 is the very first column vector so it dont need to be because it has no
#     # other vector to make it normal to.#
#     B[:,0] = B[:,0]/la.norm(B[:,0])
#     # Now for column 1 first we need to get the component of column 1 in column 0 direction,
#     # then subtract any overlap with our new zeroth vector.#
#     B[:,1] = B[:,1]-B[:,1]@B[:,0]*B[:,0]
#     # if B[:,1] is non zero then we will normalize vector
#     if la.norm(B[:,1]) > verySmallNumber:
#         B[:,1] = B[:,1]/la.norm(B[:,1])
#     else:
#         B[:,1] = np.zeros_like(B[:,1])
#     #similarly we will do for the column 2 and column 3
#     B[:,2] = B[:,2]-B[:,2]@B[:,0]*B[:,0]
#     B[:,2] = B[:,2]-B[:,2]@B[:,1]*B[:,1]
#     if la.norm(B[:,2])>verySmallNumber:
#         B[:,2]=B[:,2]/la.norm(B[:,2])
#     else:
#         B[:,2]=np.zeros_like(B[:,2])
#     B[:,3] = B[:,3]-B[:,3]@B[:,0]*B[:,0]
#     B[:,3] = B[:,3]-B[:,3]@B[:,1]*B[:,1]
#     B[:,3] = B[:,3]-B[:,3]@B[:,2]*B[:,2]
#     if la.norm(B[:,3])>verySmallNumber:
#         B[:,3]=B[:,3]/la.norm(B[:,3])
#     else:
#         B[:,3]=np.zeros_like(B[:,3])
    
# Above code using for loop for any type of matrices
    
def GramSchmidt_Basis(A):
    B = np.array(A,dtype = np.float128)
    for i in range (B.shape[1]):
        for j in range(i):
            B[:, i] = B[:,i] - B[:,i]@B[:,j]*B[:,j] 
            if la.norm(B[:,i])>verySmallNumber :
                B[:,i] = B[:,i]/la.norm(B[:,i]) 
            else :
                B[:,i] = np.zeros_like(B[:,i])
                    

    return B

def dimensions(A):
    return np.sum(la.norm(GramSchmidt_Basis(A), axis=0))

orthonormal = dimensions(A)
print(dimensions(A))
          
  