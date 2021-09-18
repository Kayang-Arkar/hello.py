#!/usr/bin/env python
# coding: utf-8

# # Donate Anonymously
# ### Description
# #### You can donate anonymously even admin team won't know who donate. Please do not write "Donation" in notes during transaction.
# #### Kpay: xxxxxxxxxxx
# #### Wave: xxxxxxxxxxx
# #### CB Pay : xxxx xxxx xxxx 

# In[ ]:


Amount = int (input("Amount: mmk"))
if Amount >= 500:
    print ("Our service is available.")
else:
    print ("Our service is not available.")


# ##### You can donate any amount
# ##### Our service starts at least from 500mmk.
# ##### Our service >> song or letter..... We will broadcast songs on every Sunday via Facebook and for letter, we will post on our Facebook page.
# ##### Write "song" or "letter" in small alphabets.

# In[ ]:


X = input ("song or letter: ")
print (X)
if X == "song":
   Y = input ("Singer: ")
   print (Y)
   Z = input ("Song: ")
   print (Z)
elif X == "letter":
   L = input ("You can write the letter here: ")
   print (L)
else:
    print ("please wether your alphabets are small or spelling mistake.")
   


# In[ ]:


I = input ("Any suggestion to 'Donate Anonymously'?: ")
print (I)

