#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    API Endpointin HTTP durum kodu 200 ise 'başarılı'; degilse 'başarısız' olarak raporlar.
"""

__version__ = '1.0'
__author__ = 'Pinar Karga'

from requests import get, exceptions
from logging import basicConfig, info, error, warning
from urllib.parse import urlparse

# HTTP yaniti 200 ise 'başarılı'; degilse 'başarısız' olarak doner.
def is_http_ok(uri):
    try:
        get_response = get(uri)
        return 'başarılı' if (get_response.status_code == 200) else 'başarısız'
    except exceptions.Timeout:
        warning('Timeout')
    except exceptions.TooManyRedirects:
        warning('Too many redirections')
    except exceptions.RequestException as e:
        error('Request exception'+str(e))

# uri dogrulama 
def check_uri(uri):
    try:
        parsed_uri = urlparse(uri)
        return all([parsed_uri.scheme, parsed_uri.netloc])
    except:
        return False

# Kullanicidan uri girdisi alir.
def get_uri():
    try:
        uri = input("Lutfen uri girin: ")
        if not uri:
            raise ValueError('Girdi bos')
    except ValueError:
        error("Deger Hatali")
    return uri

if __name__ == '__main__':
    basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    info('HTTP Status Code Tester Started')
    uri = "http://generator.swagger.io/api/swagger.json"
    # uri = get_uri() # kullanicidan girdi olarak.
    assert check_uri(uri),"URI hatali"
    print(is_http_ok(uri))
