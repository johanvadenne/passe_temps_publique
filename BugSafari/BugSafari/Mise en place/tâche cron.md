## Installation
```bash
sudo apt-get update
sudo apt-get install cron
```
## création d'une tâche cron
```sh
crontab -e
```
dans le fichier:
```
* * * * * echo $PATH >> ~/crontest
```
lancement des tâche cron
```sh
sudo service cron start
```
vérification
```sh
ls ~/
cat ~/crontest
```