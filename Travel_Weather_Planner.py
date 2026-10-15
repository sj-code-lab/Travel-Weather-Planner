# Travel Weather Planner
distance_mi = 6 # Storing Integer in variable
is_raining = False # Storing Boolean in variable 
has_bike = True # Storing Boolean in variable
has_car = True # Storing Boolean in variable 
has_ride_share_app = True # Storing Boolean in variable

if not distance_mi: # Using an if statement to check if distance_mi variable is falsy
    print('False') # If variable is falsy output: False
elif distance_mi <=1 and not is_raining:# Using else if statement to check if distance_mi variable is 1 or less and it is not raining  
   print('True') # If both conditions amount to True output: True
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining: # Using else if statement to check if distance_mi variable is between 1 and 6 miles  
# and person has bike and it is not raining 
  print('True') # If all conditions amount to True output: True
elif distance_mi > 6 and (has_car or has_ride_share_app): # Using else if statement to check if distance_mi is greater than 6 miles and the person has_ car or has_ride_share_app 
    print('True') # If both conditions are satisfied output: True
else: 
    print('False') # If any condition returns False output: False