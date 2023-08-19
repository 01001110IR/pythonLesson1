import json
import datetime
import os 

def display_current_time():
    current_time = datetime.datetime.now()
    print("The time is:", current_time)

def get_user_names():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    return {
        "first name": first_name,
        "last name": last_name
    }

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
    display_current_time()

    # Read existing data from JSON file
    with open("db.json", "r") as json_file:
        data = json.load(json_file)

    user_dict = get_user_names()

    # Generate a new ID for the user
    new_id = max(user["id"] for user in data["users"]) + 1

    new_user = {
        "id": new_id,
        "first name": user_dict["first name"],
        "last name": user_dict["last name"]
    }

    data["users"].append(new_user)

    print("The dictionary is updated:", data)

    # Write updated data back to JSON file
    with open("db.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    # Print the entire updated JSON data
    print("Data from JSON file:", data)
