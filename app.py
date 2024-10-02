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


logger.info('This is logged in all cases')

if __name__ == "__app__":
    logger.info('This is logged only if we execute the app.py file')
    root = tk.Tk()
    root.mainloop() 