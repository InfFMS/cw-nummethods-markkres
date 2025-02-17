import matplotlib.pyplot as plt
import numpy as np

def f(v,t):
    return R*t/(v-b)-a/v**2
a=0.1382
b=3.19e-5
R=8.314
V_crit=3*b
T_crit=8*a/(27*R*b)
T_celsium=[-140,-130,-120,-110,-100]
T_kelvin=[T_celsium[i]+273.15 for i in range(len(T_celsium))]
V=np.linspace(b+10**-5,10**-3,1000)
V_left=V[V<=V_crit]
V_right=V[V>=V_crit]
Pokazatel=0
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
#L,R=5.9e-5,1.3e-4
#est=1e-8
#while R-L>est:
#    m1=L+(R-L)/3
#    m2=R-(R-L)/3
#    if f(m1,143.15)<f(m2,143.15):
#        R=m2
#    else:
#        L=m1
#x_min=(L+R)/2
#print(x_min)
plt.subplot(1,5,2)
#plt.scatter(x_min,f(x_min,143.15))
#print(f(x_min,143.15))

plt.plot([b+10**-5,0.001],[3664186.998,3664186.998],"black")

def f_perv(V):
    return f(V,143.15)-3664186.998
def equation(x):
    if f_perv(L)>f_perv(R):
        return -f_perv(x)
    else:
        return f_perv(x)
L=5.4e-5
R=7e-5
D=1e-7
while R-L>D:
    M=(R+L)/2
    if equation(M)>0:
        R=M
    elif equation(M)<0:
        L=M
print(M)

plt.show()
