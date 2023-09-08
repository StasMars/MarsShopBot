import random
import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6143871813:AAE2H0hoE7q9HZomhIn6ZlXxjXDsNrZ1ppU') # токен

answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # кнопки после команды 'start'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button2 = types.KeyboardButton('📍 Пункты выдачи')
    button3 = types.KeyboardButton('📄 Справка')
    
    markup.row(button1)
    markup.row(button2, button3)

    if message.text == '/start':
        # текст приветствия
        bot.send_message(message.chat.id, f'Добрый день, {message.from_user.first_name}!\nЗдесь вы можете ознакомиться с коллекцией товаров нашего магазина.\nПриятных вам покупок!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вы находитесь в главном меню. Приступайте к выбору товаров.', reply_markup=markup)

# Обработка фото. 
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'Данный бот не комментирует и не обрабатывает фотографии.')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        goodsChapter(message)
    elif message.text == '📍 Пункты выдачи':
        mapChapter(message)
    elif message.text == '📄 Справка':
        infoChapter(message)
    elif message.text == '▫️ Футболки':
        tshirtChapter(message)
    elif message.text == '▫️ Толстовки':
        hoodyChapter(message)
    elif message.text == '▫️ Брюки':
        trousersChapter(message)
    elif message.text == '▫️ Обувь':
        shoeChapter(message)

    #Футболки    
    elif message.text == '▫️ Envy Lab / Футболка(Черная)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Black_T.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Футболка</b>\nЦвет: черный\n\n<b><u>Цена: 999р</u></b>\n\nСостав:\nхлопок - 95%, лайкра - 5%\n\nОписание:\nОднотонная базовая футболка приталенного кроя с V образным вырезом и коротким рукавом. Посадка Super Slim Fit. Футболка сделана из высококачественного трикотажа.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Футболка(Белая)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\White_T.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Футболка</b>\nЦвет: белый\n\n<b><u>Цена: 999р</u></b>\n\nСостав:\nхлопок - 95%, лайкра - 5%\n\nОписание:\nОднотонная базовая футболка приталенного кроя с V образным вырезом и коротким рукавом. Посадка Super Slim Fit. Футболка сделана из высококачественного трикотажа.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Футболка(Красная)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Red_T.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Футболка</b>\nЦвет: красный\n\n<b><u>Цена: 999р</u></b>\n\nСостав:\nхлопок - 95%, лайкра - 5%\n\nОписание:\nОднотонная базовая футболка приталенного кроя с V образным вырезом и коротким рукавом. Посадка Super Slim Fit. Футболка сделана из высококачественного трикотажа.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Футболка(Синяя)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Blue_T.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Футболка</b>\nЦвет: синий\n\n<b><u>Цена: 999р</u></b>\n\nСостав:\nхлопок - 95%, лайкра - 5%\n\nОписание:\nОднотонная базовая футболка приталенного кроя с V образным вырезом и коротким рукавом. Посадка Super Slim Fit. Футболка сделана из высококачественного трикотажа.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Футболка(Розовая)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Pink_T.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Футболка</b>\nЦвет: розовый\n\n<b><u>Цена: 999р</u></b>\n\nСостав:\nхлопок - 95%, лайкра - 5%\n\nОписание:\nОднотонная базовая футболка приталенного кроя с V образным вырезом и коротким рукавом. Посадка Super Slim Fit. Футболка сделана из высококачественного трикотажа.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Футболка(Серая)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Gray_T.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Футболка</b>\nЦвет: серая\n\n<b><u>Цена: 999р</u></b>\n\nСостав:\nхлопок - 95%, лайкра - 5%\n\nОписание:\nОднотонная базовая футболка приталенного кроя с V образным вырезом и коротким рукавом. Посадка Super Slim Fit. Футболка сделана из высококачественного трикотажа.', parse_mode='html', reply_markup=markup)
    
    #Толсковки
    elif message.text == '▫️ Envy Lab / Толстовка (Черная)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Black_H.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Толстовка с капюшоном</b>\nЦвет: черный\n\n<b><u>Цена: 2999р</u></b>\n\nСостав:\nхлопок 95%, эластан 5%\n\nОписание:\nТолстовка худи приталенного кроя с капюшоном. Сделана из плотного футера. Хорошо сидит, приятная к телу. Высокая доля хлопка обеспечивает повышенную износостойкость материала. Ткань содержит эластан, за счет этого тянется, но не теряет форму после стрики.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Толстовка (Белая)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\White_H.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Толстовка с капюшоном</b>\nЦвет: белый\n\n<b><u>Цена: 2999р</u></b>\n\nСостав:\nхлопок 95%, эластан 5%\n\nОписание:\nТолстовка худи приталенного кроя с капюшоном. Сделана из плотного футера. Хорошо сидит, приятная к телу. Высокая доля хлопка обеспечивает повышенную износостойкость материала. Ткань содержит эластан, за счет этого тянется, но не теряет форму после стрики.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Толстовка (Красная)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Red_H.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Толстовка с капюшоном</b>\nЦвет: красный\n\n<b><u>Цена: 2999р</u></b>\n\nСостав:\nхлопок 95%, эластан 5%\n\nОписание:\nТолстовка худи приталенного кроя с капюшоном. Сделана из плотного футера. Хорошо сидит, приятная к телу. Высокая доля хлопка обеспечивает повышенную износостойкость материала. Ткань содержит эластан, за счет этого тянется, но не теряет форму после стрики.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Толстовка (Синяя)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Blue_H.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Толстовка с капюшоном</b>\nЦвет: синий\n\n<b><u>Цена: 2999р</u></b>\n\nСостав:\nхлопок 95%, эластан 5%\n\nОписание:\nТолстовка худи приталенного кроя с капюшоном. Сделана из плотного футера. Хорошо сидит, приятная к телу. Высокая доля хлопка обеспечивает повышенную износостойкость материала. Ткань содержит эластан, за счет этого тянется, но не теряет форму после стрики.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Толстовка (Серая)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Gray_H.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Толстовка с капюшоном</b>\nЦвет: серый\n\n<b><u>Цена: 2999р</u></b>\n\nСостав:\nхлопок 95%, эластан 5%\n\nОписание:\nТолстовка худи приталенного кроя с капюшоном. Сделана из плотного футера. Хорошо сидит, приятная к телу. Высокая доля хлопка обеспечивает повышенную износостойкость материала. Ткань содержит эластан, за счет этого тянется, но не теряет форму после стрики.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Envy Lab / Толстовка (Хаки)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Huky_H.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Envy Lab / Толстовка с капюшоном</b>\nЦвет: хаки\n\n<b><u>Цена: 2999р</u></b>\n\nСостав:\nхлопок 95%, эластан 5%\n\nОписание:\nТолстовка худи приталенного кроя с капюшоном. Сделана из плотного футера. Хорошо сидит, приятная к телу. Высокая доля хлопка обеспечивает повышенную износостойкость материала. Ткань содержит эластан, за счет этого тянется, но не теряет форму после стрики.', parse_mode='html', reply_markup=markup)
    
    #Обувь
    elif message.text == '▫️ Lacoste / Кеды(Белые)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Shoes.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Lacoste / Кеды(Белые)</b> \nЦвет: белый, хаки, светло-серый\n\n<b><u>Цена: 13999р</u></b>\n\nОписание:\nОписания пока нет. Возможно, оно появится тут позже.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Lacoste / Кеды(Черные)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Shoes_Black.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Lacoste / Кеды(Черные)</b> \nЦвет: черный\n\n<b><u>Цена: 11499р</u></b>\n\nОписание:\nОписания пока нет. Возможно, оно появится тут позже.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Lacoste / Кеды(Синии)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Shoes_Blue.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Lacoste / Кеды(Синии)</b> \nЦвет: темно-синий\n\n<b><u>Цена: 11499р</u></b>\n\nОписание:\nОписания пока нет. Возможно, оно появится тут позже.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Nike / Кеды / Blazer Mid(Черные)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Shoes_N_B.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Nike / Кеды / Blazer Mid(Черные)</b> \nЦвет: черный\n\n<b><u>Цена: 11499р</u></b>\n\nСостав:\nкожа 82%, Синтетические добавки 18%\n\nОписание:\nОписания пока нет. Возможно, оно появится тут позже.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ Nike / Кеды / Blazer Mid(Белые)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Shoes_N_W.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>Nike / Кеды / Blazer Mid(Белые)</b> \nЦвет: белый\n\n<b><u>Цена: 11499р</u></b>\n\nСостав:\nкожа 82%, Синтетические добавки 18%\n\nОписание:\nОписания пока нет. Возможно, оно появится тут позже.', parse_mode='html', reply_markup=markup)
    
    #Брюки
    elif message.text == '▫️ DENIM ELATiON / Брюки зауженные летние (Светлые)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Ths.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>DENIM ELATiON / Брюки зауженные летние светлые</b> \nЦвет: бело-серый\n\n<b><u>Цена: 2600р</u></b>\n\nОписание:\nЗауженные мужские брюки в клетку без стрелок! Клетка в швах не стыкуется! Брюки тонкие со средней посадкой, имеют два передних кармана, два задних прорезных кармана, застегиваются на пуговицу и молнию. Брюки мужские летние.', parse_mode='html', reply_markup=markup)
    elif message.text == '▫️ DENIM ELATiON / Брюки зауженные летние (Синии)':
        file1 = open('C:\Python\stepik\MarsShopBot\images\Ths_B.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад к товарам')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '<b>DENIM ELATiON / Брюки зауженные летние синии</b> \nЦвет: синий\n\n<b><u>Цена: 2600р</u></b>\n\nОписание:\nЗауженные мужские брюки в клетку без стрелок! Клетка в швах не стыкуется! Брюки тонкие со средней посадкой, имеют два передних кармана, два задних прорезных кармана, застегиваются на пуговицу и молнию. Брюки мужские летние.', parse_mode='html', reply_markup=markup)
   
    # Пункты выдачи
    elif message.text == '📍 ул. Гризодубовой, 4, Москва, 125252':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Показать на карте', url='https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%93%D1%80%D0%B8%D0%B7%D0%BE%D0%B4%D1%83%D0%B1%D0%BE%D0%B2%D0%BE%D0%B9,+4,+%D0%BA.+1,+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,+125252/@55.7831679,37.5259077,572m/data=!3m2!1e3!4b1!4m6!3m5!1s0x46b549988f4351db:0xcf2e011ab420c2d3!8m2!3d55.7831679!4d37.5284826!16s%2Fg%2F11pcpxxz28?entry=ttu')
        markup.row(btn1)
        bot.send_message(message.chat.id, '<b>Адрес:</b>  ул. Гризодубовой, 4, Москва, 125252\n<b>Время работы:</b>  Ежедневно, 10:00-20:00\n<b>Ближайшее Метро:</b>  ЦСКА', parse_mode='html', reply_markup=markup)
    elif message.text == '📍 Талалихина ул., 2/1 к5, Москва, 109147':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Показать на карте', url='https://www.google.com/maps/place/%D0%A2%D0%B0%D0%BB%D0%B0%D0%BB%D0%B8%D1%85%D0%B8%D0%BD%D0%B0+%D1%83%D0%BB.,+2%2F1,+%D0%BA5,+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,+109147/@55.7345245,37.6671265,2463m/data=!3m1!1e3!4m5!3m4!1s0x46b54ac459047537:0xff5f4775671cb24e!8m2!3d55.7375656!4d37.6759411?entry=ttu')
        markup.row(btn1)
        bot.send_message(message.chat.id, '<b>Адрес:</b>  Талалихина ул., 2/1 к5, Москва, 109147\n<b>Время работы:</b>  Ежедневно, 10:00-21:00\n<b>Ближайшее Метро:</b>  Пролетарская', parse_mode='html', reply_markup=markup)
    elif message.text == '📍 ул. Щепкина, 24, Москва, 129090':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Показать на карте', url='https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%A9%D0%B5%D0%BF%D0%BA%D0%B8%D0%BD%D0%B0,+24,+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,+129090/@55.777943,37.6233325,1274m/data=!3m1!1e3!4m6!3m5!1s0x46b54a7264faeaa5:0xfde0fe8e3b8fef99!8m2!3d55.7777429!4d37.6292548!16s%2Fg%2F11bw4j521q?entry=ttu')
        markup.row(btn1)
        bot.send_message(message.chat.id, '<b>Адрес:</b>  ул. Щепкина, 24, Москва, 129090\n<b>Время работы:</b>  Ежедневно, 10:00-20:00\n<b>Ближайшее Метро:</b>  Проспект мира', parse_mode='html', reply_markup=markup)
    elif message.text == '📍 4-й Добрынинский пер., Москва, 119049':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(' Показать на карте', url='https://www.google.com/maps/place/4-%D0%B9+%D0%94%D0%BE%D0%B1%D1%80%D1%8B%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9+%D0%BF%D0%B5%D1%80.,+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,+119049/@55.7266082,37.6106163,1547m/data=!3m1!1e3!4m6!3m5!1s0x46b54b103c5b23a7:0x387c2963b0ba42ca!8m2!3d55.7271534!4d37.6176116!16s%2Fg%2F1q67k02g1?entry=ttu')
        markup.row(btn1)
        bot.send_message(message.chat.id, '<b>Адрес:</b>  4-й Добрынинский пер., Москва, 119049\n<b>Время работы:</b>  Ежедневно, 11:00-21:00\n<b>Ближайшее Метро:</b>  Серпуховская', parse_mode='html', reply_markup=markup)
    elif message.text == '💳 Купить':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('(Ссылка на оплату товара)', url='https://t.me/stmarusin')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Оплатите товар.\nПосле оплаты товара с вами свяжется наш менеджер. Спасибо что выбираете нас.', reply_markup=markup)
    elif message.text == '✏️ Написать разработчику':
        btn1 = types.InlineKeyboardButton('Написать разработчику', url='https://t.me/stmarusin')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Используйте кнопку ниже, чтобы написать разработчику', reply_markup=markup)
    elif message.text == '↩️ Назад к товарам':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

