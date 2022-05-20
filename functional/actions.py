from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.button import kb_main, kb_main2, kb_back, kb_cancel
from functional import base_menu as bm
from functional import base_menu_restaurant as bmr
from functional import order as od
from functional import feedback as fd
people = []

class FSMAdmin(StatesGroup):
    number = State()
    address = State()
    name = State()
    phone = State()
    wishes = State()
    
class FSMBack(StatesGroup):
    back = State()

async def send_welcome(message: types.Message):
    await message.reply("Hi I'm a food delivery bot.", reply_markup=kb_main2)
    print()
    print("Выполнена функция старта")
    
async def dopbutton(message: types.Message):
    await message.reply("Plese choose", reply_markup=kb_main)
    
async def main(message: types.Message):
    await message.reply("OK", reply_markup=kb_main2)
    
async def McDon(message: types.Message):
    text = [bm.selectTable()]
    
    text1 = text[0][0][0]
    text10 = text[0][0][1]
    text11 = text[0][0][2]
    
    text2 = text[0][1][0]
    text20 = text[0][1][1]
    text21 = text[0][1][2]
    
    text3 = text[0][2][0]
    text30 = text[0][2][1]
    text31 = text[0][2][2]
    
    text4 = text[0][3][0]
    text40 = text[0][3][1]
    text41 = text[0][3][2]
    
    text5 = text[0][4][0]
    text50 = text[0][4][1]
    text51 = text[0][4][2]
    
    await message.reply("Number for order: "+str(text1)+"\n"+"Dish: "+text10+"\n"+"Сompound: "+text11)
    await message.reply("Number for order: "+str(text2)+"\n"+"Dish: "+text20+"\n"+"Сompound: "+text21)
    await message.reply("Number for order: "+str(text3)+"\n"+"Dish: "+text30+"\n"+"Сompound: "+text31)
    await message.reply("Number for order: "+str(text4)+"\n"+"Dish: "+text40+"\n"+"Сompound: "+text41)
    await message.reply("Number for order: "+str(text5)+"\n"+"Dish: "+text50+"\n"+"Сompound: "+text51, reply_markup=kb_main2)
    
async def rest(message: types.Message):
    text = [bmr.selectTable()]
    
    text1 = text[0][0][0]
    text10 = text[0][0][1]
    text11 = text[0][0][2]
    
    text2 = text[0][1][0]
    text20 = text[0][1][1]
    text21 = text[0][1][2]
    
    text3 = text[0][2][0]
    text30 = text[0][2][1]
    text31 = text[0][2][2]
    
    text4 = text[0][3][0]
    text40 = text[0][3][1]
    text41 = text[0][3][2]
    
    text5 = text[0][4][0]
    text50 = text[0][4][1]
    text51 = text[0][4][2]
    
    await message.reply("Number for order : "+str(text1)+"\n"+"Dish: "+text10+"\n"+"Сompound: "+text11)
    await message.reply("Number for order : "+str(text2)+"\n"+"Dish: "+text20+"\n"+"Сompound: "+text21)
    await message.reply("Number for order : "+str(text3)+"\n"+"Dish: "+text30+"\n"+"Сompound: "+text31)
    await message.reply("Number for order : "+str(text4)+"\n"+"Dish: "+text40+"\n"+"Сompound: "+text41)
    await message.reply("Number for order : "+str(text5)+"\n"+"Dish: "+text50+"\n"+"Сompound: "+text51, reply_markup=kb_main2)
    
async def upload(message: types.Message):
    await FSMAdmin.number.set()
    await message.reply("Send 'Number for order' please", reply_markup=kb_cancel)
    people.clear
    
async def upnumber(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    await FSMAdmin.next()    
    people.append(message.text)
    await message.reply("Send address please", reply_markup=kb_cancel)
    
async def upaddress(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await FSMAdmin.next()
    people.append(message.text)
    await message.reply("Send your name please", reply_markup=kb_cancel)
    
async def upname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    people.append(message.text)
    await message.reply("Send number of your phone please", reply_markup=kb_cancel)
    
async def upphone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    people.append(message.text)
    await message.reply("Send your wishes please", reply_markup=kb_cancel)
    
async def upwishes(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['wishes'] = message.text
    people.append(message.text)
    await message.reply("Ok. We have received your order.", reply_markup=kb_main2)
    od.insertManyDataMode(people[0], people[1], people[2], people[3], people[4])
    print(od.selectTable())
    await state.finish()
   
async def feedback(message: types.Message):
    await FSMBack.back.set()
    await message.reply("Write your review please", reply_markup=kb_cancel)
        
async def upfeedback(message: types.Message, state: FSMContext):
    fls = [message.text]
    print(fls)
    fd.insertData(fls)
    print(fd.selectTable())
    await message.reply("Thank you for your feedback:)", reply_markup=kb_main2)
    await state.finish()
    fls.clear
    
async def phones(message: types.Message):
    help = ["78488487", "464841848", "3135484354", "4873265894", "2032564121"]
    await message.reply("Los Angeles: " + str(help[0]) + "\n" + 
                        "Moscow: " + str(help[1]) + "\n" + 
                        "Minsk: " + str(help[2]) + "\n" + 
                        "Pekin: " + str(help[3]) + "\n" + 
                        "Manaus:" + str(help[4]), reply_markup=kb_main2)

async def cancel(message: types.Message, state: FSMContext):
    print("test")
    current_state = await state.get_state()
    print(current_state)
    if current_state is None:
        await message.reply("OK", reply_markup=kb_main2)
        return
    await state.finish()
    print("test")
    await message.reply("OK", reply_markup=kb_main2)
    print("test")
        
def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cancel, Text(equals="Cancel", ignore_case=True), state='*')
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(dopbutton, Text(equals='Menu', ignore_case=True), state=None)
    dp.register_message_handler(main, Text(equals='Back', ignore_case=True), state=None)    
    dp.register_message_handler(McDon, Text(equals='McDonalds', ignore_case=True), state=None)
    dp.register_message_handler(rest, Text(equals='Restaurant', ignore_case=True), state=None)
    dp.register_message_handler(upload, Text(equals='Do order', ignore_case=True), state=None)
    dp.register_message_handler(upnumber, state=FSMAdmin.number)
    dp.register_message_handler(upaddress, state=FSMAdmin.address)
    dp.register_message_handler(upname, state=FSMAdmin.name)    
    dp.register_message_handler(upphone, state=FSMAdmin.phone)
    dp.register_message_handler(upwishes, state=FSMAdmin.wishes)
    dp.register_message_handler(feedback, Text(equals='Give feedback', ignore_case=True), state='*')
    dp.register_message_handler(upfeedback, state=FSMBack.back)
    dp.register_message_handler(phones, lambda message: message.text.startswith("Phones for help"))