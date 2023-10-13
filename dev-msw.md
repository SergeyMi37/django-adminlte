# useful commands
## django ---------------------------------------------------------------
```
python -m venv dtb_venv
source dtb_venv/bin/activate
source dtb_venv/Scripts/activate # for Windows
pip install -r requirements.txt

wget --continue https://github.com/intersystems-community/iris-driver-distribution/raw/main/DB-API/intersystems_irispython-3.2.0-py3-none-any.whl &&     pip install intersystems_irispython-3.2.0-py3-none-any.whl &&     rm intersystems_irispython-3.2.0-py3-none-any.whl

# pip install appmsw/api/intersystems_irispython-3.2.0-py3-none-any.whl
python -m pip install --upgrade pip
python manage.py makemigrations #<name> ex. appmsw
python manage.py migrate
python manage.py createsuperuser --noinput --username adm --email adm@localhost.com
# python run_polling.py
python manage.py runserver

python -m venv dtb_venv && source dtb_venv/Scripts/activate && pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate && python manage.py runserver 8081

# https://the-bosha.ru/2016/06/29/django-delaem-damp-bazy-dannykh-i-vosstanavlivaem-iz-nego-s-dumpdata-i-loaddata/
# https://realpython.com/django-pytest-fixtures/#fixtures-in-django
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > db-all.json
python manage.py loaddata db-all.json
python manage.py dumpdata --exclude auth.permission --exclude auth.user --exclude contenttypes --exclude auth.group --exclude admin.logentry --exclude sessions.session --indent 2 > db-init-param.json

# https://vivazzi.pro/ru/it/translate-django/
# https://egorovegor.ru/django-multiple-language-support/
mkdir locale
django-admin makemessages -l ru -i env -i src
django-admin makemessages -l en -i env -i src
django-admin makemessages -a -i env -i src # update
django-admin compilemessages -i env -i src

python manage.py collectstatic 
# 
pip freeze > requirements.txt

## docker ------------------------------------------------------------------
### stoped and clean all containers
docker stop $(docker ps -a -q) &&  docker rm $(docker ps -a -q) && docker system prune -f
### rmi images
docker rmi $(docker images -a -q) && docker system prune -f
### clean up docker 
```
docker system prune -f
```
### start container with iris
```
$ docker-compose up -d
```
docker-compose up --build -d
```
### build container with no cache
```
docker-compose build --no-cache --progress=plain
```
### open terminal to docker
```
docker-compose exec iris iris session iris -U IRISAPP
```
```
docker logs <container_id>
docker stop $(docker ps -f name=sys -q) &&  docker rm $(docker ps -f name=sys -q) && docker system prune -f
```

## git ------------------------------------------------------------------
### commit and push
```
git add *
git commit -am "upd"
git push
```
## git stored
```
git config --global credential.helper "cache --timeout=86400"
git config --global credential.helper store
```
```
git stash
git stash pop
git stash drop
```
```
git config --global credential.helper store
git config --global user.name "SergeyMi37"
git config --global user.email "Sergey.Mikhaylenko@gmail.com"
```
## ---------- SQLite
  sudo apt install sqlite3
  sqlite3 db.sqlite3 'select * from auth_user'
  sqlite3 db.sqlite3 'select * from MainApp.snippet'
  sqlite3 db.sqlite3 'select * from appmsw_param'

## export IRIS Analytics artifacts
```
d ##class(dev.code).export("*.DFI")
```
## build cube
```
do ##class(%DeepSee.Utils).%BuildCube("CubeName")
```
## export globals
```
do $System.OBJ.Export("po*.GBL","/irisdev/app/src/gbl/globals.xml",,.errors)
zw errors
```
## update code apptools-django application
```
USER>do ##class(apptools.core.code).exp("/iris-backup/apptools/apptools-django/src/","apptools.","apptools.M")
```

