#       AGE         #
age = input('input your age: ')  # input
if int(age) >= 16:  # validate the condition, and also change the age input from a string to an integer
    print("okay go ahead")  # do this
else:  # if the condition doesn't meet the terms
    print("you're younger than 16")  # do this

#       HEIGHT      #
height = input('your height in meters : ')
if float(height) <= 1:  # validate the con
    print('you can not ride, under 1m')  # if it meets the term do this
elif float(height) >= 4:  # if the first term is false do this
    print('you can not ride, over 4m')
elif float(height) >= 3 <= 4:  # another term if last 2 terms are false
    print('wow you are tall')
else:  # if the con don's meet any of the terms do this
    print('you can ride')
