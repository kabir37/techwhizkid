
print("Select operation.")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. quit")

choice = input("Enter choice(1/2/3/4/5): ")

if(choice == '5'):
	print("BYE")
else:
	while (True):
		if choice in ('1', '2', '3', '4', '5'):
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))

			if choice == '1':
				print(num1+num2)
			elif choice == '2':
				print(num1-num2)
			elif choice == '3':
				print(num1*num2)
			elif choice == '4':
				print(num1/num2)
			else:
				print("Invalid Input")