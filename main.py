import eurojackpot.draw
import eurojackpot.result
import eurojackpot.ticket
import lotto.draw
import lotto.result
import lotto.ticket

lotto_tickets = lotto.ticket.get()
if not lotto_tickets:
    pass
else:
    lotto_draw = lotto.draw.get()
    for lotto_ticket in lotto_tickets:
        lotto_result = lotto.result.evaluate(lotto_draw, lotto_ticket)
        lotto.result.print_out(lotto_draw, lotto_ticket, lotto_result)

eurojackpot_tickets = eurojackpot.ticket.get()
if not eurojackpot_tickets:
    pass
else:
    eurojackpot_draw = eurojackpot.draw.get()
    for eurojackpot_ticket in eurojackpot_tickets:
        eurojackpot_result = eurojackpot.result.evaluate(
            eurojackpot_draw, eurojackpot_ticket)
        eurojackpot.result.print_out(eurojackpot_draw,
                                     eurojackpot_ticket,
                                     eurojackpot_result)
        print('\n------------------------------------------\n')
