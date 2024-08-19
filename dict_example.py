#! /ust/bin/python3 

acronyms = {'LOL': 'Laugh out loud',
            'IDK': 'I dont know',
            'TBH': 'to be honest'}


print (acronyms['LOL'])

#uopdate the key 

acronyms['TBH'] = 'honestly'


# Delete a key 

del acronyms['TBH']

print(acronyms)

defenition = acronyms.get('IDK')

if defenition:
    print(defenition)
else:
    print("Value does not exist")


sentence = 'IDK' + 'what happend' + 'TBH'

transilation = acronyms.get('IDK') + 'what happend' + acronyms.get('IDK')

print ('sentence:', sentence)
print ('transilation:', transilation)
