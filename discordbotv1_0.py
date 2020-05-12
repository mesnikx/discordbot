import requests
import random
import COVID19Py
import discord
import asyncio

TOKEN = 'NzA5NDQxOTQ4ODgwMDc2ODUw.Xrl-Qw.nUAIlMdnlGvsv2yoyikoNjftIKo'
covid19 = COVID19Py.COVID19()


class CovidBotClient(discord.Client):

    # def start_message(message):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    #     btn1 = types().KeyboardButton('Во всём мире')
    #     btn2 = types().KeyboardButton('США')
    #     btn3 = types().KeyboardButton('Россия')
    #     btn4 = types().KeyboardButton('Италия')
    #     btn5 = types().KeyboardButton('Не знаете чем себя занять на самоизоляции тыкните сюда)')
    #     btn6 = types().KeyboardButton('!info')
    #     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    #
    #     send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные пj коронавирусу напишите " \
    #                    f"название страны, например: США, Украина, Россия и так далее\n"
    #     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    async def on_message(self, message):
        if message.author == self.user:
            return
        final_message = ""
        get_message_bot = message.content.lower()
        if get_message_bot == 'абхазия':
            location = covid19.getLocationByCountryCode('AB')
        elif get_message_bot == 'австралия':
            location = covid19.getLocationByCountryCode('AU')
        elif get_message_bot == 'австрия':
            location = covid19.getLocationByCountryCode('AT')
        elif get_message_bot == 'азербайджан':
            location = covid19.getLocationByCountryCode('AZ')
        elif get_message_bot == 'алжир':
            location = covid19.getLocationByCountryCode('DZ')
        elif get_message_bot == 'ангола':
            location = covid19.getLocationByCountryCode('AO')
        elif get_message_bot == 'антарктида':
            location = covid19.getLocationByCountryCode('AQ')
        elif get_message_bot == 'аргентина':
            location = covid19.getLocationByCountryCode('AR')
        elif get_message_bot == 'армения':
            location = covid19.getLocationByCountryCode('AM')
        elif get_message_bot == 'афганистан':
            location = covid19.getLocationByCountryCode('AF')
        elif get_message_bot == 'багамы':
            location = covid19.getLocationByCountryCode('BS')
        elif get_message_bot == 'беларусь':
            location = covid19.getLocationByCountryCode('BY')
        elif get_message_bot == 'бельгия':
            location = covid19.getLocationByCountryCode('BE')
        elif get_message_bot == 'болгария':
            location = covid19.getLocationByCountryCode('BG')
        elif get_message_bot == 'боливия':
            location = covid19.getLocationByCountryCode('BO')
        elif get_message_bot == 'бразилия':
            location = covid19.getLocationByCountryCode('BR')
        elif get_message_bot == 'венгрия':
            location = covid19.getLocationByCountryCode('HU')
        elif get_message_bot == 'вьетнам':
            location = covid19.getLocationByCountryCode('VN')
        elif get_message_bot == 'германия':
            location = covid19.getLocationByCountryCode('DE')
        elif get_message_bot == 'гонконг':
            location = covid19.getLocationByCountryCode('HK')
        elif get_message_bot == 'гренландия':
            location = covid19.getLocationByCountryCode('GL')
        elif get_message_bot == 'греция':
            location = covid19.getLocationByCountryCode('GR')
        elif get_message_bot == 'грузия':
            location = covid19.getLocationByCountryCode('GE')
        elif get_message_bot == 'дания':
            location = covid19.getLocationByCountryCode('DK')
        elif get_message_bot == 'египет':
            location = covid19.getLocationByCountryCode('EG')
        elif get_message_bot == 'израиль':
            location = covid19.getLocationByCountryCode('IL')
        elif get_message_bot == 'индия':
            location = covid19.getLocationByCountryCode('IN')
        elif get_message_bot == 'индонезия':
            location = covid19.getLocationByCountryCode('ID')
        elif get_message_bot == 'ирак':
            location = covid19.getLocationByCountryCode('IQ')
        elif get_message_bot == 'иран':
            location = covid19.getLocationByCountryCode('IR')
        elif get_message_bot == 'испания':
            location = covid19.getLocationByCountryCode('ES')
        elif get_message_bot == 'италия':
            location = covid19.getLocationByCountryCode('IT')
        elif get_message_bot == 'казахстан':
            location = covid19.getLocationByCountryCode('KZ')
        elif get_message_bot == 'канада':
            location = covid19.getLocationByCountryCode('CA')
        elif get_message_bot == 'китай':
            location = covid19.getLocationByCountryCode('CN')
        elif get_message_bot == 'кипр':
            location = covid19.getLocationByCountryCode('CY')
        elif get_message_bot == 'куба':
            location = covid19.getLocationByCountryCode('CU')
        elif get_message_bot == 'латвия':
            location = covid19.getLocationByCountryCode('LV')
        elif get_message_bot == 'литва':
            location = covid19.getLocationByCountryCode('LT')
        elif get_message_bot == 'мадагаскар':
            location = covid19.getLocationByCountryCode('MG')
        elif get_message_bot == 'мальдивы':
            location = covid19.getLocationByCountryCode('MV')
        elif get_message_bot == 'мексика':
            location = covid19.getLocationByCountryCode('MX')
        elif get_message_bot == 'монголия':
            location = covid19.getLocationByCountryCode('MN')
        elif get_message_bot == 'нидерланды':
            location = covid19.getLocationByCountryCode('NL')
        elif get_message_bot == 'норвегия':
            location = covid19.getLocationByCountryCode('NO')
        elif get_message_bot == 'оаэ':
            location = covid19.getLocationByCountryCode('OM')
        elif get_message_bot == 'оман':
            location = covid19.getLocationByCountryCode('OM')
        elif get_message_bot == 'пакистан':
            location = covid19.getLocationByCountryCode('PK')
        elif get_message_bot == 'перу':
            location = covid19.getLocationByCountryCode('PE')
        elif get_message_bot == 'польша':
            location = covid19.getLocationByCountryCode('PL')
        elif get_message_bot == 'португалия':
            location = covid19.getLocationByCountryCode('PT')
        elif get_message_bot == 'россия':
            location = covid19.getLocationByCountryCode('RU')
        elif get_message_bot == 'румыния':
            location = covid19.getLocationByCountryCode('RO')
        elif get_message_bot == 'са':
            location = covid19.getLocationByCountryCode('SA')
        elif get_message_bot == 'сербия':
            location = covid19.getLocationByCountryCode('RS')
        elif get_message_bot == 'сингапур':
            location = covid19.getLocationByCountryCode('SG')
        elif get_message_bot == 'соединенное королевство':
            location = covid19.getLocationByCountryCode('GB')
        elif get_message_bot == 'сша':
            location = covid19.getLocationByCountryCode('US')
        elif get_message_bot == 'таджикистан':
            location = covid19.getLocationByCountryCode('TJ')
        elif get_message_bot == 'таиланд':
            location = covid19.getLocationByCountryCode('TH')
        elif get_message_bot == 'турция':
            location = covid19.getLocationByCountryCode('TR')
        elif get_message_bot == 'узбекистан':
            location = covid19.getLocationByCountryCode('UZ')
        elif get_message_bot == 'украина':
            location = covid19.getLocationByCountryCode('UA')
        elif get_message_bot == 'филиппины':
            location = covid19.getLocationByCountryCode('PH')
        elif get_message_bot == 'финляндия':
            location = covid19.getLocationByCountryCode('FI')
        elif get_message_bot == 'франция':
            location = covid19.getLocationByCountryCode('TR')
        elif get_message_bot == 'хорватия':
            location = covid19.getLocationByCountryCode('HR')
        elif get_message_bot == 'чехия':
            location = covid19.getLocationByCountryCode('CZ')
        elif get_message_bot == 'швейцария':
            location = covid19.getLocationByCountryCode('CH')
        elif get_message_bot == 'швеция':
            location = covid19.getLocationByCountryCode('SE')
        elif get_message_bot == 'япония':
            location = covid19.getLocationByCountryCode('JP')
        elif get_message_bot == 'эстония':
            location = covid19.getLocationByCountryCode('CH')
        elif get_message_bot == 'ямайка':
            location = covid19.getLocationByCountryCode('JM')
        else:
            location = covid19.getLatest()
            final_message = f"Данные по всему миру:\nЗаболевших: {location['confirmed']:,}\nСметрей: " \
                            f"{location['deaths']:,}"
        if final_message == "":
            date = location[0]['last_updated'].split("T")
            time = date[1].split(".")
            final_message = f"Данные по стране:\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n" \
                            f"Заболевших: {location[0]['latest']['confirmed']:,}\nСметрей: " \
                            f"{location[0]['latest']['deaths']:,}"

        await message.channel.send(final_message)


class RandomThings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='позже')
    async def set_timer(self, ctx, mes1, h, mes2, m, mes3):
        await ctx.send(" ".join(['Напишу через', mes1, h, mes2, m, mes3]))
        h = int(h)
        m = int(m)
        await asyncio.sleep(h * 3600 + m * 60)
        await ctx.send("Напиши страну и узнай как там дела с короновирусом")


bot = commands.Bot(command_prefix='*')
bot.add_cog(RandomThings(bot))
client = CovidBotClient()
client.run(TOKEN)
