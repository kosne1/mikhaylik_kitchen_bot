import telebot
from datetime import datetime

website_url = 'https://crosspack.ru/'
phone_number = '+79295191725'

token = '5498020476:AAEs4HE5LoOLivhqb8OwQRvE5x54X04zY7Q'
bot = telebot.TeleBot(token)

main_markup = telebot.types.ReplyKeyboardMarkup(True, True)
main_markup.row('Правила чата', 'Частые вопросы')
main_markup.row('Перейти на сайт', 'Связь с оператором')

first_message = f"<b>Друзья, добрый день!</b>\n\n" \
                f"Хотим напомнить вам правила теплого, лампового чата — Михайлик kitchen.\n" \
                f'''Данный чат создан для открытого диалога с основателем кухни <a href="https://www.crosspack.ru/">Михайлик ''' \
                f"kitchen</a> — Денисом Михайликом.\n\n" \
                f"<b>Здесь мы предлагаем вам обсудить:</b>\n\n" \
                f"▫️Предложения по разнообразию меню;\n" \
                f"▫️ Изменения по имеющимся блюдам (например: «добавьте больше сахара» , " \
                f"«уберите из блюда соль» и т. д.);\n" \
                f"▫️ Какие блюда Вы хотели бы видеть в акциях;\n" \
                f"▫️ Лайфхаки по готовке/ хранению блюд;\n" \
                f"▫️ Здесь мы показываем производство и рассказываем о новинках.\n\n" \
                f"❌ Для оперативности решения вопросов в нашем чате нежелательны " \
                f"обсуждение и вопросы по поводу конкретного заказа, для этого есть бизнес" \
                f" чат в WhatsApp +79295191725.\n\n" \
                f"Наши операторы рады будут помочь Вам разобраться в Вашем вопросе " \
                f"ежедневно с 09:00 до 21:00.\n\n" \
                f"❌ Кроме недельных промокодов, которые выходят КАЖДЫЙ вторник в нашем ТГ " \
                f"канале запрещено указывать личные и сторонние промокоды.\n" \
                f"<i>PS. Промокоды действуют со вторника по четверг включительно!</i>\n\n" \
                f"▫️ Если вы хотите оформить заказ на завтра, то советуем оформить его " \
                f"до 13:00 текущего дня <i>(актуально для соответствующих зон, подробнее " \
                f'''смотрите на нашем <a href="https://www.crosspack.ru/">сайте</a>)</i>\n\n''' \
                f"Для комфортного общения нам пришлось ввести ряд несложных правил, " \
                f"которые помогут нам стать лучше.\n" \
                f"При первом нарушении выносится предупреждение, при втором — <b>бан</b> 🚫\n\n" \
                f"Спасибо за понимание, мы желаем Вам хорошего дня и приятного аппетита!\n" \
                f"А еще проверьте, что вы вмсете с нами в чате: https://t.me/+W_JnPZ-iOUY3MTgy\n\n" \
                f"С уважением,\n" \
                f"<i>команда Михайлик</i> kitchen 🧡"


@bot.message_handler(commands=['start'])
def start(message):
    try:
        f = open('logger.txt', 'a')
        f.write(f"[INFO {datetime.now()}] user {message.from_user.id} start session with bot\n")
        bot.send_message(message.chat.id, "Hello", reply_markup=main_markup)
    except Exception as _ex:
        f.write(f"[ERROR {datetime.now()}] {_ex} with user {message.from_user.id} \n")
    finally:
        f.close()


