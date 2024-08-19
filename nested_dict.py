contacts = {
    'number': 4,
    'students': 
    [
        {'name': 'Vasanth T M', 'email':'v@example.com'},
        {'name': 'test user', 'email': 'test@example.com'},
        {'name': 'dummy user', 'email': 'dummy@example.com'},
        {'name': 'ron user', 'email': 'ron@example.com'}
    ]
}


for student in contacts['students']:
    print(student['email'])
