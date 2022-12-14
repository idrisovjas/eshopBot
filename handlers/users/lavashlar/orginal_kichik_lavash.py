from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboard_number import tanlanma_keyboard,list1
from keyboards.inline.lavash.lavash_kind import lavash_menu
from keyboards.inline.menu_keyboard import menu_keyboard
from loader import dp,db


@dp.callback_query_handler(text='orginal_kichik_lavash')
async def orginal_lavash_kichik(call:CallbackQuery,state:FSMContext):
     file = 'AgACAgIAAxkBAAMyY2-l-Xj5i8NmIIrSynDXh3p8aK4AApK_MRuihXhLt-_DeAR0nCkBAAMCAAN5AAMrBA'
     await call.message.answer_photo(file, caption='<b>Orginal kichik lavash</b>\n\nNarx:22000 so\'m\n'
                                                   'Iltimos kerakli miqdorni tanlang!', reply_markup=tanlanma_keyboard(0))

     await state.set_state('orginal_kichik_lavash')
     await call.message.delete()
     list1.clear()

@dp.callback_query_handler(state='orginal_kichik_lavash')
async def orginal_lavash_state(call:CallbackQuery,state:FSMContext):
     data = call.data
     y=''
     if len(list1)==0 and data=='joylash':
          await call.answer(text='Siz hech qancha mahsulot tanlamadingiz!',show_alert=True)
     elif data=='joylash' and len(list1)!=0:
          for i in list1:
               y+=str(i)
          y = int(y)
          db.add_product(
                    id=call.from_user.id,
                    name=call.from_user.full_name,
                    productname='Orginal kichik lavash',
                    quantity=y,
                    price=22000
               )
          await call.answer("Buyurtmangiz qabul qilindi,davom etamizmi?",show_alert=True,cache_time=2)
          await call.message.delete()
          await call.message.answer(text='<b>Davom etamizmi?😊</b>',reply_markup=menu_keyboard)
          await state.finish()
          list1.clear()
     elif call.data == 'orqaga':
         await call.message.delete()
         file = 'AgACAgIAAxkBAAMkY2-lEmXZgTAaN4PslS7Q42FhXEkAAoy_MRuihXhLerCeGCIy2PUBAAMCAAN5AAMrBA'
         await call.message.answer_photo(file, caption='<b>Birini Tanlang!😊</b>', reply_markup=lavash_menu)
         list1.clear()
         await state.finish()

     else:
          await call.message.edit_reply_markup(reply_markup=tanlanma_keyboard(data))
          await call.answer(cache_time=1)


@dp.callback_query_handler(text='ortga')
async def ortga_def_state(call:CallbackQuery,state:FSMContext):
         await call.message.delete()
         await call.message.answer(text='<b>Davom etamizmi?😊</b>', reply_markup=menu_keyboard)
         list1.clear()
         await state.finish()