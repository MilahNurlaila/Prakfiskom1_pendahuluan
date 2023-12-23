#Tugas Praktikum Fisika Komputasi (4)
#Soal No.1
import numpy as np

# Membuat matriks 2x2
M = np.array([[1, 2], [3, 4]])

# Menghitung determinan matriks
determinant = np.linalg.det(M)

print('determinant:\n', determinant)

#Soal No.2
# Membuat matriks 2x2
M = np.array([[10, -22], [3, 45]])

# Menghitung invers matriks
inverse_of_M = np.linalg.inv(M)

print('inverse_of_M:\n', inverse_of_M)

#Soal No.3
from numpy.linalg import \
              cond
A = np.array([[1,10**-10],
              [10**-10,1]])
print('Condition number:\n', cond(A))

#Soal No.4
from numpy.linalg import \
              matrix_rank
A = np.array([[1,2],
              [3,4]])
print('Rank:\n', matrix_rank(A))
b = np.array([[5], [6]])
A_b = np.concatenate((A, b), axis = 1)
print('Augmented matrix:\n', A_b)

#Soal No.5
# Tentukan matriks Anda (contoh matriks 3x3)
A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Hitung peringkat matriks
rank = np.linalg.matrix_rank(A)

# Hitung dimensi ruang nol
num_columns = A.shape[1]
nullity = num_columns - rank

# Cetak hasil
print("Matriks:")
print(A)
print("Peringkat Matriks:", rank)
print("Dimensi Ruang Nol:", nullity)
