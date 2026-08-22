from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



#######inline_start######
inline_start_button = InlineKeyboardButton(text="شروع فرمانروایی 🤴🏻", callback_data="register", style="danger")
inline_start_markup = InlineKeyboardMarkup(inline_keyboard=[[inline_start_button]])

#######inline_confirm_country-name######
inline_confirm_country_name = InlineKeyboardButton(text="تایید ✅", callback_data="confirm_country_name", style="success")
inline_edit_country_name = InlineKeyboardButton(text="ویرایش ✏️", callback_data="edit_country_name", style="danger")
inline_confirmandedit_country_name = InlineKeyboardMarkup(inline_keyboard=[[inline_confirm_country_name],[inline_edit_country_name]])
