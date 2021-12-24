import os
c=1
file=[]
while True:
    print("\n\nEnter your modile model: ",end='')
    v = input()
    if v == '':
        continue

    if v in file:
         #print("\nyour model is "+v)
         continue # it will come out of the while loop
    else:
      #print("there is no other model of this type ...u can add to the database!!!")
      file.append(v)
      print("\n\tDatabase is updated!!")
      c=c+1
      if c==10:
          break


print("\n\nThe list of elements are: ")
for i in file:
    print(i)
