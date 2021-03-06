#!/usr/bin/env python
# coding: utf-8

# In[207]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import os


# In[208]:


d={
    'age':pd.Series(['youth','youth','middle','senior','senior','senior','middle','youth','youth','senior','youth','middle','middle','senior']),
    'income':pd.Series(['high','high','high','medium','low','low','low','medium','low','medium','medium','medium','high','medium']),              
    'student':pd.Series(['no','no','no','no','yes','yes','yes','no','yes','yes','yes','no','yes','no']),
    'credit rating':pd.Series(['fair','excellent','fair','fair','fair','excellent','excellent','fair','fair','fair','excellent','excellent','fair','excellent']),
    'buys computer':pd.Series(['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no'])
}


# creating a datafrme using pandas
table=pd.DataFrame(d)

# seperating each class attribute
age=table['age']
income=table['income']
student=table['student']
credit=table['credit rating']
buysComputer=table['buys computer']


# In[212]:


table


# In[209]:


# Function to count Distinct Values and no. of time they occur in  class label attribute
def countDistinct(data):        
    distinct=list(data.unique())    
    data=list(data)
    dicts=dict()
    for i in distinct:
        dicts[i]=data.count(i)
    return dicts


# In[210]:


ageCount=countDistinct(age)
incomeCount=countDistinct(income)
studentCount=countDistinct(student)
creditCount=countDistinct(credit)
buysComputerCount=countDistinct(buysComputer)


# In[213]:


print("Age Count:",ageCount)
print("Income Count:",incomeCount)
print("Student Count:",studentCount)
print("Credit Count:",creditCount)
print("Buys Count:",buysComputerCount,"\n\n")


# In[214]:


# Finding probabily for Buys computer=Yes and Buys Computer=No
# p(c1) and p(c2),  c1=buys computer:yes, c2=buys computer:no

# strong all the Yes from table into a list
list_of_yes=set(table.index[ table['buys computer'] == 'yes'].tolist())

# getting number of Yes from the list using len(list)
number_of_yes=len(list_of_yes)


# strong all the No from table into a list
list_of_no=set((table.index[ table['buys computer'] == 'no'].tolist()))

# getting number of No from the list using len(list)
number_of_no=len(list_of_no)


ProbYes=number_of_yes/(number_of_yes+number_of_no)
ProbNo=number_of_no/(number_of_yes+number_of_no)


print("Probability of Buy Computer, yes: ", ProbYes)
print("Probability of Buy Computer, No: ", ProbNo,"\n")


# In[215]:


printYes={}
printNo={}
# function to compute required condidtional probabilities
def findProbXi(data,param,dicts):
    findyes=set(table.index[ table[data] == param].tolist())
    yes=len(findyes.intersection(list_of_yes))
    no=(dicts[param])-yes
    printYes[str(data)+"= "+str(param)+" | Buys Computer=Yes"]=yes/number_of_yes
    printNo[str(data)+"= "+str(param)+" | Buys Computer=No"]=no/number_of_no
    return yes/number_of_yes,no/number_of_no


# In[216]:


ageWhenYes,ageWhenNo=findProbXi('age','youth',ageCount)
incomeWhenYes,incomeWhenNo=findProbXi('income','medium',incomeCount)
studentWhenYes,studentWhenNo=findProbXi('student','yes',studentCount)
creditWhenYes,creditWhenNo=findProbXi('credit rating','fair',creditCount)


for key in printYes:
    print("p(",key,")","= %.5f"%printYes.get(key))
    
print("\n\n")    

for key in printNo:
    print("p(",key,")","= %.5f"%printNo.get(key))


# In[217]:



probYesWhenX=ageWhenYes*incomeWhenYes*studentWhenYes*creditWhenYes*ProbYes
print("\n\nc1=Buys Computer : Yes")
print("P(C1/X): %.5f" %probYesWhenX,"\n\n")

probNoWhenX=ageWhenNo*incomeWhenNo*studentWhenNo*creditWhenNo*ProbNo
print("c2=Buys Computer : NO")
print("P(C2/X): %.5f\n\n"%probNoWhenX)

print("Resulting Probabilty Whether Buying = Yes or NO")
print("yes :%.5f"%probYesWhenX if probYesWhenX > probNoWhenX else "No :%.5f"%probNoWhenX)

