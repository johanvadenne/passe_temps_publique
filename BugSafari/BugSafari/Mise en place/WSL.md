# Installation
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

## Sécurité
- connexion root: refusé ✔
- nombre de connexion: 1 ❌
- connexion par clé SSH ✔
- connexion par mdp: refusé ✔