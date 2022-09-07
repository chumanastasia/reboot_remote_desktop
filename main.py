import sys
from datetime import datetime

from loguru import logger

from bash_reboot.run_bash import run_bash_script, PATH_TO_BASH_SCR, PASSWORD, IP_ADDRESS, USER_NAME
from mongo_server.mongo import add_info_to_mongo
from mail_server.send_email import send_email


def main():
    text = input()
    if text == 'error':
        logger.info('Get Error!')
        add_info_to_mongo({"ip": "10.74.8.11",
                           "name_user": "chumakova",
                           "error1": 'ImportError',
                           "time": f'{datetime.now()}'
                           })
        send_email('Error')
        run_bash_script(
            path=PATH_TO_BASH_SCR,
            ip=IP_ADDRESS,
            password=PASSWORD,
            username=USER_NAME
        )
    else:
        logger.info('All good')


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as ex:
            print(ex)
        except KeyboardInterrupt:
            sys.exit(0)

