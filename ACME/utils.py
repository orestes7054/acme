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
        
        read_lines(lines)

def read_lines(lines):
        cleared_lines = list()
        nro_lines = 1
        for line in lines:
            if not check_line(line):
                print(f"{bcolors.FAIL}Error in line {bcolors.OKBLUE}{nro_lines}{bcolors.ENDC}{bcolors.FAIL} please make sure to use the standar format. This line will not be computed{bcolors.ENDC}")
            else:
                cleared_lines.append(line)
            nro_lines += 1
        for data in cleared_lines:
                name, worked_hours_days = get_name_and_days__hours(data)
                print(name, worked_hours_days)

