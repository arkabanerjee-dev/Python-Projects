running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# the results might have more decimal digits than expected because numbers are stored in binary 
# and some decimal values cannot be converted exactly to  binary format 
# this leads to rounding errors
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)
# for 25%  tip
tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)
# as the nummber have many floating point digits, we can round the final bill to 2 decimal places
each_pays=round(final_bill,2)
print("Each person pays:",each_pays)

