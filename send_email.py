import smtplib
from credenciais import email_remetente, senha
from email.message import EmailMessage
import ssl

def send_warning(email_usuario, peso, advertencias):
    
    email_destinatario = str(email_usuario)
    subject = "ADVERTÊNCIA DE DESPERDICIO"
    body = f"""Ola Caro Usuário,

                Você está recebendo este email pois a quantia desperdiçada de comida de seu prato hoje
                foi de {peso} gramas.
                O intuito do projeto é diminuir o desperdício de alimento usando como auxílio o uso de tecnologia, aplicando-a no Restaurante Universitário. 
                O desperdício de comida é, explicitamente, um problema global, visto que, enquanto muito alimento é jogado fora, muitos nem mesmo possuem o que comer. 
                Segundo um relatório da Organização das Nações Unidas(ONU)[1] são, em 2022, 828 milhões de pessoas que passam fome no mundo, e, segundo a mesma, 
                estima-se que o desperdício beira os 121 quilos de comida per capita anual.

                Contamos com sua ajuda para mudar este cenário!

                Lembrando que ao atingir 3 ADVERTÊNCIAS, o valor de seu ticket será aumentado por 1(uma) semana.
                
                Suas advertências: {advertencias}
    
    """

    em = EmailMessage()
    em['From'] = email_remetente
    em['To'] = email_destinatario
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_remetente, senha)
        smtp.sendmail(email_remetente, email_destinatario, em.as_string())

    print('Email Enviado!')
    return
