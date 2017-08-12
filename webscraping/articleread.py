'''
for a given URL this program gets all the url's and prints them this is done using BeautifulSoup package
it also has the logging feature, the log file is mylog.txt
this is clean code
adding this to check if it gets to github
'''

from bs4 import BeautifulSoup
import urllib3
################################for logging copy below code####################
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
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

http = urllib3.PoolManager()
url = "http://www.cnn.com"
response = http.request("GET", url)
soup = BeautifulSoup(response.data, "html.parser")
linkcount = 0
for links in soup.find_all("a"):
    linkcount += 1
    print(links.get("href"))
print(linkcount)