num1 = int(input('enter number: '))
num2 = int(input('enter: z'))

if num1>num2:
    mn = num1
else:
    mn = num2

for i in range(1, mn+1):
    if(num1%i == 0 and num2%i == 0):
        hcf = i
print(f"The GCD is {hcf}")
product = num1*num2

lcm = product/hcf
print(f"The LCM is{lcm}")


