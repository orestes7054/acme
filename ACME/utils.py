from datetime import datetime
import re
from errors import EmptyFileError, ErrorFileType, bcolors



def string_to_time(time_string):
        return datetime.strptime(time_string, "%H:%M").time()


def check_line(line):
        string_ok = re.search(r"""
                                ^(([A-Za-z]+[=]+
                                [A-Z]{2}[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]){1},
                                *([A-Z]{2}[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9],)*
                                ([A-Z]{2}[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9])*)$
                                """,line, re.VERBOSE)
        return bool(string_ok)

def get_name_and_days__hours(string):
        #Get the name of the employee.
        employee_name = re.search(r"([A-Za-z]+)([=]+)", string).group(1)
        #Get the worked days and hours as a list of tuples.
        worked_days_and_hours = re.findall(r"""
                                             ([A-Z]{2})([0-9][0-9]:[0-9][0-9])-([0-9][0-9]:[0-9][0-9])
                                             """, string, re.VERBOSE)

        return employee_name, worked_days_and_hours


def check_file_extesion(path):
        if not path.endswith('.txt'):
                raise ErrorFileType()
        return read_file_lines(path)
        


def read_file_lines(path: str) -> str:
        lines = []
        try:
                with open(path) as file:
                        lines = file.readlines()
                if not lines:
                        raise EmptyFileError()
        except FileNotFoundError:
                print(bcolors.FAIL + 'File not found. Make sure to submit the complete path to the file.')
        
        
        return lines


