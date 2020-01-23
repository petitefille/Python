
# coding: utf-8

# # Solutions to Worksheet 1 Exercises

# Exercise 1. Write a code that produces two input boxes, asking for your name and age in turn. Print the output in the form "Hello .... You're ... years old."

# In[ ]:


Name = input("Enter your name ")
age = input("Now enter your age ")
print("Hello " + Name + ". You are " + age + " years old.")


# Exercise 2. Write two functions for converting temperature between degrees Fahrenheit and degrees Celsius (and vice versa).

# In[ ]:


def FtoC(f):
    return (1 / 1.8) * (f - 32)

def CtoF(c):
    return 1.8 * c + 32

print(FtoC(1))
print(CtoF(1))


# Exercise 3. Write a program that reads in a string and determines whether it is a palindrome.

# In[ ]:


def isPalindrome(s):
    return s == s[::-1]
text = input()
print(isPalindrome(text))


# Exercise 4. Define a function rotateR with one argument (a string) that returns the string rotated to the right. E.g. `rotateR("Thor")` should return `"rTho"`. 

# In[ ]:


def rotateR(s):
    return s[-1:]+s[:-1]
print(rotateR("Thor"))
print(rotateR(list("Thor")))


# Exercise 5. Define a function rotateL with one argument (a list) that returns the list rotated to the left. E.g. rotateL([1,2,3,4]) should return [2, 3, 4, 1].

# In[ ]:


def rotateL(l):
    return l[1:]+l[:1]
rotateL([1,2,3,4])


# Exercise 6. Do both functions work for lists and strings? If not, how can you fix that?

#     Yes, because we only used slicing.

# Exercise 7. Define a function rotateRx that gets a list as a parameter and changes that list by rotating it to the right. The function should return nothing.

# In[ ]:


def rotateRx(l):
    l[:1],l[1:] = l[-1:],l[:-1]

l = [1,2,3,4]
rotateRx(l)
print(l)


# Exercise 8. Can you modify the previous exercise so that it works for strings?

#     No, because strings cannot be modified.

# Exercise 9. Write a function `rotateR2` that gets a string as an argument and returns the string rotated to the right twice, using only the function `rotateR` defined earlier.

# In[ ]:


def rotateR2(s):
    return rotateR(rotateR(s))
rotateR2("Thor")


# Exercise 10. Write a function rotateRx2 that changes its parameter (a list) by rotating it twice to the right. The function should only use the defined rotateRx.

# In[ ]:


def rotateR2x(l):
    rotateRx(l)
    rotateRx(l)
l = [1,2,3,4]
rotateR2x(l)
l


# Exercise 11. Create a list `l` that prints as `[[1, 2, 3], [1, 2, 3]]` but when we rotate only the second part (i.e. by calling `rotateRx(l[1])`), it should return `[[3, 1, 2], [3, 1, 2]]`, i.e. both parts should be rotated.

# In[ ]:


l=[[1,2,3],[1,2,3]]
rotateRx(l[1])
print(l)


# This only changes the second list! Why?

# Let's see first how `l` actually looks like:

# ![](wrongList-before1.png "")

# When we apply `rotateRx(l[1])`, it will access the second list (`l[1]`) and that will be the parameter of `rotateRx`. So, at the end, it will look like ![](wrongList-updated.png "")

# In[ ]:


lx = [1,2,3]


# ![](goodList-1.png "")

# We can create a list `l` which points 'twice' to the same list `lx`:

# In[ ]:


l = [lx,lx]


# ![](goodList-2.png "")

# In[ ]:


rotateRx(l[1])
print(l)


# ![](goodList-3.png "")

# Exercise 12. Note that we called this 'myString', but actually this is a **LIST**!!! 

# In[ ]:


myString = [["1","a"],0,[""]]
print(myString[0][0][0])
print(myString[0][1]+myString[2][0])
print(myString[0:1]+myString[1:2])
print(myString[int(myString[0][0])])

