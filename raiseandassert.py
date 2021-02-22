'''
*********************
*                   *
*                   *
*                   *
*                   *
*********************
'''
from os import error
import traceback

def boxPrint(symbol, width, height):
    try: #try and except will try the following code, if it works, itll keep running to except i think
        if len(symbol) != 1:
            raise Exception('"symbol" needs to be a string of length 1') #error message is called a traceback, line at which error happened
    except:
            errorFile = open('error_log.txt', 'a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print("The traceback info was logged in error_log.txt")
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal than 2')

    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    
    print(symbol * width)

boxPrint('o*', 5, 10)

