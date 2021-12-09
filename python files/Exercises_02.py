#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[3]:


z1 = np.zeros(10)
z1


# #### Create an array of 10 ones

# In[4]:


a1 = np.ones(10)
a1


# #### Create an array of 10 fives

# In[5]:


a5 = 5*a1
a5


# #### Create an array of the integers from 10 to 50

# In[11]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[13]:


np.arange(10,52,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[15]:


a8 = np.arange(0,9)
a8.reshape(3,3)


# #### Create a 3x3 identity matrix

# In[16]:


np.identity(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[23]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[26]:


np.random.standard_normal(size=(1,25))


# #### Create the following matrix:

# In[36]:


a100 = np.linspace(0.01,1,100)
a100.reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[37]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[39]:


a25 = np.arange(1,26).reshape(5,5)
a25


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[63]:


a25[2:5,1:5]


# In[55]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[71]:


a25[3][4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[76]:


a25[0:3,1:2]


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[77]:


a25[4][0:]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[84]:


a25[3:5,0:5]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[85]:


a25.sum()


# #### Get the standard deviation of the values in mat

# In[86]:


a25.std()


# #### Get the sum of all the columns in mat

# In[89]:


a25.sum(axis=0)


# # Great Job!
