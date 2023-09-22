import logging
import logging.config
import os

'''
This model defines logger functions ( lggr() and errLogger() ), 
each creating logging instances with both file and console output for different log levels. 
The path for log files is based on the location of the script using the os.path.join() function. 
The log format is defined using logging.Formatter. 
lggr() is for general logging, errLogger() focuses just on error logging.

'''


def lggr():
    
    # create a logger instance 
    logger = logging.getLogger(__name__)
    
    # if no handlers are present (avoid adding duplicate handlers)
    if not logger.handlers: 

        # set logger level to info 
        logger.setLevel(logging.INFO)

        # define the path for the log file
        log_file_path = os.path.join(os.path.dirname(__file__), 'logs.log')

        # add a file handler to the logger
        fileHandler = logging.FileHandler(log_file_path)
        
        # sets the logging level for file handler to "INFO".
        fileHandler.setLevel(logging.INFO)
        
        # define the format for log messages displayed in the log file.
        fileFormatter = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        
        # add the file handler to logger
        fileHandler.setFormatter(fileFormatter)
        
        # add fileHandler
        logger.addHandler(fileHandler)
    
        # create a stream handler for logging to the console and set its level
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.INFO)
        
        # define the format of stream for logs on console
        streamFormatter = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        streamHandler.setFormatter(streamFormatter)
        
        # add streamHandler
        logger.addHandler(streamHandler)
    
    return logger

def errLogger():

    # create a logger instance
    errorLogger = logging.getLogger()

    # if no handlers are present (avoid adding duplicate handlers)
    if not errorLogger.handlers:

        # set logger level to error 
        errorLogger.setLevel(logging.ERROR)

        # define the path for the log file
        error_log_file_path = os.path.join(os.path.dirname(__file__), 'errorLogs.log')
        
        # add a file handler to the logger
        errorHandler = logging.FileHandler(error_log_file_path)
        
        # define the format for error log messages displayed in the error log file.
        errorFormater = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        
        # add the file handler to error logger
        errorHandler.setFormatter(errorFormater)
        errorLogger.addHandler(errorHandler)
        
        # create a stream handler for logging to the console and set its level
        streamHandler = logging.StreamHandler()
        errorHandler.setLevel(logging.ERROR)
        
        # set level for stream handler
        streamHandler.setLevel(logging.ERROR)
        
        # define the format of stream for logs on console
        streamFormatter = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        streamHandler.setFormatter(streamFormatter)
        
        # add streamHandler
        errorLogger.addHandler(streamHandler)
    
    return errorLogger

