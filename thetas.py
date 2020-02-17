# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression

"""
def suma(x,y,m,theta0,theta1):
    s=0
    for i in range(1,m):
        s+=(theta0+theta1*x[i-1]-y[i-1])**2
    return s

def J(theta0,theta1,m,s):
        j=m*(1/2)*s
    return j
"""

def Jderiv(x,y,m,theta0,theta1):
    s0=0
    s1=0
    jd=[]
    for i in range(0,m-1):
        s0+=(theta0+theta1*x[i]-y[i])
        s1+=(theta0+theta1*x[i]-y[i])*x[i]
    jd.append((1/m)*s0)
    jd.append((1/m)*s1)
    return jd

"""
def descXGrad0(theta0ini,theta1ini, x,y, alfa,m):
    for i in range(1,100):
        theta0=theta0ini-alfa*J(theta0ini,theta1ini,m,suma(x,y,m,theta0ini,theta1ini))
        theta0ini = theta0
    return theta0

def descXGrad1(theta0ini,theta1ini, x,y, alfa,m):
    for i in range(1,100):
        theta1=theta1ini-alfa*J(theta0ini,theta1ini,m,suma(x,y,m,theta0ini,theta1ini))
        theta1ini = theta1
    return theta1
"""

def descXGrad(theta0V,theta1V, x,y, alfa,m,tol):
    i=0
    thetas=[]
    while(i<=1000 and (theta0V>tol or theta1V>tol)):
        theta0Aux=theta0V-alfa*Jderiv(x,y,m,theta0V,theta1V)[0]
        theta1Aux=theta1V-alfa*Jderiv(x,y,m,theta0V,theta1V)[1]
        theta0V=theta0Aux
        theta1V=theta1Aux
        i=i+1
        
    thetas.append(theta0V)
    thetas.append(theta1V)
    return thetas

x=[60,62,61,55,53,60,63,58,52,48,49,43]
y=[23,23,25,25,26,26,29,30,30,32,33,31]

len(x)

thet=descXGrad(1,1,x,y,0.5,len(x),10**(-15))
print(thet)

reg = LinearRegression().fit(x,y)
help(LinearRegression())