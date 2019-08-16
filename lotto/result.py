def evaluate_ticket_number(ticket_number, subgame_number):
    tn = ticket_number[::-1]
    sgn = subgame_number[::-1]
    counter = 0
    i = 0
    while i < len(sgn):
        if tn[i] == sgn[i]:
            counter += 1
        else:
            break
        i += 1
    return counter


def evaluate(draw, ticket):
    result = {'common': [], 'sn': False, 'Spiel77': 0, 'Super6': 0}
    draw_numbers = set(draw['numbers'])
    for game in ticket['games']:
        game_number = set(game)
        result['common'].append(list(game_number.intersection(draw_numbers)))
    result['sn'] = int(ticket['ticket_number'][-1]) == draw['supernumber']
    result['Spiel77'] = evaluate_ticket_number(
        ticket['ticket_number'],
        draw['spiel77'])
    result['Super6'] = evaluate_ticket_number(
        ticket['ticket_number'],
        draw['super6'])
    return result


def print_out(draw, ticket, common):
    print(f'Lotto - {draw["date"]}')
    print()
    print('draw: '
          f'{draw["numbers"][0]:2d}, {draw["numbers"][1]:2d}, '
          f'{draw["numbers"][2]:2d}, {draw["numbers"][3]:2d}, '
          f'{draw["numbers"][4]:2d}, {draw["numbers"][5]:2d}')
    print(f'supernumber: {draw["supernumber"]}')
    print()
    i = 0
    while i < len(ticket['games']):
        print(
          f'{ticket["games"][i][0]:2d}, {ticket["games"][i][1]:2d}, '
          f'{ticket["games"][i][2]:2d}, {ticket["games"][i][3]:2d}, '
          f'{ticket["games"][i][4]:2d}, {ticket["games"][i][5]:2d} / '
          f'{common["common"][i]}')
        i += 1
    print()
    print(f'ticket number: {ticket["ticket_number"]}')
    print()
    print(f'super number: {common["sn"]}')
    print(f'Spiel77: {draw["spiel77"]} - {common["Spiel77"]}')
    print(f'Super6: {draw["super6"]} - {common["Super6"]}')
