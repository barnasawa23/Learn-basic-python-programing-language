print("********************************")
print("***        WELCOME To        ***")
print("****       DOG STORE        ****")
print("********************************")

num_dogs = 23
num_cats = 12
num_birds = 21

total_of_animals = num_dogs + num_cats + num_birds

print("Please Enter your first name:")
fname = input()

print("Please Enter your last name:")
lname = input()

#concatenation

fullname = fname + " " + lname

print("Hello, ", fullname)

print("select the animal you want to buy:")
print("1.considering buying a dog")
print("2. comparing buying a cat")

request = int(input())

if request == 1:
    print("You have selected to buy a dog")
    print("We have", num_dogs, "dogs available")
    print("Total dogs remain are:", num_dogs)

elif request == 2:
    print("You have selected to buy a cat")
    print("We have", num_cats, "cats available")
    print("Total cats remain are:", num_cats)
    



print("We have actually number of:")
print("dogs:", num_dogs, "cats:", num_cats, "birds:", num_birds)
print("Therefor we have a total of:", total_of_animals, "animals.")




