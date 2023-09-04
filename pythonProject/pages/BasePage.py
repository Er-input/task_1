class BaseClass():

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url=url)

    def move_to_element_and_click(self, element):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
