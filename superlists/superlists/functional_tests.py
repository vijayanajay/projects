__author__ = 'Ajay'
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import logging
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do lists', self.browser.title)  #5
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.RETURN)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            'New to-do item did not appear in table'
        )

        self.fail('Finish the test!')  #6

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':  #7
    unittest.main()

