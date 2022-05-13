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
       
    def ProccesPayment(self, employee_name, employee_days_and_hours):
        total_payment = 0

        for data in employee_days_and_hours:
            day, start_time, end_time = data[0], data[1], data[2]
            current_hour = start_time
            while current_hour < end_time:
                if day in self.week_days:
                    for pay in self.week_payment:
                        if  pay[0] <= current_hour <= pay[1]:
                            total_payment += pay[2]
                else:
                    for pay in self.weekend_payment:
                        print(pay[0],pay[1])
                        print(current_hour)
                        if pay[0] <= current_hour <= pay[1]:
                            total_payment += pay[2]           
                current_hour += timedelta(hours=1)
                
                
        print(total_payment)

   



    if __name__ == '__main__':
        if len(sys.argv) < 2:
            FileNotLoaded()
        user_input = sys.argv[1]
        check_file_extesion(user_input)
        



