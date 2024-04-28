from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7012598022:AAHqvfpPESQB7yPsoS0p5WtgzLqpPI-EaSs'
BOT_USERNAME: Final = '@GameSuggesterBot'



#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Добро пожаловать в GameSuggesterBot! 🎮 Готовы окунуться в мир захватывающих приключений? Я здесь, чтобы помочь вам найти самые интересные игры! Просто скажите мне, что вы ищете, и я подберу для вас идеальные варианты. Готовы начать?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Тест хуйня это хелп типа')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ты вышел из контекста')



#Respones
def hanlde_response(text: str) -> str:
    text: str = text.lower()

    if 'привет' in text:
        return 'Ну здарова'
    if 'пока' in text:
        return 'Ну пока'
    return 'иди отсюда'

async def handle_message(update: Update,context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message.type}: "{text}"')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Запуск бота...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polling the bot about the message
    print('Polling...')
    app.run_polling(poll_interval=3)