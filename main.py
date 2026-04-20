print("Hello World!")
name = str(input("Enter your name: "))
print(f"Hello {name}!, \nHow are you doing today?")
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:    print("You are a senior.")