import  logging

logger = logging.getLogger()

logging.basicConfig(level=logging.INFO, filename="server.log",filemode="a",
                    format='%(asctime)s %(levelname)s %(module)s %(message)s')

logger.info(msg='Info')
logger.error(msg="Error")
logger.warning(msg="Warning")
