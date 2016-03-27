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

# def legendre(l):
#   f = np.poly1d([1,0,-1])**l
#   return (1/float(2**l)*fact(l))*(n_derive(l,f))*f
#mnew thing learned, closures.
def assocLegendre(m,l):
  derivative = np.polyder(legendre(l),m) #this part is executed only when f(x) is called
  def eqn_1(theta):
    x = np.cos(theta)
    return ((1-x*x)**(np.absolute(m)/2.0))*derivative(x) # x is passed into the derivative and resolved
  return eqn_1


# print 'f=assocLegendre(0,0)' 
# print 'f(1)' 
# f=assocLegendre(0,0) 
# ans=f(1)
# print ans

# print 'f=assocLegendre(1,1)' 
# print 'f(1)' 
# f=assocLegendre(1,1) 
# ans=f(1)
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

from scipy.special import laguerre
def assocLaguerre(p,qmp):
  der = np.polyder(laguerre(p+qmp, True), p )
  return ((-1)**p)*der if qmp else der

print 'f=assocLaguerre(0,0)' 
print 'f(1)' 
f=assocLaguerre(0,0) 
ans=f(1)
print ans
print 'f=assocLaguerre(1,1)' 
print 'f(1)' 
f=assocLaguerre(1,1) 
ans=f(1)
print ans
print 'f=assocLaguerre(2,2)' 
print 'f(1)' 
f=assocLaguerre(2,2) 
ans=f(1)
print ans
print 'f=assocLaguerre(2,2)' 
print 'f(0)' 
f=assocLaguerre(2,2) 
ans=f(0)
print ans


































