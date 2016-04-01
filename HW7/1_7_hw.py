import scipy.constants as c
#part 1
def energy_n(n):
  return round(float(-1*((c.m_e/(2*(c.hbar**2)))*(((c.e**2)/(4*c.pi*c.epsilon_0))**2))*(1/float(n**2)))/c.e,3)


# print 'n = 1' 
# ans= energy_n(1) 
# print ans
# print 'n = 2' 
# ans= energy_n(2) 
# print ans
# print 'n = 3' 
# ans= energy_n(3) 
# print ans

#Part 2
def degToRad(deg):
  return round(float(deg)*(c.pi/180.0),5)


def radToDeg(rad):
  return round(float(rad)*(180.0/c.pi),5)

# print 'degToRad(90)' 
# ans=degToRad(90) 
# print ans
# print 'degToRad(180)' 
# ans=degToRad(180) 
# print ans
# print 'degToRad(270)' 
# ans=degToRad(270) 
# print ans
# print 'radToDeg(3.14)' 
# ans=radToDeg(3.14) 
# print ans
# print 'radToDeg(3.14/2.0)' 
# ans=radToDeg(3.14/2.0) 
# print ans
# print 'radToDeg(3.14*3/4)'
# ans=radToDeg(3.14*3/4) 
# print ans

#Part 3
import numpy as np
def sphericalToCartesian(r,theta,phi):
  x=round( r*np.cos(phi)*np.sin(theta),5)
  y=round( r*np.sin(phi)*np.sin(theta),5)
  z=round(r*np.cos(theta),5)
  return x,y,z

def cartesianToSpherical(x, y, z):
  infinity = round(np.pi/2,5)
  r = round(np.sqrt(x**2+y**2+z**2),5)
  theta = round(np.arccos(z/r),5)
  phi = round(np.arctan2(y,x),5)
  return r,theta,phi

# theta = degToRad(25)
# phi = degToRad(60)

# print sphericalToCartesian(3,theta,phi)

# ans=sphericalToCartesian(3,0,np.pi)
# print ans
# ans=sphericalToCartesian(3,np.pi/2.0,np.pi/2.0)
# print ans
# ans=sphericalToCartesian(3,np.pi,0)
# print ans
# ans=cartesianToSpherical(3,0,0)
# print ans
# ans=cartesianToSpherical(0,3,0)
# print ans
# ans=cartesianToSpherical(0,0,3)
# print ans
# ans=cartesianToSpherical(0,-3,0)
# print ans

def fact(n):
  if n == 0: return 1 
  return n*fact(n-1)

# def fact(n):
#   print n
#   total = 0
#   for x in range(n):
#     print total
#     print x
#     total*=(x+1)

  return total

# print 'fact(3)'
# ans=fact(3) 
# print ans
# print 'fact(5)'
# ans=fact(5) 
# print ans
# print 'fact(4)'
# ans=fact(4) 
# print ans
# print 'fact(1)'
# ans=fact(1) 
# print ans
from scipy.special import legendre

#new thing learned, closures.
# def assocLegendre(m,l):
#   derivative = np.polyder(legendre(l),m) #this part is executed only when f(x) is called
#   def eqn_1(theta):
#     x = np.cos(theta)
#     return ((1-x*x)**(np.absolute(m)/2.0))*derivative(x) # x is passed into the derivative and resolved
#   return eqn_1
def p00(theta):
  return 1

def p01(theta):
  return np.cos(theta)

def p02(theta):
  return 0.5*(3*np.cos(theta)**2-1)

def p03(theta):
  return 0.5*(5*np.cos(theta)**3-3*np.cos(theta))

def p11(theta):
  return np.sin(theta)

def p12(theta):
  return 3*np.sin(theta)*np.cos(theta)

def p13(theta):
  return 1.5*np.sin(theta)*(5*np.cos(theta)**2-1)

def p22(theta):
  return 3*np.sin(theta)**2

def p23(theta):
  return 15*np.sin(theta)**2*np.cos(theta)

def p33(theta):
  return 15*np.sin(theta)*(1-np.cos(theta)**2)

