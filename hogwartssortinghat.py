# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:06:10 2020

@author: Admin
"""


print ('Welcome to Hogwarts, First years!')
print ('The sorting ceremony will take place after sometime')

gryffindor= 0
ravenclaw= 0
hufflepuff= 0
slytherin= 0

print ('How do you describe yourself?')
ans1= input('a.brave b.studious c.loyal d.ambitious:')

if ans1== 'a':
    gryffindor= gryffindor + 1
    
elif ans1== 'b':
    ravenclaw= ravenclaw + 1
    
elif ans1== 'c':
    hufflepuff= hufflepuff + 1
    
elif ans1== 'd':
    slytherin= slytherin + 1
    
else:
    print('Sorry, i did not understand you') 
    
print ('What can you be found doing on weekends?')
ans2= input('a. going on adventures b. doing your homework c. spending time with your family and friends d. plotting revenge on your enemies:')

if ans2== 'a':
    gryffindor= gryffindor + 1
    
elif ans2== 'b':
    ravenclaw= ravenclaw + 1
    
elif ans2== 'c':
    hufflepuff= hufflepuff + 1
    
elif ans2== 'd':
    slytherin= slytherin + 1
    
else:
    print('Sorry, I did not understand you') 
    
print('What would you do if the dark lord was about to invade your school?')
ans3= input('a. Fight him b. Look up some good defensive curses in a book c. Stand by my friends no matter what d. Help the Dark Lord invade the school as an inside spy:')
  
if ans3== 'a':
   gryffindor= gryffindor + 1 
elif ans3== 'b':
  ravenclaw= ravenclaw + 1
elif ans3== 'c':
  hufflepuff= hufflepuff + 1
elif ans3== 'd':
  slytherin= slytherin + 1
else:
    print("Sorry, I did not understand you")
    

print ('It is a Saturday night, you have finished your homework and you have some free time. You have decided to spend some time out of your common room. Where would you go?')
ans4= input('a. The room of requirement b. The library c. The kitchens d. The forbidden forest:')

if ans4== 'a':
   gryffindor= gryffindor + 1 
elif ans4== 'b':
  ravenclaw= ravenclaw + 1
elif ans4== 'c':
  hufflepuff= hufflepuff + 1
elif ans4== 'd':
  slytherin= slytherin + 1
else:
    print("Sorry, I did not understand you")
    
print('What would you see in the Mirror of Erised?')
ans5= input('a. Yourself, going on the adventure to defeat the dark lord b. Yourself, knowledgable above all c. Yourself, surrounded by your loving family and friends d. Yourself, surrounded by riches:')

if ans5== 'a':
   gryffindor= gryffindor + 1 
elif ans5== 'b':
  ravenclaw= ravenclaw + 1
elif ans5== 'c':
  hufflepuff= hufflepuff + 1
elif ans5== 'd':
  slytherin= slytherin + 1
else:
    print("Sorry, I did not understand you")
    
print('You are locked in a duel with a skilled opponent, He/She fires an unknown spell at you, and you shout....')
ans6= input('a. Expelliarmus b. Protego c. Stupefy d. Crucio: ')

if ans5== 'a':
   gryffindor= gryffindor + 1 
elif ans5== 'b':
  ravenclaw= ravenclaw + 1
elif ans5== 'c':
  hufflepuff= hufflepuff + 1
elif ans5== 'd':
  slytherin= slytherin + 1
else:
    print("Sorry, I did not understand you")

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print("GRYFFINDOR!!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
   print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print("SLYTHERIN!!!!!!")
else:
    print('Hmmm...too tricky to decide')
    