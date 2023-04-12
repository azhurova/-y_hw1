from datetime import datetime

import art

from application.db.people import get_employees
from application.salary import calculate_salary
from dirty_main import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    first_function()
    second_function()
    print('Date:', datetime.now().strftime('%d.%m.%Y'))
    art.tprint(datetime.now().strftime('%d.%m.%Y'))
