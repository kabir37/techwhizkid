user1_age = int(input('what is your age:'))
user2_age = int(input('what is your age:'))
user3_age = int(input('what is your age:'))

if user1_age > user2_age and user3_age:
  print('user1 is the eldest')
elif user2_age > user3_age and user1_age:
  print('user2 is the eldest')
elif user3_age > user2_age and user1_age:
  print('user3 is the eldest')
else:
  print('invalid input')