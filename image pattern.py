from PIL import Image
import numpy
import random
img=Image.open(r'C:\Users\Home\Pictures\heart.png')#your png image location
s=40#output pattern's size
r=img.resize((s,s)).convert('LA')
a=numpy.asarray(r)
def multiple_uniform():
    p=['!','@','#','$','%','^','&','*','(',')','-','+','=']#your pattern is filled with this
    for i in range(s+1):
        p.append(p[i])
    return p
def multiple_random():
    p=['!','@','#','$','%','^','&','*','(',')','-','+','=']#your pattern is filled with this
    for i in range(s):
        p.append(p[i])
    return random.choice(p)
def single_uniform():
    p='.'#your pattern is filled with this
    return(p)

for i in range(s):
     print('')
     for j in range(s):       
        if min(a[i][j])>50:
            print(multiple_uniform()[j],end='')#call your desired function here
        else:
            print(' ',end='')
        j+=1

# if you call multiple_uniform(), use multiple_uniform()[j] for vertical orientation, and use multiple_uniform()[i] for horizotal orientation
#  u can use unicode to print pattern with emoji
