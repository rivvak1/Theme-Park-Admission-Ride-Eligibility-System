print("Welcome to our Python Adventure Park! c:")
print("We are going to help you set up your tickets.")
print("And pick which rides you'd like to go to.")

# questions -------------------

guest_name = input("What is your name?:")
age = int(input("What is your age?:"))
height = float(input("How tall are you? (inch):"))
ticket_type = input("Did you buy a regular or premium ticket?:")
park_member = input("Are you a park member? (yes/no):")
visiting_adult = input("Are you visiting with an adult? (yes/no):")
visit_time = input("Are you visiting in the morning or evening?:")
# printing --------------

print("Guest Name:", guest_name)
print("Age:", age)
print("Height:", height)
print("Ticket Type:", ticket_type)
print("Park Member Status:", park_member)




"""
Age   Price
0–4	  $0
5–12   $15
13–64 $30
65+	  $20
"""

# calculations ------------------

def calculate_admission(age):
    if age <= 4:
        return 0
    elif age >= 5 and age <= 12:
        return 15
    elif age >= 13 and age <= 64:
        return 30
    else:
        return 20

admission_price = calculate_admission(age)
print ("Admission Price Before Discount:", admission_price)



def calculate_discount(admission_price, park_member, visit_time):
    if visit_time == "evening" and park_member == "yes":
        return admission_price - 10
    elif visit_time == "evening":
        return admission_price - 3
    elif     park_member == "yes":
        return admission_price  - 5
    else:
        return admission_price - 0
after_discount = calculate_discount(admission_price, park_member, visit_time)

def below_zero(after_discount):
    if after_discount <= 0:
        return 0
    else:
        return after_discount

full_price = below_zero(after_discount)

print("Final Admission Price:", full_price)

def ride_level(age, height):
    if height >= 54 and age >= 16:
        return "Extreme Rides"
    elif height >= 48 and age >= 12:
            return "Thrill Rides"
    elif height >= 42 and age >= 8:
            return "Family Rides"
    elif height >= 36:
            return "Kiddie Rides"
    else:
        return "No Rides"

ride_access = ride_level(age, height)

print("Ride level:", ride_access)

def check_supervision(age , visiting_adult):
     if age < 13 and visiting_adult == "no":
        return "Adult Required"
     else:
          return "Approved"

adult_check = check_supervision(age , visiting_adult)

print("Supervision Status:", adult_check)

def check_premium(ticket_type):
     if ticket_type == "premium":
          return "PREMIUM BONUS (free snack and priority ride access!)"
     else:
          return "REGULAR TICKET"

premium_check = check_premium(ticket_type)

print("Premium Ticket Status:", premium_check)

print("Have a nice day at the park!")