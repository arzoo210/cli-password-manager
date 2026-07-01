import pytest
import os
from crypto_utils import encrypt, decrypt, generate_key, KEY_FILE
from storage import add_entry, get_entry, delete_entry, list_services, DATA_FILE

@pytest.fixture(autouse=True)
def clean():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    if not os.path.exists(KEY_FILE):
        generate_key()
    yield
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_encrypt_decrypt():
    original = "secret123"
    token = encrypt(original)
    result =decrypt(token)
    assert result == original

def test_encrypt_produces_diffoutput():
    original = "secret123"
    token = encrypt(original)
    assert token != original

def test_addgetentry():
    add_entry("gmail", "arzoo123", encrypt("mypassword"))
    entry = get_entry("gmail")
    assert entry is not None
    assert entry["username"] =="arzoo123"
    assert decrypt(entry["password"]) == "mypassword"

def test_listservices():
    add_entry("gmail", "arzoo123", encrypt("password1"))
    add_entry("github", "arzoo210", encrypt("password2"))
    services =list_services()
    assert "gmail" in services
    assert "github" in services

def test_deleteentry():
     add_entry("gmail", "arzoo123", encrypt("password1"))
     result = delete_entry("gmail")
     assert result == True
     assert get_entry("gmail") is None
    
def test_serviceDNE():
    entry = get_entry("DNE")
    assert entry is None

def test_deleteserviceDNE():
    result = delete_entry("DNE")
    assert result == False
