from timeit import repeat
from xml.dom import UserDataHandler
import datetime

# Pulane Tladi

def user_details():
    """
    Prompt user input
    """
    #print("Welcome to the username Generator!")

    # Validating if the first and last name does not contain digits
    first_name = input("Insert your first name: \n").lower()
    while not first_name.isalpha():
        print("Invalid first name")
        first_name = input("Insert your first name: \n")

    last_name = input("Insert your last name: \n").lower()
    while not last_name.isalpha():
        print("Invalid first name")
        first_name = input("Insert your last name: ")

    # validating if the year entered is correct
    cohort = int(input("Insert your cohort: \n"))
    while cohort < datetime.datetime.now().year:
        print("Cohort year can't be in the past")
        cohort = int(input("Insert your cohort: \n"))

    # validating the correct campus has been entered
    final_campus = ["durban", "johannersburg", "cape town", "phokeng"]
    campus = input("Insert the campus you will be attending in: \n")
    while not campus.lower() in final_campus:
        print("Invalid campus")
        campus = input("Insert the campus you will be attending in: \n")
    return first_name, last_name, campus, cohort


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
     
    username = first_name[-3:] + last_name[:3] + final_campus + str(cohort) 
    return username
    
    

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    
    if campus.lower() == "durban":
        abbr_campus_name = "DBN"
    elif campus.lower() == "cape town":
        abbr_campus_name = "CPT"
    elif campus.lower() == "johannersburg":
        abbr_campus_name = "JHB"
    else:
        abbr_campus_name = "PHO"
    return abbr_campus_name

if __name__ == '__main__':
    first_name, last_name, campus, cohort = user_details()
    abbr_campus_name = user_campus(campus)
    username = create_user_name(first_name, last_name, cohort, abbr_campus_name)
    print(username)
    
    
    
    
    