@bot.message_handler(content_types=['text'])
def button_response(message):
    try:
        f = open('logger.txt', 'a')
        f.write(f"[INFO {datetime.now()}] user {message.from_user.id} write message: {message.text}\n")
        if message.text == 'Правила чата':
            bot.send_message(message.chat.id, first_message, parse_mode='html')
        if message.text == 'Частые вопросы':
            user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
            user_markup.row('КАК ДОЛГО ХРАНИТСЯ ЕДА Михайлик Kitchen?')
            user_markup.row('ККАЛ НА ПОРЦИЮ ИЛИ НА 100ГР?')
            user_markup.row('ЗАЧЕМ УБРАЛИ ЭТО БЛЮДО?')
            user_markup.row('НОВЫЙ БОКС ДЛЯ САЛАТА — НЕУДОБНЫЙ!')
            user_markup.row('ПОЧЕМУ ПЛЕНКА ТАК ПЛОХО ОТРЫВАЕТСЯ?')
            user_markup.row('ЕСТЬ ЛИ У ВАС НАБОРЫ?')
            user_markup.row('МОЖНО ЛИ СДАВАТЬ КОНТЕЙНЕРЫ?')
            user_markup.row('МОЖНО ЛИ ЗАМОРАЖИВАТЬ ВАШИ БЛЮДА?')
            user_markup.row('У МЕНЯ ЕСТЬ КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ.')
            # user_markup.row('ВЕРНУТЬСЯ НАЗАД')
            bot.send_message(message.chat.id, "Выберите интересующий вас вопрос", reply_markup=user_markup)
        if message.text == 'Перейти на сайт':
            bot.send_message(message.chat.id, f"Переходите на наш сайт по ссылке:\n\n"
                                              f"{website_url}")
        if message.text == 'Связь с оператором':
            bot.send_message(message.chat.id,
                             f"Для перехода в чат с оператором просто нажмите ссылку 👉 https://api.whatsapp.com/send/?phone=79295191725&text&app_absent=0")
        if message.text == 'КАК ДОЛГО ХРАНИТСЯ ЕДА Михайлик Kitchen?':
            bot.send_message(message.chat.id, "При соблюдении температурного режима, который указан на упаковке. "
                                              "Готовые блюда быстро охлаждаются до +1/+4 градусов и упаковываются в "
                                              "газомодифицированной среде. Благодаря этому свежесть сохраняется 5 суток."
                                              "\nКроме пирожных и сендвичей в крафтовой упаковке.",
                             reply_markup=main_markup)
        if message.text == 'ККАЛ НА ПОРЦИЮ ИЛИ НА 100ГР?':
            bot.send_message(message.chat.id, "На порцию.\nМы позаботились о вас, поэтому на этикетках находится КБЖУ "
                                              "не только на 100гр, но и на всю порцию!", reply_markup=main_markup)
        if message.text == 'ЗАЧЕМ УБРАЛИ ЭТО БЛЮДО?':
            bot.send_message(message.chat.id, "В нашем меню более 130 позиций.\nКаждое 15-ое число мы добавляем и "
                                              "убираем по 4-6 позиций.\n\n"
                                              "Обращаем ваше внимание, что наша кухня НЕ является собранным рационом, "
                                              "для этого у нас есть раздел «наборы» по КБЖУ.\n\n"
                                              "Ежедневно мы готовим все 130 позиций в больших количествах и следим за "
                                              "качеством всех продуктов, поэтому для меню работает демократический "
                                              "принцип большинства. Мы не можем добавлять ваши любимые позиции, если их "
                                              "заказывают 10 человек, наравне с блюдами, которые заказывают "
                                              "тысячи людей.\n\n"
                                              "Мы за выбор и простоту с отменным качеством!\n\n"
                                              "Но мы всегда рады вашим предложениям в нашем теплом, ламповом чате. "
                                              "Мы их непременно рассмотрим.", reply_markup=main_markup)
        if message.text == 'НОВЫЙ БОКС ДЛЯ САЛАТА — НЕУДОБНЫЙ!':
            bot.send_message(message.chat.id, "Мы обновили боксы, чтобы блюда, у которых есть соус, было легко "
                                              "доставать и перемешивать.\nУчитывая вашу обратную связь, в скором "
                                              "времени мы поменяем эти боксы на более глубокие.",
                             reply_markup=main_markup)
        if message.text == 'ПОЧЕМУ ПЛЕНКА ТАК ПЛОХО ОТРЫВАЕТСЯ?':
            bot.send_message(message.chat.id, "К сожалению, решить проблему с ровным и легким открытием пленки "
                                              "может только ее поставщик — здесь мы зависимы от него. Проблема в "
                                              "сырье, из которого делают пленку, на рынке все страдают от этого.\n\n"
                                              "Мы за герметичность и за то, чтобы наши продукты сохраняли свои "
                                              "свойства — 5 суток.\n\n"
                                              "Но как только сырья на рынке станет больше, пленку будет лучшего "
                                              "качества.\nИ мы обязательно поэкспериментируем с новыми пленками.\n\n"
                                              "Спасибо за понимание.", reply_markup=main_markup)
        if message.text == 'ЕСТЬ ЛИ У ВАС НАБОРЫ?':
            bot.send_message(message.chat.id, "Да, кончено!\n"
                                              "На нашем сайте вы можете выбрать необходимый для вас набор с "
                                              "определенным количеством ккал:\n"
                                              "⁃ 1.200 ккал\n"
                                              "⁃ 1.500 ккал\n"
                                              "⁃ 1.800 ккал\n"
                                              "⁃ 2.000 ккал\n"
                                              "⁃ 2.200 ккал\n"
                                              "А также хотим обратить ваше внимание, что каждый набор собран по "
                                              "трем вариантам, чтобы вам не наскучили блюда.",
                             reply_markup=main_markup)
        if message.text == 'МОЖНО ЛИ СДАВАТЬ КОНТЕЙНЕРЫ?':
            bot.send_message(message.chat.id, "Да, наши контейнеры можно сдавать на переработку, для этого "
                                              "необходимо снять пленку и сполоснуть контейнер водой.\n"
                                              "Мы не занимаемся сбором и переработкой пластика от покупателей, "
                                              "т. к. для этого пришлось бы отправлять отдельную машину. В машине с "
                                              "едой мусор возить нельзя.", reply_markup=main_markup)
        if message.text == 'МОЖНО ЛИ ЗАМОРАЖИВАТЬ ВАШИ БЛЮДА?':
            bot.send_message(message.chat.id, "Мы не проводили таких тестирований\n"
                                              "(но клиенты говорят, что можно 🙃)", reply_markup=main_markup)
        if message.text == 'У МЕНЯ ЕСТЬ КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ.':
            bot.send_message(message.chat.id, "Присылайте ваши коммерческие предложения и идеи по сотрудничеству "
                                              "на нашу корпоративную почту: info@crosspack.ru\n\n"
                                              "Мы каждый день просматриваем заявки, и если они интересные — отвечаем.",
                             reply_markup=main_markup)
        # if message.text == 'ВЕРНУТЬСЯ НАЗАД':
        #     bot.send_message(message.chat.id, '\n', reply_markup=main_markup)
    except Exception as _ex:
        f.write(f"[ERROR {datetime.now()}] {_ex}\n")
    finally:
        f.close()


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    try:
        f = open('logger.txt', 'a')
        f.write(f"[INFO {datetime.now()}] added new user {message.from_user.id} to chat\n")
        bot.send_message(message.chat.id, f"Добро пожаловать, {message.from_user.username}\n\n"
                                          f"Не забудьте ознакомиться с закреплённым сообщением: "
                                          f'''<a href="https://t.me/mikhaylik_kitchen/156">ссылка на правила</a>\n\n'''
                                          f"Приятного общения ☺", parse_mode='html', reply_markup=main_markup)
    except Exception as _ex:
        f.write(f"[ERROR {datetime.now()}] {_ex}\n")
    finally:
        f.close()


bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота")
])

bot.set_chat_menu_button()

bot.polling(none_stop=True)
