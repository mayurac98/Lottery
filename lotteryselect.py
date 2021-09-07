import random
a=[]
n=int(input("Enter number of tickets"))
for i in range(5):
    a.append(random.randint(1000000,9999999))
print('Lottery numbers: ',a)

input("click to select a lottery number")
rand_lottery=random.choice(a)
print("Your lottery number is ",rand_lottery)
input("click next to check the lottery")
rand_select=random.choice(a)
if(rand_select == rand_lottery ):
    print("Congratulations!,You have won")
else:
    print("sorry try next time")