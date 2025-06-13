import re 
password = input("Enter password : ") 
if len(password) < 8:
    print("password should have atleast 8 characters.")
if not re.search(r'[A-Z]',password):
    print('Password should have atleast  one uppercase.')
if not re.search(r'[a-z]',password):
    print('Password should have atleast  one lowercase.')
if not re.search(r'[0-9]',password):
    print('Password should have atleast  one digit.')
if not re.search(r'[@#$%!]',password):
    print('Password should have atleast  one special character.')
else:
    print('Password is strong')