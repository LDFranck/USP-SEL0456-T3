from hashlib import sha256
from cryptography.fernet import Fernet

# Hash senha:
pswd = 'SEL0456'
hash = sha256(pswd.encode('utf-8')).digest()

# Arquivo criptografado:
key = Fernet.generate_key()
with open('chave.key', 'wb') as file:
  file.write(key)

fernet = Fernet(key)
cripto = fernet.encrypt(hash)
 
with open('config.txt', 'wb') as file:
  file.write(cripto)

# Comentários:
# Para uma rotina crítica, o sistema deve apresentar redundância de segurança.
# Nesse exemplo, o arquivo de configurações é encriptado com uma chave que é
# armazenada no arquivo 'chave.key', que pode ser colocada em uma unidade
# remomível para uma autenticação física (exemplo colocar pendrive na máquina).
# A segunda camada é o armazenamento da senha como um hash, que garante proteção
# mesmo se 'chave.key' vazar. A única maneira de executar a rotina é utilizar
# o arquivo de entrada 'entrada.txt' com a senha correta.