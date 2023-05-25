import pytest
import smtplib

@pytest.fixture
def smtp():
    return smtplib.SMTP("smtp.orange.fr")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250