from BMI.test_bmi import valid_input

print('\t\t\t BMI Calculator')
print('\n Hello, this is a BMI Calculator!')

height = float(input('Please enter your height input meters: '))
while valid_input(height) == False:
    height = float(input('Please enter your height input meters: '))

weight = int(input('Please enter your weight input kg: '))

valid_input(weight)

while valid_input(weight) == False:
    weight = int(input('Please enter your weight input kg: '))

bmi = weight/(height*height)

if bmi <= 18.5:
    print('Your BMI is', bmi, 'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
    print('Your BMI is', bmi, 'which means you are normal.')

elif bmi > 25 and bmi < 30:
    print('your BMI is', bmi, 'overweight.')

elif bmi > 30:
    print('Your BMI is', round(bmi, 2), 'which means you are obese.')

else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
          'and decimals were asked.')



input('\n\nPlease press enter to exit.')