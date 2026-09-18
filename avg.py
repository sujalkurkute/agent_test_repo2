def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


def find_user(users, username):
    for user in users:
        if user["name"] == username:
            return user

    return None


users = [
    {"name": "Sujal", "age": 21},
    {"name": "Rahul", "age": 22}
]

print(calculate_average([]))
print(find_user(users, "sujal"))