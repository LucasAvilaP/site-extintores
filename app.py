from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()  # Carrega as variáveis do .env
app.secret_key = "123456"  # Mantenha isso antes de iniciar as rotas

# Configurações do servidor SMTP do Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    mensagem = request.form.get("mensagem")

    if not nome or not email or not mensagem:
        flash("Por favor, preencha os campos obrigatórios.")
        return redirect("/")

    # Envio do e-mail
    corpo_email = f"""
    🧯 NOVA MENSAGEM DO SITE:
    
    Nome: {nome}
    E-mail: {email}
    Telefone: {telefone}
    Mensagem: {mensagem}
    """

    msg = Message(
        subject="📨 Novo Contato - Extintores XYZ",
        sender=app.config['MAIL_USERNAME'],
        recipients=['lukas.avila02@gmail.com'],  # Destinatário
        body=corpo_email
    )

    mail.send(msg)

    flash("Mensagem enviada com sucesso! Entraremos em contato em breve.")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
