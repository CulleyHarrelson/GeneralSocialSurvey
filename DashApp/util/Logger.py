import logging

logging.basicConfig(format=' %(asctime)s (%(levelname)s): %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def log_debug(msg):
    logging.debug(msg)


def log_info(msg):
    logging.info(msg)


def log_critical(msg):
    logging.critical(msg)


def log_error(msg):
    logging.error(msg)


def log_fatal(msg):
    logging.fatal(msg)


def log_warning(msg):
    logging.warning(msg)