# Travel Weather Planner 🚴🚗🌦️

A Python project that determines whether commuting is possible based on distance, weather conditions, and available transportation. This project was built to satisfy a series of user stories and pass 24 automated tests.

---

## ✅ Steps Required (User Stories + Tests)

This project required implementing variables, conditional logic, and boolean operators to satisfy all user stories and pass all tests.

### **Variables Required**
You must create the following variables:

- `distance_mi` — number (miles to travel)
- `is_raining` — boolean
- `has_bike` — boolean
- `has_car` — boolean
- `has_ride_share_app` — boolean

---

### **Conditional Logic Requirements**

Using `if`, `elif`, and `else`, the program must:

#### 1. Falsy distance  
If `distance_mi` is a falsy value:  
**Print `False`**

#### 2. Distance ≤ 1 mile  
- Print `True` only if **not raining**  
- Otherwise print `False`

#### 3. Distance > 1 and ≤ 6 miles  
- Print `True` only if **has a bike AND not raining**  
- Otherwise print `False`

#### 4. Distance > 6 miles  
- Print `True` if **has a car OR has a ride‑share app**  
- Otherwise print `False`

---

### **Boolean Operator Requirement**
You must use at least one of:  
`and`, `or`, `not`

---

### **Tests Required**
Your program must pass all **24 tests**, covering:

- Variable existence  
- Correct variable types  
- Correct conditional structure  
- Correct boolean logic  
- Correct printed output for all scenarios  

---

## 🧠 Solution Code

```python
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

## Test Results
Passed: 1. You should have a variable named distance_mi.
Passed: 2. You should assign a number to your distance_mi variable.
Passed: 3. You should have a variable named is_raining.
Passed: 4. You should assign a boolean to your is_raining variable.
Passed: 5. You should have a variable named has_bike.
Passed: 6. You should assign a boolean to your has_bike variable.
Passed: 7. You should have a variable named has_car.
Passed: 8. You should assign a boolean to your has_car variable.
Passed: 9. You should have a variable named has_ride_share_app.
Passed: 10. You should assign a boolean to your has_ride_share_app variable.
Passed: 11. You should use at least one if statement.
Passed: 12. You should use at least one elif branch in your program.
Passed: 13. You should use at least one boolean operator (and, or, or not) in your code.
Passed: 14. You should use the print() function to display the result.
Passed: 15. When distance_mi is a falsy value, the program should print False.
Passed: 16. When the distance is 1 mile or less and it is not raining, the program should print True.
Passed: 17. When the distance is 1 mile or less and it is raining, the program should print False.
Passed: 18. When the distance is between 1 mile (excluded) and 6 miles (included), and it is raining with no bike, the program should print False.
Passed: 19. When the distance is between 1 mile (excluded) and 6 miles (included), it is not raining but no bike is available, the program should print False.
Passed: 20. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is not raining, the program should print True.
Passed: 21. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is raining, the program should print False.
Passed: 22. When the distance is greater than 6 miles and a ride share app is available, the program should print True.
Passed: 23. When the distance is greater than 6 miles and a car is available, the program should print True.
Passed: 24. When the distance is greater than 6 miles and neither a car nor a ride-share app is available, the program should print False.
