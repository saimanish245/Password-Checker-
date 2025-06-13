import re 
def password_check(password):
  if len(password) < 8:
    return("password should have atleast 8 characters.")
  if not re.search(r'[A-Z]',password):
    return('Password should have atleast  one uppercase.')
  if not re.search(r'[a-z]',password):
    return('Password should have atleast  one lowercase.')
  if not re.search(r'[0-9]',password):
    return('Password should have atleast  one digit.')
  if not re.search(r'[@#$%!]',password):
    return('Password should have atleast  one special character.')
  else:
    return('Password is strong')
user_password = input("Enter password : ")   
banny=password_check(user_password)
print(banny)             