import random
import time 
def get_random_date(start_date, end_date):
        print("printing random date between start_date and end_date")
        random_generator = random.Random()
        start_struct = time.strptime(start_date, "%Y-%m-%d")
        end_struct = time.strptime(end_date, "%Y-%m-%d")
        start_time = time.mktime(start_struct)
        end_time = time.mktime(end_struct)
        random_time = random_generator.uniform(start_time, end_time)
        random_date = time.strftime("%Y-%m-%d", time.localtime(random_time))
        return random_date
print(get_random_date("2020-01-01", "2023-12-31"))