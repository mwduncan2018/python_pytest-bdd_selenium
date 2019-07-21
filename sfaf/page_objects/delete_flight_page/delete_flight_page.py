#!/usr/bin/env python3
"""Page-object model for the Delete Flight Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from selenium.webdriver.common.by import By

class DeleteFlightPage(AbstractPage):
    """Page-Object Model for the Delete Flight Page.
    """

    #The url path for the Delete Flight Page.
    _path = "Delete"
    #The page name displayed on the Delete Flight Page.
    _page_name = "Delete Flight"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
        'delete_button' : (By.ID, "btnDelete"),
    }

    @classmethod
    def click_delete_button(self):
        """Clicks the delete button to delete the flight.

        Args:
            None
        
        Returns:
            None
        """
        self.is_at_with_exception()
        Driver.instance.find_element(*self._selectors['delete_button']).click()


if __name__ == "__main__":
    pass