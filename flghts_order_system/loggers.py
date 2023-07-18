import logging
import logging.config


def lggr():
    
    logger = logging.getLogger(__name__)
    if not logger.handlers:  # avoid adding duplicate handlers
        logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler('logs.log')
        fileHandler.setLevel(logging.INFO)
        fileFormatter = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        fileHandler.setFormatter(fileFormatter)
        logger.addHandler(fileHandler)
    
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.INFO)
        streamFormatter = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        streamHandler.setFormatter(streamFormatter)
        logger.addHandler(streamHandler)
    
    return logger

def errLogger():

    errorLogger = logging.getLogger()
    if not errorLogger.handlers:
        errorLogger.setLevel(logging.ERROR)
        errorHandler = logging.FileHandler('errorLogs.log')
        errorFormater = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        errorHandler.setLevel(logging.ERROR)
        errorHandler.setFormatter(errorFormater)
        errorLogger.addHandler(errorHandler)
    
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.ERROR)
        streamFormatter = logging.Formatter(
            '%(asctime)s - %(name)s -model: %(module)s -func:%(funcName)s -line:%(lineno)d - %(levelname)s - %(message)s'
            )
        streamHandler.setFormatter(streamFormatter)
        errorLogger.addHandler(streamHandler)
    
    return errorLogger

