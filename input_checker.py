user_input1= input('enter a number or a word or sentence:')
user_input2= input('enter another number or a word or sentence:')

print("\n")
try:
	val_1= int(user_input1)
	val_2= int(user_input2)
	ans = (val_1+val_2)
	print("Addition of Int:",ans)
except ValueError:
	try:
		val_1= float(user_input1)
		val_2= float(user_input2)
		ans = (val_1+val_2)
		print("Addition of float:",ans)
	except ValueError:
		ans = (user_input1 + user_input2)
		print("Concatenated inputs:", ans)