# Функция, отвечающая за раздел всех товаров
def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('▫️ Футболки')
    button2 = types.KeyboardButton('▫️ Толстовки')
    button3 = types.KeyboardButton('▫️ Брюки')
    button4 = types.KeyboardButton('▫️ Обувь')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Здесь представлены все товары, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел футболок
def tshirtChapter(message):
    # Кнопки для футболок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('▫️ Envy Lab / Футболка(Черная)')
    button2 = types.KeyboardButton('▫️ Envy Lab / Футболка(Белая)')
    button3 = types.KeyboardButton('▫️ Envy Lab / Футболка(Красная)')
    button4 = types.KeyboardButton('▫️ Envy Lab / Футболка(Синяя)')
    button5 = types.KeyboardButton('▫️ Envy Lab / Футболка(Розовая)')
    button6 = types.KeyboardButton('▫️ Envy Lab / Футболка(Серая)')
    button7 = types.KeyboardButton('↩️ Назад к товарам')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Здесь представлены все модели футболок, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел толстовок
def hoodyChapter(message):
    # Кнопки для толстовок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('▫️ Envy Lab / Толстовка (Черная)')
    button2 = types.KeyboardButton('▫️ Envy Lab / Толстовка (Белая)')
    button3 = types.KeyboardButton('▫️ Envy Lab / Толстовка (Красная)')
    button4 = types.KeyboardButton('▫️ Envy Lab / Толстовка (Синяя)')
    button5 = types.KeyboardButton('▫️ Envy Lab / Толстовка (Серая)')
    button6 = types.KeyboardButton('▫️ Envy Lab / Толстовка (Хаки)')
    button7 = types.KeyboardButton('↩️ Назад к товарам')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Здесь представлены все модели толстовок, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел брюк
