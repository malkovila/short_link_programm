import random
import string


def made_short_link(link):
    a = link.split('https://')
    letters = string.ascii_letters  # Получаем все латинские буквы
    linkk = ''.join(random.choice(letters) for _ in range(8))
    new_link = 'https://' + linkk

    res = []

    res.append(link)
    res.append(new_link)

    return res