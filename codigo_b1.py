from hashlib import sha256
from cryptography.fernet import Fernet

# Carregar chave:
with open('chave.key', 'rb') as file:
  key = file.read()

# Arquivo criptografado:
fernet = Fernet(key)
 
with open('config.txt', 'rb') as file:
  cripto = file.read()
 
decripto = fernet.decrypt(cripto)

# Arquivo entrada:
with open('entrada.txt', 'r') as file:
  input = file.read()

hash_input = sha256(input.encode('utf-8')).digest()
is_ok = True if decripto == hash_input else False

if not is_ok:
  raise ValueError(f'Entrada: {input} (SENHA INCORRETA)')
else:
  print(f'Entrada: {input} (SENHA CORRETA)')