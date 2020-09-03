from telegram.ext import Updater,InlineQueryHandler, CommandHandler
import requests,logging
from decouple import config


def getty():
    data = requests.get('https://covidnigeria.herokuapp.com/api').json()
    samples,confirmed,active,discharged,deaths = data["data"]["totalSamplesTested"],data["data"]["totalConfirmedCases"],data["data"]["totalActiveCases"],data["data"]["discharged"],data["data"]["death"]
    return ( "total-samples-tested"+":"+str(samples) + '\n' +
    "confirmed-cases"+":"+str(confirmed) + '\n' +
    "active-cases"+":"+str(active) + '\n' +
    "discharged-patients"+":"+str(discharged) +'\n'
    "deaths-recorded"+":"+str(deaths))

def greet():
    x = 'hello !, hola !, bonjour  e benvenuto !, get up-to-date coronavirus cases in nigeria by simply typing the word /casez'
    return x



def casez(update, context):
    cases = getty()
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=cases)

def hello(update,context):

    greetings = greet()
    salut = 'hello !, hola !, bonjour  e benvenuto !, get up-to-date coronavirus cases in nigeria by simply typing the word /casez'
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=greetings)




def main():
    updater = Updater(config("token"),use_context=True)
    dp = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logger = logging.getLogger(__name__)
    dp.add_handler(CommandHandler('casez',casez))
    dp.add_handler(CommandHandler('greet',greet))

    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
