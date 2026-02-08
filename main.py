import os
import asyncio
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from aiohttp import web  # server fake só pra Render

TOKEN = os.getenv("TOKEN")

frases_finais = [
    "🔥 ACORDA GRUPOOO!!!",
    "💀 SUMIU TODO MUNDO???",
    "🚨 QUEM NÃO RESPONDER É NPC",
    "😂 CADÊ OS MEMBROS FANTASMAS?",
    "💥 GRUPO REVIVIDO NA BASE DO CAOS",
    "🧠 ATIVEM O CÉREBRO IMEDIATAMENTE",
    "🤡 QUEM SUMIR VIRA MEME",
    "💣 CONVOCAÇÃO NÍVEL APOCALIPSE",
]

gifs_caos = [
    "https://media.giphy.com/media/l0MYB8Ory7Hqefo9a/giphy.gif",
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
    "https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif",
]

async def convocar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    msg = await context.bot.send_message(chat_id, "💣 INICIANDO CONVOCAÇÃO EXPLOSIVA...")
    await asyncio.sleep(1)
    efeitos = ["🚨🚨 ALERTA MÁXIMO 🚨🚨","😂 MEME MODE ATIVADO","🔥 INVOCANDO MEMBROS...","💀 ACORDANDO OS MORTOS","🤡 CHAMANDO OS SUMIDOS","🧨 PREPARANDO EXPLOSÃO SOCIAL"]
    for efeito in efeitos:
        await context.bot.edit_message_text(efeito, chat_id, msg.message_id)
        await asyncio.sleep(1)
    await context.bot.edit_message_text("3️⃣ SEGURA A BOMBA 💣", chat_id, msg.message_id)
    await asyncio.sleep(1)
    await context.bot.edit_message_text("2️⃣ PREPARA O PRINT 📸", chat_id, msg.message_id)
    await asyncio.sleep(1)
    await context.bot.edit_message_text("1️⃣ VAI EXPLODIR 💥", chat_id, msg.message_id)
    await asyncio.sleep(1)
    frase = random.choice(frases_finais)
    await context.bot.edit_message_text(f"🔥💥 TODOS CONVOCADOS!!! {frase}", chat_id, msg.message_id)
    await context.bot.send_animation(chat_id, random.choice(gifs_caos))

async def caos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respostas = ["💥 CAOS ATIVO!!!","🔥 O GRUPO PEGOU FOGO","😂 MEME SUPREMACY","🤡 RESPEITA O CAOS","💣 EXPLOSÃO DE NOTIFICAÇÕES","🧠 CÉREBROS EM CURTO"]
    await update.message.reply_text(random.choice(respostas))

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("convocar", convocar))
    app.add_handler(CommandHandler("caos", caos))

    print("💥 BOT CAOS ABSOLUTO ONLINE EM PYTHON 3.13 🔥")

    # Rodar polling em paralelo com server fake
    runner = web.AppRunner(web.Application())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 10000)))
    await site.start()

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
