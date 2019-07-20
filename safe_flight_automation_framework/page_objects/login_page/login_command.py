#!/usr/bin/env python3
"""LoginCommand is used by LoginPage to make a fluent API for the login form.
"""

import sys
from ..driver import Driver
from selenium.webdriver.common.by import By

class LoginCommand:
    def __init__(self, username, USERNAME, PASSWORD, LOGIN_BUTTON):
        self._username = username
        self._password = ""
        self._USERNAME = USERNAME
        self._PASSWORD = PASSWORD
        self._LOGIN_BUTTON = LOGIN_BUTTON
    def with_password(self, password):
        self._password = password
        return self
    def submit_form(self):
        Driver.instance.find_element(*self._USERNAME).send_keys(self._username)
        Driver.instance.find_element(*self._PASSWORD).send_keys(self._password)
        Driver.instance.find_element(*self._LOGIN_BUTTON).click()


if __name__ == "__main__":
    pass