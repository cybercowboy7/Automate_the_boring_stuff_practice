import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.critical('Start of program')  # This will still log since


# Within this import of the logging module, I define a file to export my log messages to so that it
# does not clutter the screen when running the program
# setting level = logging.DEBUG will show all levels of logging wherein level = logging.ERROR will
# only show ERROR and CRITICAL logs
def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total


print(factorial(5))
logging.debug('End of program')
