from telegram.ext import Updater,InlineQueryHandler, CommandHandler
import requests,logging
from decouple import config
import pandas as  pd
from pandas import DataFrame
from bs4 import BeautifulSoup
import time

def totale():
    data = requests.get('https://api.covid19api.com/summary').json()
    new,total,newdeath,totaldeath,newrecovered,totalrecovered = data["Global"]["NewConfirmed"],data["Global"]["TotalConfirmed"],data["Global"]["NewDeaths"],data["Global"]["TotalDeaths"], data["Global"]["NewRecovered"], data["Global"]["TotalRecovered"]
    df = pd.DataFrame({"countries":
    [data['Countries'][i]['Country'] for i in range(len(data['Countries']))],
    "total-confirmed":
    [data['Countries'][i]['TotalConfirmed'] for i in range(len(data['Countries']))]})
    #print(df.head())
    #high_low_cases = data["Countries"]["TotalConfirmed"]
    x = max(df['total-confirmed'])
    y = min(df['total-confirmed'])
    
   


    return("###COVID-19 UPDATES !, STAY TUNDED##\n" "\nNovel(new cases):"+str(new) + '\n' + "Worldwide-case-count:"+str(total) +
    '\n' + "Recent worldwide deaths:"+str(newdeath) + '\n' + 
    "Total-number-of confirmed worldwide deaths:" + str(totaldeath) + '\n' +
    "recently recovered covid-patients:" + str(newrecovered) + '\n' + "total-recovered-patients:"+str(totalrecovered)
    + '\t' + '\n' + '\n'+ "\nNB:" + '\n'+
     f"the the highest number of confirmed cases in a single country is {x}" + '\n' +
    f"the the lowest number of confirmed-cases in a single country  is {y}" + '\n' +'\n' +
   'be safe people and hope for the best !')

def scraper():
     ##scraper parts
    #response = requests.get('https://www.who.int/')
    response = requests.get('https://www.bmj.com/coronavirus')
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find(class_="css-1wdyrrm")
    tags = tags.findAll('a')
    for tag in tags:
        res = tag['href']
        time.sleep(1)
    print(res)
    return ("for additional resources check out the following links:"+ '\n'+ res)



def casez(update, context):
    cases = totale()
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=cases)

def casez2(update,context):
    cases2 = scraper()
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=cases2)


def main():
    updater = Updater(config("token2"),use_context=True)
    dp = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logger = logging.getLogger(__name__)
    print(logger)
    dp.add_handler(CommandHandler('start',casez))
    dp.add_handler(CommandHandler('resource',casez2))
    #dp.add_handler(CommandHandler('greet',greet))

    
    updater.start_polling()
    updater.idle()

if __name__ =="__main__":
    main()

