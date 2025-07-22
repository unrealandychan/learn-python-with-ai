
# Lesson 34: Solution

import json

user_profile = {
    "id": 123,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "is_active": True,
    "roles": ["user", "admin"]
}

json_string = json.dumps(user_profile, indent=4)
print("JSON String:")
print(json_string)

new_dict = json.loads(json_string)
print("\nEmail from new dictionary:", new_dict["email"])

