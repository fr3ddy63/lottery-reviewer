import datetime
import urllib

from helper import indices


def get():
    url = urllib.request.urlopen('https://www.lotto.de/lotto-6aus49')
    html = url.read()

    today = datetime.date.today()
    days_offset = (today.weekday() + 2) % 7
    last_saturday = today - datetime.timedelta(days=days_offset)
    last_saturday_text = datetime.datetime.strftime(last_saturday, '%d.%m.%Y')
    last_saturday_text = last_saturday_text.encode()

    idxs = indices(html, b'<span class="WinningNumbers__date">')
    idxs = indices(html, b'<span class="LottoBall__circle">', idxs=idxs)
    idxs = indices(
        html,
        b'<span class="WinningNumbersAdditionalGame__placeholder">Spiel 77',
        idxs=idxs)
    idxs = indices(
        html,
        b'<span class="WinningNumbersAdditionalGame__placeholder">Super 6',
        idxs=idxs)
    idxs.sort()

    date = ''
    numbers_saturday = False
    numbers = []
    number_spiel77 = ''
    number_super6 = ''

    for idx in idxs:
        idx_end = html.find(b'</span>', idx)
        text = html[idx:idx_end]
        if b'Samstag' in text and last_saturday_text in text:
            date = last_saturday_text.decode('utf-8')
            numbers_saturday = True
        if b'Mittwoch' in text:
            numbers_saturday = False
        if b'LottoBall__circle' in text and numbers_saturday:
            numbers.append(
                int(''.join(
                    i for i in text.decode('utf-8') if i.isdigit())))
        if b'Spiel 77' in text and numbers_saturday:
            idx_end_number = html.find(b'</span>', idx_end + 7)
            number_spiel77 = ''.join(
                i for i in html[idx_end:idx_end_number].decode('utf-8')
                if i.isdigit())
        if b'Super 6' in text and numbers_saturday:
            idx_end_number = html.find(b'</span>', idx_end + 7)
            number_super6 = ''.join(
                i for i in html[idx_end:idx_end_number].decode('utf-8')
                if i.isdigit())

    if (len(numbers) == 7
            and len(number_spiel77) == 7
            and len(number_super6) == 6):
        number_super = numbers[-1]
        numbers = numbers[0:6]
        return {
            "date": date,
            "numbers": numbers,
            "supernumber": number_super,
            "spiel77": number_spiel77,
            "super6": number_super6}

    return None
