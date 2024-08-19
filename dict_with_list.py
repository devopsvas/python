menus = { 'Breakfast': ['Egg S', 'Begal', 'Coffee'], 
           'Lunch': ['BLT', 'PB', 'TS'],
           'Soup':  ['Soup', 'Salad', 'Spaghetti', 'Taco']
         }

print('Breakfast:',  menus ['Breakfast'])


for m in menus:
    print(m)


for name, menu in menus.items():
    print (name, ':', menu )

