import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    if not filtered_users:
        print("No users found!")
    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]
    if not filtered_users:
        print("No users found!")

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    if not filtered_users:
        print("No users found!")
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = (
        input(
            "What would you like to filter by? (Currently 'name', 'age' and 'email' are supported): "
        )
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    if filter_option == "age":
        while True:
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                filter_users_by_age(age_to_search)
                break
            except ValueError:
                print("Please enter a number:")

    if filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()
            if "@" in email_to_search and email_to_search[-4:] == ".com":
                filter_users_by_email(email_to_search)
                break
            else:
                print("Please enter a valid email: ")


else:
    print("Filtering by that option is not yet supported.")
