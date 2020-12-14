from telegram import ParseMode
from handler import Handler
from markups import first_markup, second_markup
from telegram.ext import ConversationHandler
import requests
import const


def filter_currency(context):
    currency = context.user_data['currency'][3:6]
    element = const.CURRENCY.index(currency)
    currency = const.CURRENCY_ICON[element]
    return currency


class Convertor(Handler):

    def convertor_start(self, context):
        self.message.reply_text("Во что бы вы хотели перевести?", reply_markup=second_markup())
        return "currency"

    def convertor_currency(self, context):
        if self.message.text in const.CURRENCY:
            if not self.message.text == '↹' and not self.message.text == 'Назад':
                context.user_data['currency'] = self.message.text.replace(" → ", "")
                self.message.reply_text("Напишите число для перевода!")
                return "value"
            elif self.message.text == 'Назад':
                Handler.all_message(self, context)
                Handler.return_flag = True
                return ConversationHandler.END
            else:
                Handler.all_message(self, context)
        else:
            self.message.reply_text("Вы не выбрали ни одной кнопки!")

    def convertor_value(self, context):
        try:
            if self.message.text == 'Назад':
                Handler.all_message(self, context)
                Handler.return_flag = True
                return ConversationHandler.END
            value = context.user_data['value'] = float(self.message.text)
            requestsIB = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&interval=1'
                                      'min&apikey=UWFL45VWBLIXSZD3'.format(context.user_data['currency'])).json()
            value = value * float(float(requestsIB['Global Quote']['05. price']))
            value = "{0:.2f}".format(value)
            currency = context.user_data['currency'][0:3]
            val = filter_currency(context=context)
            text = '<b>{currency}:</b> <code>{value}</code>{val}'.format(currency=currency, value=str(value), val=val)
            self.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=first_markup())
            return ConversationHandler.END
        except ValueError:
            self.message.reply_text("Вы меня сломали!", reply_markup=first_markup())
            return ConversationHandler.END
