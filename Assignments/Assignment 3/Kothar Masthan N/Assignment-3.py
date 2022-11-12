#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


a=7
b=4
print(pow(7,4))


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[14]:


s = "Hi there Sam!"
my_list = s.split()
my_list[2] = 'dad!'


# In[15]:


s = "Hi there Sam!"
my_list = s.split()
my_list[2] = 'dad!'


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[10]:


planet = "Earth"
diameter = 12742

print('The diameter of {pla} is {dia} kilometers.'.format(pla=planet,dia=diameter))


# In[13]:


planet = "Earth"
diameter = 12742

print('The diameter of {pla} is {dia} kilometers.'.format(pla=planet,dia=diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[12]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2][0]


# In[11]:


lst[3][1][2][0]


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[16]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# In[17]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[ ]:


List is Mutable and Tuple is immutable.


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[19]:


def domainGet(strDomain): 
   return strDomain.split('@')[1]


# In[20]:


out = domainGet('user@domain.com')
print(out)


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[23]:


def findDog(st):
    print(st.lower())
    return 'dog' in st.split() 


# In[24]:


findDog('Is there a dog here?')
if('Is there s dod here'):
    print('True')
else:
    print(false)


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[25]:


def countDog(st):
    st.lower().split()
    return st.count('dog')


# In[26]:


countDog('This dog runs faster than the other dog dude!')


# ### Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[46]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        print('Big Ticket')
    elif speeding > 60:
        print('Small Ticket')
    else:
        print('No Ticket')
    
    
    
caught_speeding(81,True)
caught_speeding(91,False)


# In[ ]:





# In[ ]:





# Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. 

# In[6]:


emp_list=[24000,23500,23000,22500,22000]


for i in emp_list:
    print(i)
    
print(sum(emp_list))


# Create two dictionaries in Python:
# 
# First one to contain fields as Empid,  Empname,  Basicpay
# 
# Second dictionary to contain fields as DeptName,  DeptId.
# 
# Combine both dictionaries. 

# In[1]:


def Merge(dict_1,dict_2):
    return(dict_2.update(dict_1))

dict_1={'Empid':101,'Empname':'Pradeep','Basicpay':25000}
dict_2={'DeptName':'IT','Deptid':'1A2B'}
print(Merge(dict_1,dict_2))
print(dict_2)


# In[ ]:


