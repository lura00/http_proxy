import pytest
from ..app import http_proxy
from requests import status_codes
# import sys
# sys.path.append('/./app/application/app/folder')

"""Unit tests for http_proxy.py 

import pytest to run pytest, requests to check status codes is correct

 run using pytest command, pytest -v (verbosity for more output"""

def test_status_code_ok():
    if http_proxy.MyProxy.do_GET == True:

        assert status_codes(200)