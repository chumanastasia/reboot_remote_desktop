# 💻 ↔️ 💻 reboot_remote_desktop: перезапуск удаленного  компьютера внутри сети  💻 ↔️ 💻
## Описание
В данном проекте расположены скрипты для перезапуска удаленного рабочего стола
Локальный и удаленный компьютеры должны находиться в одной локальной сети

## ⚙️ Инструкция по работе ⚙️ 

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