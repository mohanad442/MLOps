import logging
logging.basicConfig()

logger = logging.getLogger('demo app')
logger.setLevel(logging.INFO)

logger.error(f'Error')
logger.exception(f'Exception')
logger.warning(f'warning')
logger.info(f'Info')
logger.debug(f'Debug')