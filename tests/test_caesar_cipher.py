from caesar_cipher import __version__
import caesar_cipher.caesar_cipher import *


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    expected = 'Wi xkwo sc Krwkn Crkvosx'
    actual = encrypt('My name is Ahmad Shalein', 10)
    assert actual == expected

def test_decrypt():
    expected = 'My name is Ahmad Shalein'
    actual = decrypt('Wi xkwo sc Krwkn Crkvosx', 10)
    assert actual == expected 

def test_crack():
    assert crack('Wi xkwo sc Krwkn Crkvosx') == 'My name is Ahmad Shalein'
