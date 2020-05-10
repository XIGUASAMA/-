#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


f=open("input.txt", "r", encoding="utf-8-sig")
str_f=f.read()
f.close()
text=[]
text=str_f.split("\n\n")
text[1] = text[1].replace("\n","")
print(text)


# In[3]:


exec(text[0])
exec(text[1])
print(V)
print(C)


# In[4]:


net_dict={}
for i in range(0,len(C)):
    for j in range(0,len(C[i])):
        if C[i][j]>0:
            net_dict[(V[i],V[j])] = [C[i][j],0]
print(net_dict)


# In[5]:


while(1):
    Tab_dict={}
    for i in range(0,len(V)):
        Tab_dict[V[i]] = [0,0]
    Tab_dict['vs'][0] = '-'
    Tab_dict['vs'][1] = float("inf")
    print(Tab_dict)
    m = -1
    temp_vt=[0,0]
    for i in V:
        m += 1
        n = -1
        for j in V:
            n += 1
            #print(i,j,m,n)
            if (i,j) in list(net_dict.keys()) and j == V[-1]:
                if min(Tab_dict[i][1],net_dict[(i,j)][0] - net_dict[(i,j)][1]) > temp_vt[1]:
                    temp_vt[0] = V[m] + "+"
                    temp_vt[1] = min(Tab_dict[i][1],net_dict[(i,j)][0] - net_dict[(i,j)][1])
            elif (i,j) in list(net_dict.keys()) and net_dict[(i,j)][0] > net_dict[(i,j)][1] and Tab_dict[j][1] == 0 and m < n:
                Tab_dict[j][0] = V[m] + "+"
                Tab_dict[j][1] = min(Tab_dict[i][1],net_dict[(i,j)][0] - net_dict[(i,j)][1])
                print(i,j,Tab_dict[i][1],net_dict[(i,j)][0],net_dict[(i,j)][1],Tab_dict[j][1])
            elif (i,j) in list(net_dict.keys()) and net_dict[(i,j)][1] > 0 and Tab_dict[i][1] == 0 and m > n:
                Tab_dict[i][0] = V[n] + "-"
                Tab_dict[i][1] = min(Tab_dict[j][1],net_dict[(i,j)][1])
    Tab_dict['vt'] = temp_vt
    print(Tab_dict)
    theta = Tab_dict['vt'][1]
    
    if Tab_dict['vt'] == [0,0]:
        print(net_dict)
        print(Tab_dict)
        break

    j = 'vt'
    while(1):
        i = Tab_dict[j][0][0:-1]
        if Tab_dict[j][0][-1] == '+':
            net_dict[(i,j)][1] += theta
        elif Tab_dict[j][0][-1] == '-':
            net_dict[(j,i)][1] -= theta
        j = i
        if(j == 'vs'):
            break
    print(net_dict)
    print("*******************************************************************************")


# In[6]:


f=open("output.txt", "w", encoding="utf-8")
f.truncate()
f.write("求解完成！\n该网络的最小割：")
IN = []
for i in V:
    if (Tab_dict[i])[1] != 0:
        IN.append(i)
print(IN)

summ = 0
f.write("{")
for i in range(0,len(V)):
    for j in range(0,len(V)):
        #print(V[i],V[j])
        if V[i] in IN and V[j] not in IN and i < j and (V[i],V[j]) in list(net_dict.keys()):
            print((V[i],V[j]))
            f.write("(" + str(V[i]) + "," + str(V[j]) + ")")
            summ += net_dict[(V[i],V[j])][1]
f.write("}" + "\n")

print(summ)
f.write("该网络的最大流流量和最小割容量：" + str(summ))
f.close()

