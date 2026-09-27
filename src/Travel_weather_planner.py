distance_mi=5
is_raining=True # is Raining
has_bike=False # no Bike
has_car=True  # has car
has_ride_share_app= False #no ride share app 

if bool(distance_mi):
    # for truthy values of distance_mi
    if distance_mi <= 1 :
        if not(is_raining):
            print("True")
        else:
            print("False")

    elif (distance_mi>1 and distance_mi <=6):

      #   ONLY GO IF NOT RAINING AND BIKE IS PRESENT
          if not(is_raining) and has_bike:
              print("True")
          else:
              print("False")
    else:
        if has_ride_share_app or has_car:
            print("True")
        else :
            print("False")
else:
    # in case distance has falsy values 
    print("False")
