from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboard_number import tanlanma_keyboard,list1
from keyboards.inline.lavash.lavash_kind import lavash_menu
from keyboards.inline.menu_keyboard import menu_keyboard
from loader import dp,db


@dp.callback_query_handler(text='pishloqli_lavash')
async def pishloqli_lavash(call:CallbackQuery,state:FSMContext):
     file = 'AgACAgIAAxkBAAM6Y2-mYDXeQMc9M8WAhLct5zvHpNoAApS_MRuihXhLpju5yr0F3_oBAAMCAAN5AAMrBA'
     await call.message.answer_photo(file, caption='<b>Pishloqli lavash</b>\n\nNarx:22000 so\'m\n'
                                                   'Iltimos kerakli miqdorni tanlang!', reply_markup=tanlanma_keyboard(0))
     list1.pop()
     await state.set_state('pishloqli_lavash')
     await call.message.delete()

@dp.callback_query_handler(state='pishloqli_lavash')
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
                    productname='Pishloqli lavash',
                    quantity=y,
                    price=22000
               )
          await call.answer("Buyurtmangiz qabul qilindi,davom etamizmi?",show_alert=True)
          file = 'AgACAgIAAxkBAAMaY0fwH5JoMlbLuFrAB9cWF_qyHGsAAk-_MRtq7UFK3AxrzMjwU-oBAAMCAAN5AAMqBA'
          await call.message.delete()
          await call.message.answer_photo(file, caption='<b>Birini Tanlang!</b>', reply_markup=menu_keyboard)
          await state.finish()
          list1.clear()
     elif call.data == 'orqaga':
         await call.message.delete()
         file = 'AgACAgIAAxkBAAMkY2-lEmXZgTAaN4PslS7Q42FhXEkAAoy_MRuihXhLerCeGCIy2PUBAAMCAAN5AAMrBA'
         await call.message.answer_photo(file, caption='<b>Birini Tanlang!</b>', reply_markup=lavash_menu)
         list1.clear()
         await state.finish()

     else:
          await call.message.edit_reply_markup(reply_markup=tanlanma_keyboard(data))
          await call.answer(cache_time=1)




