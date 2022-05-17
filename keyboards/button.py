from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

button_start = KeyboardButton('/start')

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start.add(button_start)

button_menu = KeyboardButton('Menu')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_menu.add(button_menu)

button_order = KeyboardButton('Do order')

kb_order = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_order.add(button_order)

button_feedback = KeyboardButton('Give feedback')

kb_feedback = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_feedback.add(button_feedback)

button_help = KeyboardButton('Phones for help')

kb_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_help.add(button_help)

button_cancel = KeyboardButton('Cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_cancel.add(button_cancel)

button_menu_mak = KeyboardButton('McDonalds')

kb_mak = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_mak.add(button_menu_mak)

button_menu_restaurant = KeyboardButton('Restaurant')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_main.add(button_menu_mak).add(button_menu_restaurant).add(button_cancel)

kb_main2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_main2.add(button_menu).add(button_order).add(button_feedback).add(button_help)