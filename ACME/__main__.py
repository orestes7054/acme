import sys
from ACME.utils import check_file_extesion,  help, example, read_file_lines
from ACME.errors import FileNotLoaded, OptionError
from ACME.payment_class import AcmeEmployee

def main():
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
            #The user just type the option or the file
            if argv[0] == '-h':
                help()
            elif argv[0] == '-example':
                employees = read_file_lines('ACME/acme.txt')
                for employee in employees:
                    AcmeEmployee(employee)
                example(str(AcmeEmployee.output))
                AcmeEmployee.output = ""
            else:
                user_input = argv[0]
                employees = check_file_extesion(user_input)
                for employee in employees:
                    AcmeEmployee(employee)
                print(str(AcmeEmployee.output))
    else:
        FileNotLoaded()

if __name__ == '__main__':
    main()
    
    
   
