import tkinter as tk
import logging
from bitmex import get_contracts

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



if __name__ == "__main__":
    bitmex_contracts = get_contracts()

    root = tk.Tk()

    for contract in bitmex_contracts:
        label_widget = tk.Label(root, text=contract)
        label_widget.pack(side=tk.TOP)


    root.mainloop() 