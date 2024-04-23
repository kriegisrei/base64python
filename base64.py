import base64

choice = input("Would you like to encode or decode a base64 string? ").title()
answers = ["Encode", "Decode"]

if choice == "Encode":
    encode = input(str("Enter the string you want to encode: "))
    encodebytes = encode.encode("utf-8")
    encoded = base64.b64encode(encodebytes)
    print(encoded)
elif choice == "Decode":
    print("You want to decode")
else:
    if choice not in answers:
        print("I did not understand that")