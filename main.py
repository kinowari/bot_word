import telebot
global string,id
from modals import User,Quest
from modals import session
import time

bot = telebot.TeleBot('1517294601:AAG1nrb-sTECo1tWNaE96qceQqp4gTbF7Mw')
def reletter(string):
    ss=''
    a="""    
    а
   а а
  ааааа
 а     а
а       а
"""
    b="""
бббббб
б
бббббб
б     б
бббббб"""
    v="""
вввввв
в     в
вввввв
в     в
вввввв"""
    g="""
ггггггг
г
г
г
г"""
    d=""" 
 ддддд
 д   д
 д   д
ддддддд
д     д"""
    e="""
еееееее
е
ееееее
е
еееееее"""
    zh="""
ж   ж   ж
 ж  ж  ж
    ж
 ж  ж  ж
ж   ж   ж"""
    z="""
ззззззз
      з
 зззззз
      з
ззззззз"""
    i="""
и         и
и      и и
и    и   и
и  и     и
и         и"""
    k="""
к      к
к    к
к к
к    к
к      к"""
    l="""     
     л
    л л
   л   л
  л     л
 л       л"""
    m="""
м         м
м м     м м
м  м   м  м
м    м    м
м         м"""
    n="""
н       н
н       н
ннннннннн
н       н
н       н"""
    o=""" 
 ооооооо
о       о
о       о
о       о
 ооооооо"""
    p="""
ппппппппп
п       п
п       п
п       п
п       п"""
    r="""
рррррррр
р       р
рррррррр
р
р"""
    s=""" 
 ссссссс
с
с
с
 ссссссс"""
    t="""
ттттттттт
      т
      т
      т
      т"""
    y="""
у      у
 у    у
   у 
  у
у
"""
    f=""" 
 ффффффф
ф   ф   ф
 ффффффф
    ф
    ф"""
    h="""
х       х
  х   х
    х
  х   х
х        х"""
    c="""
ц     ц
ц     ц
ц     ц
цццццццц
       ц"""
    ch="""
ч      ч
ч      ч
 ччччччч
       ч
       ч"""
    sh="""
ш   ш   ш
ш   ш   ш
ш   ш   ш
ш   ш   ш
шшшшшшшшш"""
    shch="""
щ   щ   щ
щ   щ   щ
щ   щ   щ
щщщщщщщщщщ
          щ"""
    firm="""
ъъ
 ъ
 ъъъъъъъ
 ъ      ъ
 ъъъъъъъ"""
    soft="""
ь
ь
ььььььь
ь      ь
ььььььь"""
    ea="""
эээээээ
       э
 эээээээ
       э
эээээээ"""
    u="""
ю  ююю
ю ю   ю
юю    ю
ю ю   ю
ю  ююю"""
    self="""
яяяяя
я    я
яяяяя
я    я
я      я"""
    dict={' ':'\n\n','а':a,'б':b,'в':v,'г':g,'д':d,'е':e,'ё':e,'ж':zh,'з':z,'и':i,'й':i,'к':k,'л':l,'м':m,'н':n,'о':o,'п':p,
          'р':r,'с':s,'т':t,'у':y,'ф':f,'х':h,'ц':c,'ч':ch,'ш':sh,'щ':shch,'ъ':firm,'ь':soft,'э':ea,'ю':u,'я':self}

    for letter in string:
        try:
            if letter!=' ':
                ss+=dict.get(letter.lower())+'\n'
            else: ss+dict.get(letter)+'\n'
        except:print(letter)
    return ss

