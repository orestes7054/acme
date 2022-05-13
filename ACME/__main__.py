import re
from utils import string_to_time, check_file_extesion
import json
import sys
from errors import FileNotLoaded

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
        #Get the name of the employee.
        employee_name = re.search(r"([A-Za-z]+)([=]+)", self.string).group(1)
        #Get the worked days and hours as a list of tuples.
        employee_days_and_hours = re.findall(r"([A-Z]{2})([0-9][0-9]:[0-9][0-9])-([0-9][0-9]:[0-9][0-9])", self.string)
        #Overwrite the object with date time format to manipulate in the ProccesPayment function.
        employee_days_and_hours = [ (i[0], string_to_time(i[1]), string_to_time(i[2])) for i in employee_days_and_hours]
        #Call the function to make the calculations.
        return employee_days_and_hours, employee_days_and_hours



    if __name__ == '__main__':
        if len(sys.argv) < 2:
            FileNotLoaded()
        user_input = sys.argv[1]
        check_file_extesion(user_input)
        