def assocLegendre(m,l):
  if m==0 and l==0:
    return p00
  elif m==0 and l==2:
    return p02
  elif m==1 and l==1:
    return p11
  elif m==3 and l==3:
    return p33
  elif m==0 and l==1:
    return p01
  elif m==2 and l==3:
    return p23
  elif m==2 and l==2:
    return p22
  elif m==1 and l==3:
    return p13
  elif m==1 and l==2:
    return p12
  elif m==0 and l==3:
    return p03
  else:
    return None


# print 'f=assocLegendre(0,0)' 
# print 'f(1)' 
# f=assocLegendre(0,0) 
# ans=f(1)
# print ans

# print 'f=assocLegendre(1,1)' 
# print 'f(1)' 
# f=assocLegendre(1,1) 
# ans=f(c.pi/2)
# print ans

# print 'f=assocLegendre(2,3)' 
# print 'f(1)' 
# f=assocLegendre(2,3) 
# ans=f(1)
# print ans

# print 'f=assocLegendre(2,3)' 
# print 'f(0)' 
# f=assocLegendre(2,3) 
# ans=f(0)
# print ans

def lag00(x):
  return 1
def lag01(x):  
  return np.poly1d([-1,1])(x)
def lag11(x):
  return np.poly1d([-2,4])(x)
def lag10(x):
  return 1
def lag02(x):
  return np.poly1d([1,-4,2])(x)
def lag12(x):
  return np.poly1d([3,-18,18])(x)
def lag22(x):
  return np.poly1d([12,-96,144])(x)
def lag21(x):
  return np.poly1d([-6,18])(x)
def lag20(x):
  return 2
def lag03(x):
  return np.poly1d([-1,9,-18,6])(x)
def lag13(x):
  return np.poly1d([-4,48,-144,96])(x)
def lag23(x):
  return np.poly1d([-20,300,-1200,1200])(x)
def lag33(x):
  return np.poly1d([-120,2160,-10800,14400])(x)
def lag32(x):
  return np.poly1d([60,-600,1200])(x)
def lag31(x):
  return np.poly1d([-24,96])(x)
def lag30(x):
  return 6


from scipy.special import laguerre
def assocLaguerre(p,qmp):
  if p == 0 and qmp == 0:
    return lag00
  elif p == 0 and qmp == 1:
    return lag01
  elif p == 1 and qmp == 1:
    return lag11
  elif p == 1 and qmp == 0:
    return lag10
  elif p == 0 and qmp == 2:
    return lag02
  elif p == 1 and qmp == 2:
    return lag12
  elif p == 2 and qmp == 2:
    return lag22
  elif p == 2 and qmp == 1:
    return lag21
  elif p == 2 and qmp == 0:
    return lag20
  elif p == 0 and qmp == 3:
    return lag03
  elif p == 1 and qmp == 3:
    return lag13
  elif p == 2 and qmp == 3:
    return lag23
  elif p == 3 and qmp == 3:
    return lag33
  elif p == 3 and qmp == 2:
    return lag32
  elif p == 3 and qmp == 1:
    return lag31
  elif p == 3 and qmp == 0:
    return lag30

  

# print 'f=assocLaguerre(0,0)' 
# print 'f(1)' 
# f=assocLaguerre(0,0) 
# ans=f(1)
# print ans
# print 'f=assocLaguerre(1,1)' 
# print 'f(1)' 
# f=assocLaguerre(1,1) 
# ans=f(1)
# print ans
# print 'f=assocLaguerre(2,2)' 
# print 'f(1)' 
# f=assocLaguerre(2,2) 
# ans=f(1)
# print ans
# print 'f=assocLaguerre(2,2)' 
# print 'f(0)' 
# f=assocLaguerre(2,2) 
# ans=f(0)
# print ans


import scipy.constants as c
import numpy as np 

def angular_wave_func(m,l,theta,phi):
  e = (-1)**m if m>0 else 1
  return np.round(e*np.sqrt(((1.0+2*l)*fact(l-abs(m)))/(4.0*c.pi*float(fact(l+abs(m)))))*np.exp((0+1j)*m*phi)*assocLegendre(m,l)(theta),5)


