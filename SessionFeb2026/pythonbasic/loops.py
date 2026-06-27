# while loop

'''
count = 0

while count < 5:
    print("Count:", count)
    count += 1

numbers = (34,54,67,21,78,97,45,44,80,19)
for n in numbers:
    if n == 21:
        print("Found 21, breaking the loop.")
        break
    print("Number:", n)

# loops code for loops.py
'''

for letter in 'Python':
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
print ("Good bye!")


'''
for count in range(6):
   print ("Iteration no. {}".format(count))
   if count == 3:
       print ("Breaking the loop at iteration no. {}".format(count))
       break
else:
   print ("for loop over. Now in else block")
print ("End of for loop")
'''
'''
# for loop
for i in range(5):
    print("Iteration:", i)  

    # for interation variable in [0,1,2,3,4]:
    #     statement

for i in [1,2,3,4,5]:
    print("Iteration:", i)


for char in "Hello":
    print("Character:", char)

numbers = (34,54,67,21,78,97,45,44,80,19)
for n in numbers:
    print("Number:", n)

print()

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
  print (x,":",numbers[x])
'''