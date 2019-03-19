def evaluate(draw, ticket):
    return [{'main': draw['main'].intersection(game['main']),
             'euro': draw['euro'].intersection(game['euro'])}
            for game in ticket]


def print_out(draw, ticket, common):
    print(f'Eurojackpot - {draw["date"]}')
    print()
    main = sorted(list(draw["main"]))
    euro = sorted(list(draw["euro"]))
    print(f'{main[0]:2d}, {main[1]:2d}, {main[2]:2d}, {main[3]:2d}, '
          f'{main[4]:2d} / {euro[0]:2d}, {euro[1]:2d}')
    print()
    i = 0
    while i < len(ticket):
        main_game = sorted(list(ticket[i]["main"]))
        euro_game = sorted(list(ticket[i]["euro"]))
        x = main_game + euro_game
        print(f'{x[0]:2d}, {x[1]:2d}, {x[2]:2d}, {x[3]:2d}, {x[4]:2d} '
              f'/ {x[5]:2d}, {x[6]:2d} '
              f'- [{len(common[i]["main"])}] / [{len(common[i]["euro"])}]')
        i += 1
