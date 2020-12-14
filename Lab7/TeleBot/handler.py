from markups import first_markup, second_markup, re_second_markup
from telegram import ReplyKeyboardRemove
import random
import const


class Handler:
    return_flag = True

    def __init__(self):
        self.message = None
        self.effective_chat = None

    def start(self, context):
        chat = self.effective_chat
        self.message.reply_text(
            "Привет {}, мне еще не дали имени, я расскажу тебе что там с курсом".format(chat.first_name),
            reply_markup=first_markup())

    def reload(self, context):
        self.message.reply_text(random.choice(const.ANSWERS_RELOAD), reply_markup=first_markup())

    def all_message(self, context):
        msg = self.message.text
        if msg == 'Закрыть':
            self.message.reply_text('Если я понадоблюсь нажми /reload', reply_markup=ReplyKeyboardRemove())
        elif msg == 'Назад':
            self.message.reply_text("Выберете что-то одно", reply_markup=first_markup())
        elif msg == '↹':
            if Handler.return_flag:
                self.message.reply_text("Выберете валюту.", reply_markup=re_second_markup())
            else:
                self.message.reply_text("Выберете валюту.", reply_markup=second_markup())
            Handler.return_flag = not Handler.return_flag
        else:
            self.message.reply_text(random.choice(const.ANSWERS_ERRORS))
