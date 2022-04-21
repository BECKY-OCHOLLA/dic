#!/usr/bin/env python3.9
#person = {
#    'jina':'loise',
#    'age': 23,
#    'favorite_movie':'spiderman going home'
#}


from pydoc import doc


print('hi there...')

name = input('What\'s your name?\n\n')

age = input(f"Thanks for trusting me with that {name}... and how old are you?\n\n")

person = {
    'jina':'',
    'age': '',
    'favorite_movie':''
}

person['jina'] = {name}
person['age'] = {age}


favorite_movie = input("What movie would you re-watch a million times?\n\n")

print('Thats not a bad pick btw...\n\n')

email_address_que = input(f'Mind giving us your email address?\n\n')


person['favorite_movie'] = {favorite_movie}

if email_address_que == 'no' or email_address_que == 'No' or email_address_que == 'NO' :
    email_address = input(f"\n\nNice...What is it?\n\n")
        
else:
    print('Then what are you here for man?\n\n')

if email_address:
        
    docstring = input(f"""
          Mmmh {person['jina']}, are you really {person['age']} or you are just messing with us?
          Also we realized that you really like {person['favorite_movie']}.
          Is that true?
          """)
    if docstring == 'yes' or docstring == 'YES' or docstring == 'Yes' :
        print('You have good taste boy')
    else:
        print('bruuuuuuuh!!!!?? \nWhy would you even lie to a robot?\n\n')
else:
    print('get out!!\n\n')
    