import smtplib

conexao = smtplib.SMTP('smtp.gmail.com', 587)
type(conexao)
conexao
conexao.ehlo()  # indica se a conexão está funcionando

# criptografia dos dados
conexao.starttls()
