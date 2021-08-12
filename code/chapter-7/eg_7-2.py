import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s \t %(message)s - line: %(lineno)d')
logger = logging.getLogger()


def fun(values, lst=[]):
    logger.debug(lst)
    lst.extend(values)
    return lst


logger.info(fun([1, 2]))
logger.info(fun([1, 2]))
