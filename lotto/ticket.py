import json

import config


def get() -> list:
    tickets = []
    ticket_files = list(config.tickets_path.glob('lotto-*'))
    for ticket_file in ticket_files:
        with open(ticket_file, 'r') as file:
            tickets.append(json.load(file))
    return tickets
