print("Enter your name:")
name = input()
print("Enter your age:")

age = int(input())

# if name == "Landry":
#     print("Hello Landry")

# elif name == "Alice":
#     print("What such a lovely name!, Alice")

# else :
#     print("You are not user, Please register!,", name)

if name == "Landry" and age > 30:
    print("Hello Landry, You are old enough to vote")

elif name == "Landry" and age < 30:
    print("Hello Landry, You are not old enough to vote")

else :
    print("Hello there!!!")