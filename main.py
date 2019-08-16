import eurojackpot.draw
import eurojackpot.result
import eurojackpot.ticket
import lotto.draw
import lotto.result
import lotto.ticket

# Lotto

print('\n---Lotto----------------------------------\n')
lotto_tickets = lotto.ticket.get()
if lotto_tickets:
    lotto_draw = lotto.draw.get()
    for lotto_ticket in lotto_tickets:
        lotto_result = lotto.result.evaluate(lotto_draw, lotto_ticket)
        lotto.result.print_out(lotto_draw, lotto_ticket, lotto_result)
        print('\n------------------------------------------\n')

# Eurojackpot

print('\n---Eurojackpot----------------------------\n')
eurojackpot_tickets = eurojackpot.ticket.get()
if eurojackpot_tickets:
    eurojackpot_draw = eurojackpot.draw.get()
    for eurojackpot_ticket in eurojackpot_tickets:
        eurojackpot_result = eurojackpot.result.evaluate(
            eurojackpot_draw, eurojackpot_ticket)
        eurojackpot.result.print_out(eurojackpot_draw,
                                     eurojackpot_ticket,
                                     eurojackpot_result)
        print('\n------------------------------------------\n')
