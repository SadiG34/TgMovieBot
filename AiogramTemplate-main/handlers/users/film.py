from aiogram import types
from requests import request
from aiogram.dispatcher.filters import Command
from loader import dp, bot, omdb_api_key


def create_response_message(response):
    message = f'<b>{response["Title"]}</b>\n' \
    f'Год выпуска: {response["Year"]}\n' \
    f'Рейтинг: <b>{response["imdbRating"]}</b>\n' \
    f'Длительность: {response["Runtime"]}\n' \
    f'Режиссер: {response["Director"]}\n' \
    f'Актеры: {response["Actors"]}'

    return message


# если сайт с api лег reguest поменять и в env поменять api
@dp.message_handler(Command('film'))
async def bot_film(message: types.Message):
    params = message.text.split()
    if len(params) == 1:
        await message.answer('Недостаточно параметров. \n'
                             'Примеры использования параметров:\n'
                             '1. /film название_фильма\n'
                             '2. /film название_фильма год_выпуска\n'
                             '3. /film imdb_код_фильма imdb\n')
        return

    elif len(params) == 2:
        if params[1][:5] == 'imdb_':
            request_URL = f'https://www.omdbapi.com/?apikey={omdb_api_key}&i={params[1][5:]}'
        else:
            request_URL = f'https://www.omdbapi.com/?apikey={omdb_api_key}&t={params[1]}'
    else:
        request_URL = f'https://www.omdbapi.com/?apikey={omdb_api_key}&t={params[1]}&y={params[2]}'
    response = request('GET', request_URL).json()
    if response["Response"] == "True":
        await message.answer(create_response_message(response))
    else:
        await message.answer(response["Error"])