## zpm --------------------------------------------------------------------
## Installed zpm short one line
```
s r=##class(%Net.HttpRequest).%New(),proxy=$System.Util.GetEnviron("https_proxy") Do ##class(%Net.URLParser).Parse(proxy,.pr) s:$G(pr("host"))'="" r.ProxyHTTPS=1,r.ProxyTunnel=1,r.ProxyPort=pr("port"),r.ProxyServer=pr("host") s:$G(pr("username"))'=""&&($G(pr("password"))'="") r.ProxyAuthorization="Basic "_$system.Encryption.Base64Encode(pr("username")_":"_pr("password")) set r.Server="pm.community.intersystems.com",r.SSLConfiguration="ISC.FeatureTracker.SSL.Config" d r.Get("/packages/zpm/latest/installer"),$system.OBJ.LoadStream(r.HttpResponse.Data,"c")

zn "%SYS" d ##class(Security.SSLConfigs).Create("z") s r=##class(%Net.HttpRequest).%New(),r.Server="pm.community.intersystems.com",r.SSLConfiguration="z" d r.Get("/packages/zpm/latest/installer"),$system.OBJ.LoadStream(r.HttpResponse.Data,"c")

zpm "generate d:\_proj\_mygirhub\isc-apptools-lockdown-2\isc-apptools-lockdown\src\ -export 00000,appmsw"
```

## .bashrc ----------------------------------------------------------------------
### User specific aliases and functions
```
alias mc="mc -S dark"
alias hi="history"
alias myip='wget -qO myip http://www.ipchicken.com/; grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" myip;  rm myip'
export PATH=$PATH:/opt/libreoffice6.4/program
```

### PgUp/PgDn
### https://qastack.ru/programming/4200800/in-bash-how-do-i-bind-a-function-key-to-a-command
```
if [[ $- == *i* ]]
then
    bind '"\e[5~": history-search-backward'
    bind '"\e[6~": history-search-forward'
fi
```
### f12
```
bind '"\e[24~":"pwd\n"'
```
export HISTCONTROL=ignoredups:erasedups

## ---------------- mc
Ctrl x h - add directory
Ctrl \ - change directory
Alt i - syncronizire directory

## wsl ----------------------------------------------------------
https://docs.microsoft.com/ru-ru/windows/wsl/basic-commands
https://ab57.ru/cmdlist/wslcmd.html

### start docker and ssh
```
sudo service docker start && sudo /etc/init.d/ssh restart
```
### show list
```
wsl --list -v
```
### export to tar
```
wsl --export Ubuntu20.04 d:\wsl\wsl-backup\Ubuntu20-mc-dock.tar
```
### import from tar
```
wsl --import Ubu20 d:\wsl\Ubu20 d:\wsl\wsl-backup\curr-Ubuntu20.tar
```
### terminate
```
wsl -t Ubuntu
```
### shutdown all
```
wsl -shutdown
```
### set default
wsl --set-default Ubu20.04-mc-dock

wsl --distribution Ubu20.04 --user msw

# --------------------
import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
#----------------------
$ python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
>>> con = sqlite3.connect("db.sqlite3")  
>>> cursor=con.cursor()
>>> cursor.execute("select sqlite_version();")
<sqlite3.Cursor object at 0x00000232697E7CC0>
>>> record = cursor.fetchall()
>>> print("Версия базы данных SQLite: ", record)
Версия базы данных SQLite:  [('3.37.2',)]
>>> cursor.execute("select * from auth_user")
<sqlite3.Cursor object at 0x00000232697E7CC0>
>>> record = cursor.fetchall()
>>> print("Пользователи", record)
Пользователи [(1, 'pbkdf2_sha256$260000$W52iGSnSLyo813qud4Povb$EuGqGkUnaxZOgMGBWiSGl4rDu31AELyPZibfqagyUSM=', '2023-08-24 16:39:26.728000', 1, 'adm', '', 'adm@localhost.com', 1, 1, '2023-08-24 16:39:11.568000', '')]
>>> cursor.close()
>>> con.close()               
>>> exit()
