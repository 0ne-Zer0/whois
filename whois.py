#Importa biblioteca socket para trabalhar com pacotes de rede
import socket
import sys

# Cria variável para fazer conexão e receber o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o host do registro.br
host = "200.160.2.3"
port = 43

# Conecta no host
s.connect((host, port))

# Envia informação
s.send((sys.argv[1] + "\r\n").encode())

# Pega resultado
resposta = s.recv(4096)
print(resposta.decode(errors='ignore'))

# Fecha a conexão
s.close()
