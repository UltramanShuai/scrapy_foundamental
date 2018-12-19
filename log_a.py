#_*_coding:utf-8_*_
# Author   : Leo
# Time     : 19/12/2018

import logging
logging.basicConfig(level=logging.INFO,
                    format='levelname:%(levelname)s [%(filename)s] '
                           '[%(lineno)d] : %(message)s'
                           ' - %(asctime)s', datefmt='[%d/%b/%Y %H:%M:%S]')


logger=logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("1")
    logger.info("2")