
# coding: utf-8

# In[1]:


import math
from math import sqrt


# In[13]:


class ComplexNo(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return ComplexNo(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return ComplexNo(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return ComplexNo(real, imaginary)

    def __truediv__(self, no):
        try:
            x = float(no.real ** 2 + no.imaginary ** 2)
            y = self * ComplexNo(no.real, -no.imaginary)
            real = y.real / x
            imaginary = y.imaginary / x
            return ComplexNo(real, imaginary)
        except Exception as e:
            print (e)
            
            
    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    

    def real(self):
        return self.real
   


    def imaginary(self):
        return self.imaginary


    def conj(self):
        return ComplexNo(self.real, - (self.imaginary))

    def arg(self):
        try:
            a=self.real
            b=self.imaginary
            z=sqrt((a*a)+(b*b))

            return(2*(math.atan(b/(a+z))))
        except Exception as e:
            print(e)


    def __str__(self):
        a = self.real
        b = abs(self.imaginary)
       
        if isinstance(a, float):
            a = "%.2f" % float(a)
     
        if  isinstance(b, float):
            b = "%.2f" % abs(float(b))
        if self.imaginary == 0:
            result = str(a)

        elif self.real == 0:
            result = str(b)
        elif self.imaginary > 0:
            result = str(a) + "+" +str(b) +"i"
        else:
            result = str(a) + "-" +str((b)) +"i"
        return result



# In[14]:


#to print addition of complex number
x = ComplexNo(1.369, 6);
y = ComplexNo(6,69);
final = [x+y]
print('\n'.join(map(str, final)))


# In[15]:


#to print division of complex number
x = ComplexNo(1, 6);
y = ComplexNo(6);
final = [x/y]
print('\n'.join(map(str, final)))


# In[16]:


#to print multiplication of complex number
x = ComplexNo(1, 6);
y = ComplexNo(6,2);
final = [x*y]
print('\n'.join(map(str, final)))


# In[24]:


#to print substraction of complex number
x = ComplexNo(1, -60);
y = ComplexNo(6,-2.684);
final = [x-y]
print('\n'.join(map(str, final)))


# In[18]:


#to print real number of complex number
x = ComplexNo(1);
final=[x.real]
print('\n'.join(map(str, final)))


# In[19]:


#to print imaginary of complex number
x = ComplexNo(1);
final=[x.imaginary]

print('\n'.join(map(str, final)))


# In[20]:


#to print conjugate of complex number
x = ComplexNo(1, 7);
final=[x.conj()]
print('\n'.join(map(str, final)))


# In[21]:


#to print argument of complex number
x = ComplexNo(-3,3);
final=[x.arg()]
print('\n'.join(map(str, final)))

