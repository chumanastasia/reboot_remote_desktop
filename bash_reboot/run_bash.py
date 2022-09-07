import subprocess

from loguru import logger


PATH_TO_BASH_SCR = 'path_to_sh_skript'
# Первый позиционный аргумент
IP_ADDRESS = 'ip_address'
# Второй позиционный аргумент
PASSWORD = 'password_username'
# Третий позиционный аргумент
USER_NAME = 'username'


def run_bash_script(path, ip, password, username):
    try:
        subprocess.Popen([f'{path}', f'{ip}', f'{password}', f'{username}'])
        logger.success('Remote desktop was rebooted successfully!')
    except Exception as _ex:
        logger.error(f'{_ex}')

