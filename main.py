"""Hi Tre, this is the code that I have gotten stuck on.
The instructions are to move through 3 levels of if statements and have the machine produce an output.
my issue is that it won't produce the print statements of the (photo_request) and it won't add the $3 to
the (total_bill). My gut tells me that the (photo_request) doesn't need to live under each
if statement... But I'm struggling. So without giving me the answer, how can I think about
this differently? """

# I wonder what happens when I do something
# I will figure out how this works
# When i type here it auto-updates on github desktop... i think
# so i think the process is, commit, then push. Let's try from PyCharm, now.

#Code below:

# check height - need 120cm or more
# Check age - ($12-18 or over), ($7 [12-18]), ($5-12 or under)
# photo request - if yes, add $3 to total bill

height = int(input("How tall are you in cm?: "))
total_bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you?: "))
    if age >= 18:
        print("The cost is $12")
        total_bill += 12
        if age:
            photo_request = str(input("Do you want photos?: "))
            if photo_request.upper() == 'yes':
                total_bill += 3
                print("That will be $3 extra.")
                print(f"Your total cost is ${total_bill}")
    elif age > 12:
        print("The cost is $7")
        total_bill += 7
        if age:
            photo_request = str(input("Do you want photos?: "))
            if photo_request.upper() == 'yes':
                total_bill += 3
                print("That will be $3 extra.")
                print(f"Your total cost is ${total_bill}")
    else:
        print("The cost is $5")
        total_bill += 5
        if age:
            photo_request = str(input("Do you want photos?: "))
            if photo_request.upper() == 'yes':
                total_bill += 3
                print("That will be $3 extra.")
                print(f"Your total cost is ${total_bill}")
            else:
                print(f"Ok, you owe ${total_bill}")
else:
    print("You are not tall enough to ride the roller coaster.")
    print(f"{total_bill}", "is what you owe.")


