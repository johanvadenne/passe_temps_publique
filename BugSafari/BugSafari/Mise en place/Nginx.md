## Installation
```sh
sudo apt install nginx
```
## création d'un serveur
```sh
cd /etc/nginx/sites-available
nano serveur
```
contenant du fichier:
```
server {
        listen 8080;
        listen [::]:8080;

        root /var/www/nginx/BugSafari;
        index index.html index.htm index.nginx-debian.html;

        server_name BugSafari www.BugSafari;

        location / {
                try_files $uri $uri/ =404;
        }

	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
		fastcgi_pass unix:/run/php/php7.4-fpm.sock;
	}
        
        location ~ /api/vue/([^/]+) {
            rewrite ^/api/vue/([^/]+)$ /BDD_API.php?table=$1&vue=true last;
            include fastcgi_params;  # Inclure les paramètres FastCGI si nécessaire
            fastcgi_pass 127.0.0.1:8080;  # Utilisez l'adresse du serveur FastCGI appropriée
        }
        
        location ~ /api/([^/]+)/(\d+) {
            rewrite ^/api/([^/]+)/(\d+)$ /BDD_API.php?table=$1&id=$2 last;
            include fastcgi_params;  # Inclure les paramètres FastCGI si nécessaire
            fastcgi_pass 127.0.0.1:8080;  # Utilisez l'adresse du serveur FastCGI appropriée
        }
        
        location ~ /api/([^/]+) {
            rewrite ^/api/([^/]+)$ /BDD_API.php?table=$1 last;
            include fastcgi_params;  # Inclure les paramètres FastCGI si nécessaire
            fastcgi_pass 127.0.0.1:8080;  # Utilisez l'adresse du serveur FastCGI appropriée
        }

}
```
*listen*: port d'écoute
*root*: chemin de notre dossier
*index index.html index.htm index.nginx-debian.html;* : fichier par default
*server_name*: nom serveur
*location*: route
## associer nginx et php
```sh
location ~ \.php$ {
		include snippets/fastcgi-php.conf;
		fastcgi_pass unix:/run/php/php7.4-fpm.sock;
	}
```

`fastcgi_pass unix:/run/php/php7.4-fpm.sock;`: représente la version php
## création route
```sh

        location ~ /api/vue/([^/]+) {
            rewrite ^/api/vue/([^/]+)$ /BDD_API.php?table=$1&vue=true last;
            include fastcgi_params;  # Inclure les paramètres FastCGI si nécessaire
            fastcgi_pass 127.0.0.1:8080;  # Utilisez l'adresse du serveur FastCGI appropriée
        }
```
## commande
```sh
sudo service nginx start
sudo service nginx restart
sudo service nginx stop
```