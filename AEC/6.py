import re
def pass_criteria(password):
    if len(password)<8:
       print("the password is too short");
    else:
       has_lowercase=any(char.islower() for char in password)
       has_uppercase=any(char.isupper() for char in password)
       has_digit=any(char.isdigit() for char in password)
       has_special=any(char in "#$@!%^&*)(_+{}:><?~" for char in password)
       complexity=sum(has_lowercase,has_uppercase,has_digit,has_special)
       if complexity<3:
           print("the password is not complex")
       else:
           common=[r'123',r'111',r'pass',r'admin']
           for pattern in common:
                if pattern in password:
                    print("the password is common")
                else:
                    print("the password meets the criteria");
if __name__=="__main__":
   password=input("enter the password")
   pass_criteria(password)
