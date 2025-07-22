

# Lesson 10: Solution

contact = {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "phone": "123-456-7890"
}

print("Email:", contact["email"])

contact["address"] = "123 Main St, Anytown, USA"
print("Contact after adding address:", contact)

contact["phone"] = "987-654-3210"
print("Contact after changing phone:", contact)

print("\nContact Details:")
for key, value in contact.items():
    print(f"{key.title()}: {value}")

