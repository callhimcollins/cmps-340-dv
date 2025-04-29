import logging

from config import CONFIG # type: ignore

logging.basicConfig(filename="code/output/log.txt", level=logging.INFO)

def log(message):
    logging.info(message)

def export_pickle(obj, filename):
    import pickle
    with open(f"{CONFIG['PICKLE_PATH']}", "wb") as f:
        pickle.dump(obj, f)