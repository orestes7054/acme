import logging 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class EmptyFileError(Exception):
        def __init__(self):
                error = logging.getLogger()
                error.error(bcolors.WARNING + "The file has no data. Please select another file.")
                exit(1)


class FileNotLoaded(Exception):
        def __init__(self):
                error = logging.getLogger()
                error.error(bcolors.WARNING + 'You have not submitted any file!')
                exit(1)

class ErrorFileType(Exception):
        def __init__(self):
                error = logging.getLogger()
                error.error(bcolors.WARNING + 'The file extension is not supported. Please select a' \
                 +  bcolors.OKGREEN + ' .txt file')
                exit(1)