def trousersChapter(message):
    # Кнопки для брюк
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('▫️ DENIM ELATiON / Брюки зауженные летние (Светлые)')
    button2 = types.KeyboardButton('▫️ DENIM ELATiON / Брюки зауженные летние (Синии)')
    button3 = types.KeyboardButton('↩️ Назад к товарам')
    markup.row(button1, button2)
    markup.row(button3)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Здесь представлены все модели брюк, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел обуви
def shoeChapter(message):
    # Кнопки для обуви
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('▫️ Lacoste / Кеды(Белые)')
    button2 = types.KeyboardButton('▫️ Lacoste / Кеды(Черные)')
    button3 = types.KeyboardButton('▫️ Lacoste / Кеды(Синии)')
    button4 = types.KeyboardButton('▫️ Nike / Кеды / Blazer Mid(Черные)')
    button5 = types.KeyboardButton('▫️ Nike / Кеды / Blazer Mid(Белые)')
    button6 = types.KeyboardButton('↩️ Назад к товарам')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Здесь представлены все модели обуви, которые сейчас находятся в продаже:', reply_markup=markup)


# Функция, отвечающая за раздел пунктов выдачи 
def mapChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('📍 ул. Гризодубовой, 4, Москва, 125252')
    button2 = types.KeyboardButton('📍 Талалихина ул., 2/1 к5, Москва, 109147')
    button3 = types.KeyboardButton('📍 ул. Щепкина, 24, Москва, 129090')
    button4 = types.KeyboardButton('📍 4-й Добрынинский пер., Москва, 119049')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Все пункты выдачи товаров.\nВыберите самый удобный для вас.', reply_markup=markup)

# Функция, отвечающая за раздел справки
def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Написать разработчику', url='https://t.me/stmarusin')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Раздел справки.\nЕсли возникли какие-то пробелемы или товары не соответствуют указанным, можете отправить жалобу или оставить комментарий разработчику. Всегда рады обратной связи', reply_markup=markup)
    
# Строчка, чтобы программа не останавливалась
bot.polling(none_stop=True)