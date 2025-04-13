import logging

logging.basicConfig(filename="code/output/log.txt", level=logging.INFO)

def log(message):
    logging.info(message)

def export_csv(df, filename):
    df.to_csv(f"code/output/exports/{filename}", index=False)

def export_pickle(obj, filename):
    import pickle
    with open(f"code/output/exports/{filename}", "wb") as f:
        pickle.dump(obj, f)