import datetime
import urllib.request

from helper import indices


def get():
    url = urllib.request.urlopen('https://www.lotto.de/eurojackpot')
    html = url.read()

    today = datetime.date.today()
    days_offset = (today.weekday() + 3) % 7
    last_friday = today - datetime.timedelta(days=days_offset)
    last_friday_text = datetime.datetime.strftime(last_friday, '%d.%m.%Y')
    last_friday_text = last_friday_text.encode()

    idxs = indices(html, b'<span class="WinningNumbers__date">')
    idxs = indices(html, b'<span class="LottoBall__circle">', idxs=idxs)
    idxs.sort()

    date = ''
    numbers = []

    for idx in idxs:
        idx_end = html.find(b'</span>', idx)
        text = html[idx:idx_end]
        if b'Freitag' in text:
            date = last_friday_text.decode('utf-8')
        if b'LottoBall__circle' in text:
            numbers.append(
                int(''.join(
                    i for i in text.decode('utf-8') if i.isdigit())))

    if len(numbers) == 7:
        return {
            'date': date,
            'main': frozenset(numbers[0:5]),
            'euro': frozenset(numbers[5:7])
        }

    return None
