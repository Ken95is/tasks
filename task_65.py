users = [
    {"email": "User@Example.com", "age": 20},
    {"email": "user@example.com", "age": 22},
    {"email": "admin@test.com", "age": 30},
    {"email": "ADMIN@test.com", "age": 25},
]


result = {}
for user in users:
    email = user['email'].lower()
    print(email)
    age = user['age']
    print(age)

    if email not in result or age > result[email]['age']: # result[email] подставляет значение переменной email
        result[email] = {"email": email, "age": age}

unique_users = list(result.values())
print(unique_users)
# print(result)
