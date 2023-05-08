import  logging

logger = logging.getLogger()

logging.basicConfig(level='DEBUG', filename="client.log",filemode="a",
                    format='%(asctime)s %(levelname)s %(module)s %(message)s')