# Real Estate Website setting at local
Clone repository
```
git clone https://github.com/Anhduchb01/BDSWeb
cd BDSWeb
```
## Installation 
Create new Python environment with Python 3.9 by conda
``` 
conda create -n realEstate python=3.9
conda activate realEstate
```
### Install library
##### Window
```
pip install -r requirements.txt
pip install mysqlclient==2.1.1
```
##### MacOS
Install HomeBrew 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Install mysqlclient through HomeBrew
```
brew install mysql
pip install mysqlclient
pip install requirements.txt
```
Running MySQL
```
brew services start mysql
```
### Download Image folder on the following link
```
https://drive.google.com/drive/folders/1wcWnIX7KKhMz7A3as68t6oRIA41imSZO?usp=sharing
```
Then, create new folder Image at `BDSWeb/` then move Image folder to `BDSWeb/Image`

Result example: `BDSWeb/Image/baidang`
### Download XamPP 
```
https://www.apachefriends.org/download.html
```
Install and run XamPPControl.

![image](https://user-images.githubusercontent.com/73813209/179924699-8c786308-cb64-42d8-b67d-75c2be2d03b5.png)

Running two servers: MySQL Database and Apache Web Server. Then, go to following link.
```
http://localhost/phpmyadmin
```
Click to the import tab, then choose file `diachi.sql` at `BDSWeb/diachi.sql`

![image](https://user-images.githubusercontent.com/73813209/179939778-2d7a605e-34ba-4dc0-92fc-7f7569225407.png)

Go to `BDSWeb/BDSWeb/setting.py` change `PASSWORD` to " and `PORT` default is '3306'

## Running code
##### Window
```
python manage.py runserver
```
##### MacOs
Open configure file MySQL server on XamPP, then take socket path of MySQL. Then do the following code.
```
ln -s /this/is/your/MySQL/socket/path /tmp/mysql.sock
brew services restarts mysql
python manage.py runserver
```



