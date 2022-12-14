from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='๐ฏ Lavashlar',callback_data='lavash'),
            InlineKeyboardButton(text='๐ฑ Setlar',callback_data='set'),
        ],
        [
            InlineKeyboardButton(text='๐ฅ Xaggi',callback_data='xaggi'),
            InlineKeyboardButton(text='๐ฐ Shirinliklar',callback_data='shirinlik'),
        ],
        [
            InlineKeyboardButton(text='๐ Pitsalar',callback_data='pitsa'),
            InlineKeyboardButton(text='๐ฅช Klab Sendvich',callback_data='klab_sendvich'),
        ],
        [
            InlineKeyboardButton(text='๐ Burger va Donerlar',callback_data='burger_doner'),
            InlineKeyboardButton(text='๐ญ Hotdoglar',callback_data='hotdog'),
        ],
        [
            InlineKeyboardButton(text='๐ Sneklar',callback_data='snek'),
            InlineKeyboardButton(text='๐ฅ Salatlar',callback_data='salat'),
        ],
        [
            InlineKeyboardButton(text='๐ง Ichimliklar',callback_data='ichimlik'),
            InlineKeyboardButton(text='๐ Souslar',callback_data='sous'),
        ],
        [
            InlineKeyboardButton(text='๐ Buyurtmalar Tarixi',callback_data='tarix'),
        ],
        [
            InlineKeyboardButton(text='๐ Savatchaga o\'tish',callback_data='savatcha'),
        ]
    ],
)

check_box = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='โป๏ธ Tozalash',callback_data='delete_history')
        ],
        [
            InlineKeyboardButton(text='โฉ๏ธ Menuga o\'tish',callback_data='buyurtma')
        ]
    ]
)

buying = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='๐งพ Buyurtmani tasdiqlash',callback_data='enter_buy')
        ],
        [
            InlineKeyboardButton(text='Yana buyurtma berish',callback_data='buyurtma')
        ]
    ]
)

order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='๐ Yetkazib berish',callback_data='order_we'),
            InlineKeyboardButton(text='๐โโ๏ธ Olib ketish', callback_data='order_you'),

        ],
        [
            InlineKeyboardButton(text='๐ Ortga',callback_data='ortga')
        ],
    ],
)