## erreur commise
```shell
sudo rm -r /*
```

## Résultat
Certains fichiers et dossiers ont été supprimé, mais pas tout car des dossiers et des fichiers sont protégés par le système et d'autres je ne sais pas pourquoi.

## Problème rencontré
certains fichiers ont été supprimés et le nombre étant inconnu, la carte à joué était la réinstallation.
```
sudo service mysql stop
sudo service mariadb stop
sudo service apache2 stop
sudo service nginx stop

sudo apt purge phpmyadmin
sudo apt purge nginx
sudo apt purge mariadb-server
sudo apt purge php
sudo apt purge apache2

sudo apt remove phpmyadmin
sudo apt-get remove --purge nginx nginx-common nginx-full
sudo apt remove mariadb-server
sudo apt remove php
sudo apt remove apache2

sudo rm -rf /etc/nginx
sudo rm -rf /etc/apache2
sudo rm -rf /etc/mysql /var/lib/mysql
sudo rm -rf /usr/local/mysql
sudo apt-get remove --purge mariadb-server mariadb-common mariadb-client
sudo rm -rf /etc/phpmyadmin
sudo rm /etc/apache2/conf-available/phpmyadmin.conf
sudo rm /etc/apache2/conf-enabled/phpmyadmin.conf

sudo apt-get autoremove
sudo apt-get clean
sudo reboot
```

La commande `whereis` est utilisée pour localiser l'exécutable, les sources et la documentation d'un programme sur votre système. Elle affiche les emplacements de plusieurs composants associés à un programme donné.
```
whereis phpmyadmin
whereis nginx
whereis mariadb-server
whereis php
whereis apache2
```
s'il reste des fichiers supprimer les.

## puis l'installation

## MariaDB
```
sudo apt install mariadb-server
sudo mysql_secure_installation
```
## apache2 et PHP
```
sudo apt-get update
sudo apt-get install apache2 php libapache2-mod-php
```
## phpmyadmin
choisir le serveur apache2 pour l'installation
```
sudo apt install phpmyadmin
```

### NGINX
```
sudo apt install nginx
```