# print 'angular_wave_func(0,0,0,0)' 
# ans=angular_wave_func(0,0,0,0) 
# print ans
# print 'angular_wave_func(0,1,c.pi,0)' 
# ans=angular_wave_func(0,1,c.pi,0) 
# print ans
# print 'angular_wave_func(1,1,c.pi/2,c.pi)' 
# ans=angular_wave_func(1,1,c.pi/2,c.pi) 
# print ans
# print 'angular_wave_func(0,2,c.pi,0)' 
# ans=angular_wave_func(0,2,c.pi,0) 
# print ans

import scipy.constants as c
import numpy as np 

def radial_wave_func(n,l,r):
  a = c.physical_constants["Bohr radius"][0]
  na = n*a
  p1 = (2/na)**3
  p2 = fact(n-l-1)/(2*n*fact(n+l)**3.0)
  squarert_part = np.sqrt(p1*p2)
  lag_part = assocLaguerre(2*l+1,n-l-1)((2*r)/na)
  exponent = np.exp(-r/na)*((2*r/na)**l)
  return np.round((squarert_part*exponent*lag_part)/a**(-1.5),5)


# a=c.physical_constants['Bohr radius'][0] 
# print 'radial_wave_func(1,0,a)'
# ans=radial_wave_func(1,0,a) 
# print ans
# print 'radial_wave_func(1,0,a)' 
# ans=radial_wave_func(1,0,a) 
# print ans
# print 'radial_wave_func(2,1,a)' 
# ans=radial_wave_func(2,1,a) 
# print ans
# print 'radial_wave_func(2,1,2*a)' 
# ans=radial_wave_func(2,1,2*a) 
# print ans

# fvec=numpy.vectorize(f)
# xx,yy,zz=numpy.meshgrid(x,y,z)
# m=numpy.absolute(c)
#thankx git
def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
  a = c.physical_constants["Bohr radius"][0]
  plot = np.mgrid[-roa:roa:Nx*1j,-roa:roa:Ny*1j,-roa:roa:Nz*1j] #creates a 3D matrix containing all the points from -roa to roa, with the steps between each point determined by Nz,Ny or nx
  xx, yy, zz = [ np.swapaxes(plot[i],0,1) for i in xrange(3) ] #performs matrix transformations and transposes values for the axes
  rr, tt, pp = np.vectorize( cartesianToSpherical )( xx, yy, zz ) #passes all the arrays throug the cart to sphere func

  fullwave = angular_wave_func(m,l,tt,pp)*radial_wave_func(n,l,rr*a)

  mag = np.square( np.absolute( fullwave ) )  #psi square
  return np.round(xx,5), np.round(yy,5), np.round(zz,5), np.round(mag,5)


# print 'Test 1' 
# x,y,z,mag=hydrogen_wave_func(2,1,0,8,2,2,2) 
# print 'x, y, z:'
# print x, y, z
# print 'mag:'
# print mag
# print 'Test 2' 
# x,y,z,mag=hydrogen_wave_func(2,1,1,5,3,4,2) 
# print 'x, y, z:'
# print x, y, z
# print 'mag:'
# print mag
# print 'Test 3' 
# x,y,z,mag=hydrogen_wave_func(1,0,0,10,20,20,20) 
# print 'x, y, z:'
# print x, y, z
# print 'mag:'
# print mag


#Run pip install matplotlib
x,y,z,mag=hydrogen_wave_func(2,1, 0,10,20,20,20)

x.dump('xdata310.dat')
y.dump('ydata310.dat')
z.dump('zdata310.dat')
mag.dump('density310.dat')


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.load('xdata310.dat')
y = np.load('ydata310.dat')
z = np.load('zdata310.dat')
mag = np.load('density310.dat')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for a in range(0,len(mag)):
  for b in range(0,len(mag)):
    for c in range(0,len(mag)): 
      ax.scatter(x[a][b][c],y[a][b][c],z[a][b][c], marker='o', alpha=(mag[a][b][c]/np.amax(mag)))
plt.show()










