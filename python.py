import random

random_num = random.randint(1, 5)
while True:
   num = int(input("INPUT NUMBER 1-5 : "))
   if num != random_num:
       print("Try more ;)")
       continue
   print("u the KING11!", random_num)
   break
