import logging

logging.basicConfig(filename="code/output/log.txt", level=logging.INFO)

def log(message):
    logging.info(message)
