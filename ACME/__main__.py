from utils import string_to_time, check_file_extesion, help
import json
import sys
from errors import FileNotLoaded, OptionError
from datetime import timedelta
import os

class AcmeEmployee():
    output = ''
    def __init__(self, cleared_data, json_file='ACME/payment.json'):
        self.json_file = json_file
        self.cleared_data = cleared_data
        
        #Open the json file and read the data
        with open(self.json_file) as f:
            company_payment_data = json.load(f)
        self.company_payment_data = company_payment_data
        #Load the days and weekend days
        self.week_days = company_payment_data["week"]
        self.weekend_days = company_payment_data["weekend"]
        #Make the string data to time data (worked time) and int data (pay per hour).
        self.week_payment = [ [string_to_time(i[0]), string_to_time(i[1]), int(i[2])] for i in company_payment_data["week_pay"]]
        self.weekend_payment = [ [string_to_time(i[0]), string_to_time(i[1]), int(i[2])] for i in company_payment_data["weekend_pay"]]
        #After receive the data, procces the payment
        self.procces_payment()
     
        
    def procces_payment(self: list) -> list:
        """
        This function is the core of the app. Here the computation of 
        the total salary is made
        """
        total_payment = 0
        #Extract from the list the employee name and
        #working hours
        employee = self.cleared_data[0]
        working_hours = self.cleared_data[1]
        for data in working_hours:
            day, start_time, end_time = data[0], string_to_time(data[1]), string_to_time(data[2])
            current_hour = start_time
            while current_hour < end_time:
                if day in self.week_days:
                    for pay in self.week_payment:
                        if  pay[0] <= current_hour <= pay[1]:
                            total_payment += pay[2]
                else:
                    for pay in self.weekend_payment:
                        if pay[0] <= current_hour <= pay[1]:
                            total_payment += pay[2]
                                     
                current_hour +=  timedelta(hours=1)
    
        AcmeEmployee.output += f"The amount to pay {employee} is: {total_payment} USD\n"

    @staticmethod
    def save_output():
        """
        Save the output to a .txt file
        """  
        with open("acme_employee_payment_roll.txt", "w+") as wf:
            wf.writelines(AcmeEmployee.output)
        


    def __str__(self) -> str:
        return AcmeEmployee.output



if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) >= 1:
        if len(argv) == 2:
            #If the user types an option and the file 
            if argv[0] == '-sc':
                user_input = argv[1]
                employees = check_file_extesion(user_input)
                for employee in employees:
                    AcmeEmployee(employee)
                print(str(AcmeEmployee.output))
                AcmeEmployee.save_output()
            else:
                raise OptionError
        elif len(argv) == 1:
            #The user just type the option or
            #the file
            if argv[0] == '-h':
                help()
            else:
                user_input = argv[0]
                employees = check_file_extesion(user_input)
                print(employees)
                for employee in employees:
                    AcmeEmployee(employee)
                print(str(AcmeEmployee.output))
    else:
        FileNotLoaded()
    
   
