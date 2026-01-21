records = [
    {"id": 1, "email": "user@example.com", "age": 25},
    {"id": 2, "email": "invalid_email", "age": 17},
    {"id": 3, "email": "test@mail.com", "age": None},
]

age_val = {i['id']:i['age'] // 2 for i in records if isinstance (i['age'], int) and i['age'] >= 18}
print(age_val)

email_val = {i['id']:i['email'] for i in records if isinstance(i["email"], str) and '@' in i["email"]}
print(email_val)

final_val = [{'id': i['id'], 'email': i['email'], 'age': i['age']} for i in records if (isinstance(i.get('age'), int) and i["age"] >= 18 and isinstance(i.get('email'), str) and '@' in i["email"])]
print(final_val)