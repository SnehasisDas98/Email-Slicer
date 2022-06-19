email_address = input("Enter your email address: ")
string = email_address.split("@")
username = string[0]
domain_name = string[1]
print(f"Username: {username}")
print(f"Domain: {domain_name}")