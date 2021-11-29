import os
import sys
import inspect

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print(parentdir)
new_path = os.path.join(parentdir, "src", "ticketviewer")
sys.path.insert(1, new_path)

import pytest
import json
from ticketviewer import fetch_all_ticket, fetch_single_ticket, print_table
import yaml
import requests


#establishing session for testing
def req_session(token):
    with requests.Session() as s:
        s.headers.update(token)
        return s


with open('testing.yaml', 'r') as stream:
    data_loaded = yaml.safe_load(stream).split()

infourl = data_loaded[0].split('=')[1]
infotoken = {'Authorization': 'Basic {}'.format(data_loaded[1].split('=')[1])}
print(infotoken)

# client = req_session(infotoken)


# tests if all tickets methord is working fine
def test_all_tickets():
    assert fetch_all_ticket(req_session(infotoken), infourl,
                            navigator=False) == 0


# tests single tickets methord is working fine
def test_sing_tickets():
    assert fetch_single_ticket(req_session(infotoken), infourl + '/1') == 0


# tests if tabulate is working fine
def test_print_tickets():
    assert print_table([{
        'id': 1,
        'created_at': '20210809',
        'type': 'test',
        'subject': 'test',
        'priority': 'test',
        'status': 'test'
    }]) == 0


if __name__ == "__main__":
    pytest.main()