def transliteration(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')
    trantab = {k:v for k,v in zip(cyrillic,latin)}
    newtext = ''
    for ch in text:
        if ch!=' ':
            casefunc =  str.capitalize if ch.isupper() else str.lower
            newtext += casefunc(trantab.get(ch.lower()))
        else:newtext +=' '
    return newtext

@bot.message_handler(commands=['menu'])
def menu(message):
    global string
    if message.text !='/menu':
        string=message.text
    else:str('/str')
    bot.send_message(message.from_user.id," Выбери следующее действие со своим сообщением:\n"
                                              "1) Вывести все капсом ( для этого мне нужно дать команду '/caps').\n"
                                              "2) Вывести все маленькими ( для этого мне нужно дать команду '/low').\n"
                                              "3) Вывести все буквами из букв ( для этого мне нужно дать команду '/letter'.)\n"
                                              "4) Вывести количество символов в сообщении ( для этого мне нужно дать команду '/length'.)\n"
                                              "5) Вывести историю запросов ( для этого мне нужно дать команду '/history'.)\n"
                                              "6) Вывести все слова с заглавный буквы ( для этого мне нужно дать команду '/title'.)\n"
                                              "7) Вывести все слова в транслите на английском ( для этого мне нужно дать команду '/translit'.)\n"
                                              "8) Удалить историю запросов ( для этого мне нужно дать команду '/delete'.)\n"
                                              "9) Чтобы поменять строчку введите команду '/str'.\n"
                                              "10) Если запутались введите '/help'.")

@bot.message_handler(commands=['str'])
def get_str(message):

    if message.text=='/str':

        bot.send_message(message.from_user.id, "Напиши строчку которую нужно переделать")
        bot.register_next_step_handler(message, menu)

    else:
        menu(message)

@bot.message_handler(commands=['help'])
def help(message):

    bot.send_message(message.from_user.id," Чтобы ввести сообщение для переделывания мне нужно дать команду '/str').\n"
                                          "Чтобы узнать мои возможности введите команду '/menu').")

@bot.message_handler(commands=['caps'])
def caps(message):
    global string
    try:
        user = session.query(User).filter_by(tg_id=message.from_user.id).first()
        new_q = Quest(user_id=user.id, strTime=time.asctime(), operation='/caps', string=string)
        session.add(new_q)
        session.commit()
        bot.send_message(message.from_user.id, string.upper())
    except:
        bot.send_message(message.from_user.id,
                         'Вы не ввели текст для изменения введите команду /str и после этого вводите командуиз меню')

@bot.message_handler(commands=['low'])
def low(message):
    global string
    try:
        user = session.query(User).filter_by(tg_id=message.from_user.id).first()
        new_q = Quest(user_id=user.id, strTime=time.asctime(), operation=message.text, string=string)
        session.add(new_q)
        session.commit()
        bot.send_message(message.from_user.id, string.lower())
    except:
        bot.send_message(message.from_user.id,
                         'Вы не ввели текст для изменения введите команду /str и после этого вводите командуиз меню')

@bot.message_handler(commands=['letter'])
def letter(message):
    global string
    try:
        user = session.query(User).filter_by(tg_id=message.from_user.id).first()
        new_q = Quest(user_id=user.id, strTime=time.asctime(), operation=message.text, string=string)
        session.add(new_q)
        session.commit()
        bot.send_message(message.from_user.id, reletter(string))
    except:
        bot.send_message(message.from_user.id,
                         'Вы не ввели текст для изменения введите команду /str и после этого вводите командуиз меню')

@bot.message_handler(commands=['length'])
def length(message):
    global string
    try:
        user = session.query(User).filter_by(tg_id=message.from_user.id).first()
        new_q = Quest(user_id=user.id, strTime=time.asctime(), operation=message.text, string=string)
        session.add(new_q)
        session.commit()
        bot.send_message(message.from_user.id, len(string))
    except:
        bot.send_message(message.from_user.id,
                         'Вы не ввели текст для изменения введите команду /str и после этого вводите командуиз меню')

@bot.message_handler(commands=['title'])
def title(message):
    global string
    try:
        user = session.query(User).filter_by(tg_id=message.from_user.id).first()
        new_q = Quest(user_id=user.id, strTime=time.asctime(),operation=message.text,string=string )
        session.add(new_q)
        session.commit()
        bot.send_message(message.from_user.id, string.title())
    except: bot.send_message(message.from_user.id,
                             'Вы не ввели текст для изменения введите команду /str и после этого вводите командуиз меню')

@bot.message_handler(commands=['translit'])
def translit(message):
    global string
    try:
        user = session.query(User).filter_by(tg_id=message.from_user.id).first()
        new_q = Quest(user_id=user.id, strTime=time.asctime(),operation=message.text,string=string )
        session.add(new_q)
        session.commit()
        bot.send_message(message.from_user.id, transliteration(string))
    except: bot.send_message(message.from_user.id, 'Вы не ввели текст для изменения введите команду /str и после этого вводите командуиз меню')

@bot.message_handler(commands=['history'])
def history(message):
    user=session.query(User).filter_by(tg_id=message.from_user.id).first()

    que=session.query(Quest).filter_by(user_id=user.id).all()
    print(que)
    if que!=[]:
        for q in que:
            history=q.strTime,q.operation,q.string
            bot.send_message(user.tg_id,str(history))
    else:bot.send_message(user.tg_id,'Нет записей')


@bot.message_handler(commands=['delete'])
def deletee(message):
    user=session.query(User).filter_by(tg_id=message.from_user.id).first()
    que=session.query(Quest).filter_by(user_id=user.id).all()
    for q in que:
        session.delete(q)
    session.commit()
    bot.send_message(message.from_user.id,'Удалено')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    new_u = User(tg_id=message.from_user.id)
    session.add(new_u)
    session.commit()


    if message.text == "/start" or message.text.lower == "привет":
        print(message.from_user.id)
        bot.send_message(message.from_user.id,
                         "Привет я бот который может разнообразить твое сообщение.Если хочешь узнать все мои возможности напиши '/menu'.")
        bot.send_message(message.from_user.id, 'Введи сообщение которое нужно переделать')
        bot.register_next_step_handler(message, menu)

    else:bot.send_message(message.from_user.id, 'Напиши /start')


bot.polling(none_stop=True, interval=0)