import paramiko

# Génération de la paire de clés SSH
key = paramiko.RSAKey.generate(2048)

# Enregistrement de la clé privée au format OpenSSH
private_key_path = '.cle_privee'
key.write_private_key_file(private_key_path)

# Enregistrement de la clé publique au format OpenSSH
public_key_path = '.cle_publique.pub'
with open(public_key_path, 'w') as f:
    f.write(f'ssh-rsa {key.get_base64()}')

print("Clés SSH générées avec succès.")
