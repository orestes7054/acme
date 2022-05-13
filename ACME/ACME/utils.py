from datetime import datetime
def string_to_time(time_string):
        return datetime.strptime(time_string, "%H:%M").time()