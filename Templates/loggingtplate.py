################################for logging copy below code####################
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# specify the path where the log file need to be stored
logging.basicConfig(filename="D:\\Python Programs\\webscraping\\mylog.txt",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                   )
logger = logging.getLogger()
logger.info("this is an info message")
logger.debug("this is a debug message")
logger.warning("this is a warning message")
logger.critical("this is a critical message")
##################### for logging copy above code block ############################