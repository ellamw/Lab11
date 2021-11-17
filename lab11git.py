import json
from json.encoder import JSONEncoder

#           PART 1
list = [1121, "Jackie Grainger", 22.22, 
1122, "Jignesh Thrakkar", 25.25, 
1127, "Dion Green", 28.75, False, 
24.32, 1132, "Jacob Gerber", 
"Sarah Sanderson", 23.45, 1137, True, 
"Brandon Heck", 1138, 25.84, True, 
1152, "David Toma", 22.65, 
23.75, 1157, "Charles King", False, 
"Jackie Grainger", 1121, 22.22, False, 
22.65, 1152, "David Toma"]


#           PART 3
# first we will remove duplicates using list comprehension
list1 = []
[list1.append(x) for x in list if x not in list1]


# now we will remove bools
for i in list1:
    if type(i) == bool:
        list1.remove(i)


#           PART 2
# now we will start creating each dictionary
companyData = []
dictionary = {}
dictionary1 = {}
underpaidSalaries = []
companyRaises = []

for i in list1:
    # employee name
    if type(i) == str:
        dictionary['employeeName'] = i
    # employee info
    elif type(i) == int:
        dictionary['employeeInformation'] = i
    # employee hourly wage
    elif type(i) == float:
        dictionary['employeeHourlyWage'] = i
    
    if(len(dictionary)) == 3:
        

        #           PART 4
        dictionary['totalHourlyRate'] = dictionary['employeeHourlyWage'] * 1.3
        companyData.append(dictionary)
        

        #           PART 5
        if dictionary['totalHourlyRate'] >= 28.15:
            if dictionary['totalHourlyRate'] <= 30.65:
                underpaidSalaries.append(dictionary)
                
        
        #       PART 6
        if dictionary['employeeHourlyWage'] >= 22 and dictionary['employeeHourlyWage'] <= 24:
                dictionary1['employeeName'] = dictionary['employeeName']
                dictionary1['employeeHourlyWageAfterRaise'] = dictionary["employeeHourlyWage"] * 1.05
                dictionary1_copy = dictionary1.copy()
                companyRaises.append(dictionary1_copy)
        elif dictionary['employeeHourlyWage'] >= 24  and dictionary['employeeHourlyWage'] <= 26:
                dictionary1['employeeName'] = dictionary['employeeName']
                dictionary1['employeeHourlyWageAfterRaise'] = dictionary["employeeHourlyWage"] * 1.04
                dictionary1_copy = dictionary1.copy()
                companyRaises.append(dictionary1_copy)
        elif dictionary['employeeHourlyWage'] >= 26 and dictionary['employeeHourlyWage'] <= 28:
                dictionary1['employeeName'] = dictionary['employeeName']
                dictionary1['employeeHourlyWageAfterRaise'] = dictionary["employeeHourlyWage"] * 1.03
                dictionary1_copy = dictionary1.copy()
                companyRaises.append(dictionary1_copy)
        else:
            dictionary1['employeeName'] = dictionary['employeeName']
            dictionary1['employeeHourlyWageAfterRaise'] = dictionary["employeeHourlyWage"] * 1.02
            dictionary1_copy = dictionary1.copy()
            companyRaises.append(dictionary1_copy)


        dictionary = {}


#       PART 7
# list2 converted to json and printed out 
json_object = json.dumps(companyData, indent = 4)
print("\nThe companyData list is: \n", json_object)

json_object2 = json.dumps(underpaidSalaries, indent = 4)
print("\nThe underpaidSalaries list is: \n", json_object2)

json_object3 = json.dumps(companyRaises, indent = 4)
print("\nThe companyRaises list is: \n", json_object3)