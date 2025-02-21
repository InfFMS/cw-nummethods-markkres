import matplotlib.pyplot as plt
import numpy as np

def f(v,t):
    return R_for_GAS*t/(v-b)-a/v**2
def l(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

#константы
a=0.1382
b=3.19e-5
R_for_GAS=8.314
V_crit=3*b
T_crit=8*a/(27*R_for_GAS*b)
T_celsium=[-140,-130,-120,-110,-100]
T_kelvin=[T_celsium[i]+273.15 for i in range(len(T_celsium))]
V=np.linspace(b+10**-5,10**-3,1000)
V_left=V[V<=V_crit]
V_right=V[V>=V_crit]
Pokazatel=0
#графики
for j in range(len(T_kelvin)):
    if T_kelvin[j]<=T_crit:
        P_left=f(V_left,T_kelvin[j])
        P_right=f(V_right,T_kelvin[j])
        plt.subplot(1,5,j+1)
        plt.plot(V_left,P_left,'blue')
        plt.plot(V_right,P_right,'blue')
    else:
        if Pokazatel==0:
            P_left=f(V_left,T_kelvin[j])
            P_right=f(V_right,T_kelvin[j])
            plt.subplot(1,5,j+1)
            plt.plot(V_left,P_left,'red')
            plt.plot(V_right,P_right,'red')
            Pokazatel=1
        else:
            P_left=f(V_left,T_kelvin[j])
            P_right=f(V_right,T_kelvin[j])
            plt.subplot(1,5,j+1)
            plt.plot(V_left,P_left,'blue')
            plt.plot(V_right,P_right,'blue')

#минимум            
L,R=5.9e-5,1.3e-4
est=1e-8
while R-L>est:
    m1=L+(R-L)/3
    m2=R-(R-L)/3
    if f(m1,143.15)<f(m2,143.15):
        R=m2
    else:
        L=m1
x_min=(L+R)/2
#точка минимума на графике
plt.subplot(1,5,2)
plt.scatter(x_min,f(x_min,143.15))
print("минимум: ",x_min,f(x_min,143.15))
#максимум
L,R=1.3e-4,10**-3
est=1e-8
while R-L>est:
    m1=L+(R-L)/3
    m2=R-(R-L)/3
    if f(m1,143.15)>f(m2,143.15):
        R=m2
    else:
        L=m1
x_max=(R+L)/2
#точка максимума на графике
plt.scatter(x_max,f(x_max,143.15))
print("максимум: ",x_max, f(x_max,143.15))

#Длина кривой
i=x_min
length=0
while i<x_max+10e-8:
    length+=l(i,f(i,143.15),i+10e-8,f(i+10e-8,143.15))
    i+=10e-8
print("длина кривой запрещенной зоны ",length)

#прямая для нахождения корней уравнения
plt.plot([b+10**-5,0.001],[3664186.998,3664186.998],"black")

#корни уравнения
def f_perv(V):
    return f(V,143.15)-3664186.998
def equation(x):
    if f_perv(L)>f_perv(R):
        return -f_perv(x)
    else:
        return f_perv(x)
#первый корень
L=5.4e-5
R=7e-5
D=1e-7
while R-L>D:
    M=(R+L)/2
    if equation(M)>0:
        R=M
    elif equation(M)<0:
        L=M
V1=M
#второй корень
L=7e-5
R=1e-4
D=1e-7
while R-L>D:
    M=(R+L)/2
    if equation(M)>0:
        R=M
    elif equation(M)<0:
        L=M
V2=M

#третий корень
L=1e-4
R=3e-4
D=1e-7
while R-L>D:
    M=(R+L)/2
    if equation(M)>0:
        R=M
    elif equation(M)<0:
        L=M
V3=M
plt.scatter(V1,f(V1,143.15))
plt.scatter(V2,f(V2,143.15))
plt.scatter(V3,f(V3,143.15))
print("корни: ",V1,V2,V3)

#интегралы
i=V1
S1=0
while i<V3+10e-8:
    S1+=(10e-8)*(f(i,143.15)+f(i+10e-8,143.15))/2
    i+=10e-8
S2=0
i=V1
while i<V3+10e-8:
    S2+=(10e-8)*3664186.998
    i+=10e-8
print('интеграл 1: ', S1)
print("интеграл 2: ", S2)

plt.show()
