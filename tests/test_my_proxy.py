from pyparsing import empty
import pytest
from ..app import http_proxy
import requests
from urllib import request, response
from http import server
import sqlite3
import socketserver
# import unittest

# import sys
# sys.path.append('/./app/application/app/folder')

"""Unit tests for http_proxy.py 

import pytest to run pytest, requests to check status codes is correct

 run using pytest command, pytest -v (verbosity for more output"""


def test_setup_database():
    """ Fixture to set up the in-memory database with test data """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            http TEXT,
            www TEXT)''')
    cursor.execute("SELECT * FROM blocks;")
    data = cursor.fetchall()
    assert len(data) == 0
    conn.commit()
    conn.close()


def test_insert_data():
    """Test to insert data to db and checks that table on db contains data."""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            http TEXT,
            www TEXT)''')

    sample_data = [
        ('www.example.com', 'http://example.com')
    ]
    cursor.executemany('INSERT INTO blocks VALUES(NULL, ?, ?)', sample_data)
    cursor.execute("SELECT * FROM blocks;")
    data = cursor.fetchall()
    assert len(data) == 1


def test_server_connection():
    """Testing to connect to a http-domain, connection OK"""
    # url = 'http://example.com'
    # web = requests.get(url)
    # assert http_proxy.MyProxy(url).do_GET() == requests.status_code(200)
    # assert web.status_code == 200
    # PORT = 8000
    # proxies = http_proxy.MyProxy.do_GET()
    # httpd = socketserver.ForkingTCPServer(('', PORT), http_proxy.MyProxy)
    # print(httpd)
    session = requests.Session()

    session.proxies = {'http': 'http://127.0.0.1:8000'}

    url = 'http://example.com'

    response = session.get(url)

    assert response.status_code == 200

    # proxy = http_proxy.MyProxy.do_GET()
    # if proxy is True:

    #     url = requests.get('localhost:8000/http://example.com', proxies=proxy)
    #     assert url.status_code == 200
    # else:
    #     assert url.status_code == 400
    # # httpd.serve_forever()
    # # response = requests.get(url, proxies=httpd)
    # # print(response)
    # # proxy = http_proxy.httpd
    # response = requests.post(url, proxies=proxy)
    


def test_connect_to_blocked_website():
    """Test that tries to connect to a website that is blocked from db"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            http TEXT,
            www TEXT)''')
    sample_data = [
        ('www.example.com', 'http://example.com')
    ]
    cursor.executemany('INSERT INTO blocks VALUES(NULL, ?, ?)', sample_data)
    url = 'http://example.com'
    cursor.execute('SELECT * FROM blocks;')
    blocked_domain = cursor.fetchall()
    web = requests.get(url)
    if web in blocked_domain:
        requests.ConnectionError()
        assert web.status_code == 400