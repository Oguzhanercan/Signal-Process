'''Signals and System for Computer Scientist Homework 1'''
import numpy as np #
import matplotlib.pyplot as plt

lenx = int(input("Enter the len of x : "))
lenh = int(input("Enter the len of h : "))
index_x = int(input("Enter the first index of x : "))
index_h = int(input("Enter the first index of h : "))

def inputarray(length): # Arrayi okuyoruz.
    array = []
    array = [int(input(f"{i+1}. element of array : ")) for i in range(length)]
    return array
print(f"Enter the values of array x : \n")
x = inputarray(lenx)
print(f"Enter the values of array h : \n")
h = inputarray(lenh)

def padding_zero(array,padsize):#padding
    for i in range(padsize):
        array.insert(i,0)
    for i in range(padsize):
        array.append(0)
    return array

def reverse(array,length):# Reverse array
    for i in range(int(len(array)/2)):
        temp = array[i]
        array[i] = array[length-i-1]
        array[length-1-i] = temp
    return array


def conv1d(x,h,lenx,lenh): # 1 dimensional convolution
    conved = []
    lenconved = lenh+lenx-1
    if (lenx >= lenh):
        a = x[:]
        b = h[:]
        a = padding_zero(a, lenh - 1)
        b = reverse(b, lenh)
    elif (lenh > lenx):
        a = h[:]
        b = x[:]
        a = padding_zero(a, lenx - 1)
        b = reverse(b,lenx)
    for i in range(lenconved):
        sum = 0
        for j in range(len(b)):
            sum = sum + a[j+i]*b[j]
        conved.append(sum)
    return conved
conved = conv1d(x,h,lenx,lenh)
print(conved)

#Visualization
t1 = np.arange(index_x,index_x+lenx,1)
t2 = np.arange(index_h,index_h+lenh,1)
t3 = np.arange(index_x,index_x+len(conved),1)
conved_np = np.convolve(x,h) # Numpy ile konvolüsyon.

fig, ([ax1, ax2],[ax3,ax4]) = plt.subplots(2,2,figsize = (20,5))
plt.subplots_adjust( hspace=0.5)
ax1.stem(t1,x,'tab:blue')
ax1.set_title('f(x)')
ax2.stem(t2, h, 'tab:orange')
ax2.set_title('h(x)')
ax3.stem(t3, conved, 'tab:green')
ax3.set_title('y(x)')
ax4.stem(t3, conved_np)
ax4.set_title('y(x) by numpy')
plt.show()
