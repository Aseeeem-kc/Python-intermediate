#  SECURITY LEVELS:
# DEBUG
# INFO
# Warning
# Error 
# Critical

import logging

# logging.basicConfig(level = logging.DEBUG)
# logging.debug('ALL components failed')

# logging.warning('You have got 20 mails in your inbox!')
# logging.critical('ALL components failed')

logger = logging.getLogger("Ashim logger")
# logger.info("The best logger created right now")
# logger.critical("Your app was taken down!")

# logger.log(logging.ERROR, "An error occured")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
# Logging messages
logger.debug("This is a debug message!")
logger.info("This is an important information")
logger.warning("This is a warning!") 
logger.error("This is an error!") 
logger.critical("This is critical!")
