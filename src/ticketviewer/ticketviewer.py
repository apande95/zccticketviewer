import requests
from base64 import b64encode
import json
from config import ZENDESK
from pprint import pprint
from tabulate import tabulate


#error handling TBD
class Fails(Exception):
    pass


# establishing session
def req_session():
    with requests.Session() as s:
        s.headers.update(ZENDESK['HEADERS'])
        return s


#Prints tabulated json objects
def print_table(tickets):
    # print(tickets)
    # print(len(tickets))
    #because of space contraints in a terminal, the following columns are the only ones displayed.
    try:
        keys = ['id', 'created_at', 'type', 'subject', 'priority', 'status']
        #using the same function for single and multiple tickets
        reduced_tickets = []
        for i in tickets:
            reduced_tickets.append([i[x] for x in keys])
        print(tabulate(reduced_tickets, headers=keys, tablefmt='pipe'))
        return 0
    except:
        print('\nError Tabulating\n')
        return 1


#fetch all tickets with pagination
def fetch_all_ticket(s, url, navigator=False):
    try:
        resp = s.get(url, params=ZENDESK['PARAMS'])
        if 'error' in resp.json():
            raise Fails(resp.json()['error'])
        print_table(resp.json()['tickets'])
        next = resp.json()['links']['next']
        prev = resp.json()['links']['prev']
        if not navigator:
            return 0
        if int(resp.json()['tickets'][0]['id']) == 1:
            prev = None
        display = ''
        if prev:
            display += '\nPress 1 to move one page back'
        if next:
            display += '\nPress 2 to move one page forward'
        display += '\nPress 3 to quit back to main interface'
        if not prev and not next:
            print('\nReached the END :) Reverting to main menu...\n')
            return 0
        navigation = int(input(display + '\n'))
        if navigation not in (1, 2, 3):
            raise Fails('Invalid page navigation movement\n')
        elif navigation == 1:
            fetch_all_ticket(s, prev,navigator=True)
        elif navigation == 2:
            fetch_all_ticket(s, next,navigator=True)
        elif navigation == 3:
            return 0
    except Exception as e:
        print()
        print('Error Fetching Tickets from Zendesk :', url, '\n', str(e))
        return 1


#fetch single ticket with ID that is supplied
def fetch_single_ticket(s, url):
    try:
        resp = s.get(url)
        if 'error' in resp.json():
            raise Fails(resp.json()['error'])
        print_table([resp.json()['ticket']])
        return 0
    except BaseException as e:
        print()
        print('Error Fetching Tickets from Zendesk :', url, '\n', str(e))
        return 1


#main CLI Loop
def main():
    s = req_session()
    while True:
        inp = input(
            '\nPress 1 for all tickets\nPress 2 for individual ticket\nPress 3 to fetch no. of tickets\nPress 4 to quit\n'
        )
        try:
            choice = int(inp)
            if choice not in (1, 2, 3, 4):
                raise Fails('choice not correct')
            elif choice == 1:
                fetch_all_ticket(s,
                                 ZENDESK['CLIENT_URL'] +
                                 ZENDESK['TICKETS_URL'],
                                 navigator=True)
            elif choice == 2:
                ticket_id = input('\nPlease insert ticket ID\n')
                ticket_id = int(
                    ticket_id)  # will throw error in case non int provided
                ticket_str = '/' + str(ticket_id)  # converting back to str
                fetch_single_ticket(
                    s, ZENDESK['CLIENT_URL'] + ZENDESK['TICKETS_URL'] +
                    ticket_str)
            elif choice == 3:
                break
            elif choice == 4:
                break
        except Exception as e:
            print('Error in input :', str(e))
            pass


if __name__ == '__main__':
    main()