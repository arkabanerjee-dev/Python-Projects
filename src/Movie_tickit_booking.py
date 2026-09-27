base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)
#  user is eligible to book a ticket if they are 21 or older,
#  or if they are 18 or older and either the show time is not 'Evening'
#  or they are a member
# and has a higher precedence than or. 
# This means conditions joined with 'and' are grouped together,
#  as if they were wrapped in parentheses. 
# WE can use parentheses () to change how conditions are grouped.
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    # here the show_time and is_member are one condition
    # if one of them is true, the whole condition will be true 
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price=(base_price + extra_charges + service_charges)-discount
    print("Final price of ticket:",final_price)
else:
    print('Ticket booking failed due to restrictions')