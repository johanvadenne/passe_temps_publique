source:
- nginx - php: https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-20-04

info:
>snippets:
>
>Emplacement : /etc/nginx/snippets/
Description : Ce répertoire est utilisé pour stocker des fichiers de configuration réutilisables, appelés "snippets". Un snippet est un fragment de configuration qui peut être inclus dans d'autres fichiers de configuration Nginx. Cela permet de réduire la duplication de code et de faciliter la maintenance.

>modules-enabled:
>
>Emplacement : /etc/nginx/modules-enabled/
Description : Ce dossier contient des liens symboliques vers les fichiers de configuration des modules Nginx actuellement activés. Nginx peut être étendu en activant différents modules, et ces liens symboliques pointent vers les fichiers de configuration correspondants dans le dossier modules-available. Lorsqu'un module est activé, son fichier de configuration est lié ici.

>sites-available:
>
>Emplacement : /etc/nginx/sites-available/
Description : Les fichiers de configuration des différents sites web disponibles sont stockés dans ce dossier. Chaque fichier de configuration représente la configuration d'un site web spécifique. Ces configurations peuvent inclure des informations telles que les paramètres du serveur, les règles de routage, les règles de sécurité, etc.

>sites-enabled:
>
>Emplacement : /etc/nginx/sites-enabled/
Description : Ce dossier contient des liens symboliques vers les fichiers de configuration des sites web Nginx actuellement activés. Ces liens pointent vers les fichiers de configuration correspondants dans le dossier sites-available. En activant ou désactivant ces liens, vous pouvez activer ou désactiver rapidement des sites web spécifiques sans avoir à déplacer ou supprimer les fichiers de configuration.
En résumé, les dossiers snippets, modules-enabled, sites-available, et sites-enabled dans le contexte de Nginx sous Linux sont utilisés pour organiser et gérer les fichiers de configuration, améliorant ainsi la modularité et la facilité de gestion des serveurs web Nginx.