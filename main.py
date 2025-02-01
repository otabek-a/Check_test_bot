from telegram.ext import CallbackContext, Filters, MessageHandler, Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
import os

son = 1
res = {}
ans=[]
def start(update, context):
    reply_key = [
        ['Make_test', 'Check_test'],
        ['all answer band'],
    ]
    make = ReplyKeyboardMarkup(reply_key)
    update.message.reply_text(
        'Assalomu aleykum, iltimos bot ishlashi uchun tugmalardan birini tanlang',
        reply_markup=make
    )

def test(update, context):
    global son, res
    if f'{son}' not in res:
        res[son] = None
        update.message.reply_text(
            'Iltimos, endi to‘g‘ri formatda: mayda harflar va orada bo‘sh joy qo‘ymasdan answer tugmasini bosib javobini yuboring  sonni javobni yuboring. Masalan: absdf...'
        )
    else:
        son += 1
        res[son] = None
        update.message.reply_text(
            'Yangi test tayyor! To‘g‘ri formatda javobni yuboring.'
        )

def send_test(update, context):
    global res, son
    javob = update.message.text

    if ' ' not in javob and javob.islower(): 
        res[son] = javob
        result_text = "\n".join([f"Son: {key}, " for key, value in res.items()])
        update.message.reply_text(f"Javob qabul qilindi! Hozirgi barcha testlar:\n{result_text}")
        son += 1 
    elif javob !='Check_test':
        update.message.reply_text(f"Javob uchun noto‘g‘ri format: {javob}. Iltimos, qayta urinib ko‘ring.")


def check_test(update,context):
    update.message.reply_text('Iltimos testing kodini oldin yozib testni davomidan joy taylamay va xamda mayda xarflarda yuboring masalan: 1asdfg....')
def savol(update,context):
    global res
    matn=update.message.text[0]
    matn2=update.message.text[1:]
    count=res.get(int(matn),'None')
    true=0
    false=0
    i=0
    max_len = max(len(count), len(matn2))
    for i in range(max_len):
        if i < len(count) and i < len(matn2):
           if count[i]==matn2[i]:
              true+=1
           if count[i] != matn2[i]:
            false+=1
        else:
           false+=1
    ans.append(f'TEST={matn} true javoblar: {true}, false javoblar: {false}')
    update.message.reply_text(f'To‘g‘ri javoblar: {true}, Noto‘g‘ri javoblar: {false}')

def tekshir(update,context):
    if update.message.text[0].isdigit():
         savol(update, context)
    else:
        send_test(update, context)





def sasha(update,context):
    global ans
    update.message.reply_text(ans)








updater = Updater(token=os.environ['TOKEN'])
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text('all answer band'),sasha))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.regex('^(Make_test)$'), test))
dispatcher.add_handler(MessageHandler(Filters.regex('^(Check_test)$'), check_test))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, tekshir))

updater.start_polling()
updater.idle()
