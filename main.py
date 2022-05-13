import re
from utils import string_to_time, check_line, get_name_and_days__hours
import json
import sys

class AcmeEmployee:
    def __init__(self, string, company_payment_data):
        #String is the info from the txt 
        self.string = string
        #Open the json file with the company info and make it 
        #a python object
        with open("payment.json") as company_payment_data:
            self.company_payment_data = json.load(company_payment_data)
        #Load the days and weekend days
        self.week_days = self.company_payment_data["week"]
        self.weekend_days = self.company_payment_data["weekend"]
        #Make the string data to time data (worked time) and int data (pay per hour).
        self.week_payment = [ [string_to_time(i[0]), string_to_time(i[1]), int(i[2])] for i in self.company_payment_data["week_pay"]]
        self.weekend_payment = [ [string_to_time(i[0]), string_to_time(i[1]), int(i[2])] for i in self.company_payment_data["weekend_pay"]]
        

    
    def GetName(self):
        """
         Function to obtain the data to proccess from the string passed.
         This function uses regex to parse the data.
         The result data is the name of the employee and a list of tuples:
         tuple[0]=day, tuple[1]=start hour, tuple[2]=end hour.
        """
            
        #Overwrite the object with date time format to manipulate in the ProccesPayment function.
        #employee_days_and_hours = [ (i[0], string_to_time(i[1]), string_to_time(i[2])) for i in employee_days_and_hours]
        #Call the function to make the calculations.
        result = check_line(self.string)
        print(result)
    


    if __name__ == '__main__':
        user_input = sys.argv[1]
        if not check_line(user_input):
            print('Error in line')
        else:
            employee = print(get_name_and_days__hours(user_input))
        
            
       



