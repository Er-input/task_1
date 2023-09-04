import datetime
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BaseClass
from selenium.webdriver.common.by import By


class FormClass(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def set_values(self, name, last_name, email, gender,
                   mobile, date_of_birth, subject, hobbies, picture, current_address,
                   state, city):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_gender(gender)
        self.set_mobile(mobile)
        self.set_date_of_birth(date_of_birth)
        self.set_subjects(subject)
        self.set_hobbies(hobbies)
        self.set_picture(picture)
        self.set_current_address(current_address)
        self.set_state(state)
        self.set_city(city)
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.browser.find_element(By.CLASS_NAME, 'modal-header')))
            return self.assert_information(name, last_name, email, gender,
                                           mobile, date_of_birth, subject, hobbies, picture, current_address,
                                           state, city)
        except AssertionError as AE:
            return AE.__str__()
        except:
            return False

    def set_name(self, name):
        self.browser.find_element(By.ID, 'firstName').send_keys(name)

    def set_last_name(self, last_name):
        self.browser.find_element(By.ID, 'lastName').send_keys(last_name)

    def set_email(self, email):
        self.browser.find_element(By.ID, 'userEmail').send_keys(email)

    def set_gender(self, gender):
        elements = self.browser.find_elements(By.CSS_SELECTOR, '#genterWrapper > div .custom-control-label')
        for elem in elements:
            if elem.text == gender:
                self.move_to_element_and_click(elem)
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(elem)).click()

    def set_mobile(self, mobile):
        self.browser.find_element(By.ID, 'userNumber').send_keys(mobile)

    def set_date_of_birth(self, date_of_birth):
        pick_date = self.browser.find_element(By.ID, 'dateOfBirthInput')
        pick_date.send_keys(Keys.CONTROL + "a")
        pick_date.send_keys(datetime.datetime.strftime(datetime.datetime.strptime(date_of_birth, '%d.%m.%Y'), '%d %b %Y'))
        pick_date.send_keys(Keys.ENTER)


    def set_subjects(self, subjects):
        subject = self.browser.find_element(By.XPATH, '//*[@id="subjectsInput"]')
        for sub in subjects:
            subject.send_keys(sub)
            subject.send_keys(Keys.ENTER)

    def set_hobbies(self, hobbies):
        elements = self.browser.find_elements(By.CSS_SELECTOR, '#hobbiesWrapper > div .custom-control-label')
        for elem in elements:
            if elem.text in hobbies:
                self.move_to_element_and_click(elem)
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(elem)).click()

    def set_picture(self, picture):
         self.browser.find_element(By.ID, 'uploadPicture').send_keys(picture)

    def set_current_address(self, current_address):
         self.browser.find_element(By.ID, 'currentAddress').send_keys(current_address)

    def set_state(self, state):
        state_pick = self.browser.find_element(By.ID, 'react-select-3-input')
        state_pick.send_keys(state)
        state_pick.send_keys(Keys.ENTER)

    def set_city(self, city):
        city_pick = self.browser.find_element(By.ID, 'react-select-4-input')
        city_pick.send_keys(city)
        city_pick.send_keys(Keys.ENTER, Keys.ENTER)

    def click_submit_button(self):
        self.browser.find_element(By.XPATH, '//*[@id="submit"]').click()

    def assert_information(self, name, last_name, email, gender,
                   mobile, date_of_birth, subject, hobbies, picture, current_address,
                   state, city):
        rows = self.browser.find_elements(By.XPATH, '//td[2]')
        assert f'{name} {last_name}' == rows[0].text, 'Ошибка в информации о имени и фамилии'
        assert email == rows[1].text, 'Ошибка в email'
        assert gender == rows[2].text, 'Ошибка в поле'
        assert mobile == rows[3].text, 'Ошибка в телефоном номере'
        assert datetime.datetime.strftime(datetime.datetime.strptime(date_of_birth, '%d.%m.%Y'), '%d %B,%Y') == rows[4].text, 'Ошибка в дате рождения'
        assert ', '.join(subject) == rows[5].text, 'Ошибка в выбранных предметах'
        assert ', '.join(hobbies)  == rows[6].text, 'Ошибка в выбранных хобби'
        #assert picture == rows[2].find_element(By.TAG_NAME, 'td')
        assert current_address == rows[8].text, 'Ошибка в текущем адресе'
        assert f'{state} {city}' == rows[9].text, 'Ошибка в стране и городе'
        return True