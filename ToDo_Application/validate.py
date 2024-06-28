
import re
email=input("enter email id of a user")
phone_number=input("enter phone number of a user")
email_pattern=r"^[a-zA-Z0-9_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
phone_number_pattern=r"^\d{10}$"
if re.match(email_pattern,email):
    print("input email is valid")
else:
    print("input email id is not valid")
if re.match(phone_number_pattern,phone_number):
    print("input phone number is valid")
else:
    print("input phone nubmer is not valid")