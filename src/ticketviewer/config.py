# configs
import os

ZENDESK = {
    'CLIENT_URL': os.environ.get('URL'),
    'TOKEN': os.environ.get('TOKEN'),
    'HEADERS': {
        'Authorization': 'Basic {}'.format(os.environ.get('TOKEN'))
    },
    'PARAMS': {
        'page[size]': 25
    },
    'PAGE_START': 0,
    'TICKETS_URL': '/api/v2/tickets',
    'TICKETS_COUNT_URL': '/api/v2/tickets/count'
}