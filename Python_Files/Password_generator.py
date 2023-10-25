import secrets
import string


pass_length = input("What length password would you like? ")

random_token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(int(pass_length)))
print(random_token)


output = random_token

file_path = "passes.txt"

with open(file_path, 'w') as file:
    file.write("-" + output)

print("Token written to file")
