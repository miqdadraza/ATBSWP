import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.basicConfig(filename='myProgramLog.txt, 'level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #will print the logs to a file and not show in the program

#logging.disable(logging.CRITICAL) #this will disable the logs critical and below (all messages). You could pass .WARNING will disable all logs warning and below

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial (%s)' %(n))
    total = 1
    #for i in range(n+1):
    for i in range(1,n+1): # now this will ommit the zero. range from 1 to n+1
        total *= i #there is a multiply by 0 problem here, because the first value returned is 0 * total, next is always multiplied by this 0. This happens if the commented code is run
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' %(total))

    return total

print(factorial(6))

logging.debug('End of program')