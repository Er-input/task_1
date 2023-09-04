import os
import pytest
from pages.FormPage import FormClass
from conftest import browser

url = 'https://demoqa.com/automation-practice-form'

@pytest.mark.smoke
def test_form_completion(browser):
    set_form = FormClass(browser)
    set_form.open(url=url)
    assert set_form.set_values('Ержан', 'Ембергенов', 'count1@inbox.ru', 'Male',
                      '7777324228', '02.12.2007', ['Maths', 'Hindi'], ['Sports', 'Reading'],
                      f'{os.getcwd()}' + '/images/1.jpg', 'Tolebi 71', 'Haryana', 'Panipat')

@pytest.mark.xfail
def test_form_with_incomplite_phone(browser):
    set_form = FormClass(browser)
    set_form.open(url=url)
    assert set_form.set_values('Алия', 'Жаксылыкова', 'co2@inbox.ru', 'Female',
                      '77773242', '02.12.2007', ['Maths', 'Hindi'], ['Sports', 'Reading'],
                      f'{os.getcwd()}' + '/images/1.jpg', 'Tolebi 71', 'Haryana', 'Panipat') == False

@pytest.mark.xfail
def test_form_with_incomplite_email(browser):
    set_form = FormClass(browser)
    set_form.open(url=url)
    assert set_form.set_values('', '', 'inbox.ru', 'Other',
                      '7777324222', '02.12.2007', ['Maths', 'Hindi'], ['Sports', 'Reading'],
                      f'{os.getcwd()}' + '/images/1.jpg', 'Tolebi 71', 'Haryana', 'Panipat') == False
