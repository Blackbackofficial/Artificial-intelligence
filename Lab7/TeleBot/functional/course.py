from handler import Handler
from markups import third_markup
from telegram.ext import ConversationHandler
from telegram import ParseMode
import requests
import const


class Course(Handler):

    def start_course(self, context):
        self.message.reply_text("Во что бы вы хотели перевести?", reply_markup=third_markup())
        return "currency"

    def enter_currency(self, context):
        if self.message.text in const.CURRENCY:
            if not self.message.text == 'Назад':
                context.user_data['currency'] = self.message.text + 'RUB'
                requestsIB = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&interval=1'
                                          'min&apikey=UWFL45VWBLIXSZD3'.format(context.user_data['currency'])).json()
                value = 1 * "{0:.2f}".format(float(requestsIB['Global Quote']['05. price']))
                text = '<b>{currency}:</b> <code>{value}</code>₽'.format(currency=self.message.text, value=str(value))
                self.message.reply_text(text, parse_mode=ParseMode.HTML)
            else:
                Handler.all_message(self, context)
                return ConversationHandler.END
        else:
            self.message.reply_text("Вы не выбрали ни одной кнопки!")



