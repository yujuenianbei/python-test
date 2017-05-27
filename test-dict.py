people = {
    'Alice':{
        'phone':'123',
        'addr':'mun1'
    },
    'Ben':{
        'phone':'456',
        'addr':'mun2'
    },
    'Cel':{
        'phone':'789',
        'addr':'mun3'
    }
}
labels = {
    'phone':'phoneNumber',
    'addr':'address'
}
name = input('Name:')
request = input('Phone number(p) or address(a)?')

if request == 'p':key = 'phone'
if request == 'a':key = 'addr'
 
if name in people :print ("%s's %s is %s." %(name,labels[key],people[name][key]))