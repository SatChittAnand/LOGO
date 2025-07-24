name = input('Enter your name:- ')
age = int(input('Enter your age:'))
print(f"{name} you are just in age of {age}.")
if(age == 0):
    print("Oops! You are in your Mom's umb🫄")
elif(age > 0 and age <= 8 ):
    print("Oh!, No You are a cute little baby.")
elif(age >= 9 and age<=15):
    print('Arey!, you are a student🧑🏻‍🎓 now in school🏫.')
elif(age >= 18 and age<=59):
    print("You are eligible to vote👨🏻.")
elif(age>=60):
    print('You are old now, but you can vote.')
else:
    print("No, you are not eligible for voting.")

a = input("OKAY!, Thank You")