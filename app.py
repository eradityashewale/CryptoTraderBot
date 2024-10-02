import tkinter as tk
import logging

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)


logger.addHandler(stream_handler)
logger.addHandler(file_handler)


logger.debug("This message is important only when debugging the program")
logger.info("This message just show basic information")
logger.warning("This message is about something you should pay attention to")
logger.error("This message helps to debug an error that occured in your program")

root = tk.Tk()

root.mainloop() 