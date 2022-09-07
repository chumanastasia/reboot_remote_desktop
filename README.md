# 💻 ↔️ 💻 reboot_remote_desktop: перезапуск удаленного  компьютера внутри сети  💻 ↔️ 💻
## Описание
В данном проекте происходит перезагрузка удаленного рабочего стола, запись ошибки в бд monogo
и отправка письма на почту yandex

## ⚙️ Инструкция по работе ⚙️ 
### Основной файл main.py
```python
def main():
    text = input()
    if text == 'error':
        logger.info('Get Error!')
        add_info_to_mongo({"ip": "ip",
                           "name_user": "username",
                           "error1": 'Error',
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
```
Функция `main` находится в бесконечном цикле. В случае получения триггера `error`,выполняется запись в бд
`mongodb`,  отправка сообщения на яндекс почту и перезагрузка удаленного компьютера
### Локальный компьютер Windows:
1. Установить `Git Bash`  для работы с bash  скриптами
2. Установить `putty (plink)` для автоматического ввода пароля при удаленном подключении
3. Выполнить команду для перезапуска удаленного компьютера 
`unix`:
```commandline
plink -pw '[password]' [username]@[host] "echo "[password]"| sudo -S shutdown -r now"
```
Либо заустить скрипт `windows_to_unix.sh`
```commandline
./windows_to_unix.sh [ip]
```
`windows`:
```commandline
plink -pw '[password]' [username]@[host] "shutdown /r"
```
Либо заустить скрипт `windows_to_windows.sh`
```commandline
./windows_to_windows.sh [ip]
```

### Локальный компьютер unix:
1. Установить `sshpass`  для автоматического ввода пароля
2. Выполнить команду для перезапуска удаленного компьютера 
`unix`:
```commandline
sshpass -p '[password]' ssh -q [username]@[host] "echo "[password]"| sudo -S shutdown -r now"
```
Либо заустить скрипт `windows_to_unix.sh`
```commandline
./unix_to_unix.sh [ip]
```
**windows**:
```commandline
sshpass -p '[password]' ssh -q [username]@[host] "shutdown /r"
```
Либо заустить скрипт `unix_to_windows.sh`
```commandline
./unix_to_windows.sh [ip]
```