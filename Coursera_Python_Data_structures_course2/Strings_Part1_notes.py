# Looking inside Strings

# b a n a n a
# 0 1 2 3 4 5

'''fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x -1]
print(w)

print(len(fruit))'''

# 2nd example

# using fruit as variable -- here we're using an indefinite loop
'''fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit [index]
    print(index, letter)
    index = index + 1'''

# using a definite loop and the same variable fruit = 'banana'
'''fruit = 'banana'
for letter in fruit:
    print(letter)
# the iteration variable here it is 'letter', it iterates through the string 'banana' and the block/body - here is print(letter)/whatever
#  is under the for loop -
# of code is executed once for each value in the sequence.

    

# LOOPING AND COUNTING

word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count + 1
print(count)'''

# SLICING STRINGS

# Monty Python
# 01234567891011

s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20]) # it is ok to have the second number beyond of the end of the string. it stops at the end, here it stops at 11.




