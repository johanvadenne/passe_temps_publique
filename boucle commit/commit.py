from git import Repo

repo_path = './repertoire'

# Initialiser le référentiel Git
repo = Repo(repo_path)

for i in range(64):
    fichier = open("chemin/fichier", "w+", encoding="utf-8")
    fichier.write(str(i))
    fichier.close()

    # Ajouter les fichiers modifiés ou nouvellement créés au commit
    repo.index.add(["chemin/fichier"])

    # Effectuer le commit avec un message
    commit_message = 'commit - '+str(i)
    repo.index.commit(commit_message)

# Pusher les modifications vers le serveur distant (si nécessaire)
origin = repo.remote('origin')
origin.push()
print(i)