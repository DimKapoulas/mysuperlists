from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        return self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone heard about a cool on-line app.
        # He/she goes to check its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title  and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # She types "Buy peacok feathers" into a text box
        inputbox.send_keys('Buy peacok feathers')

        # Whe she hits enter, the page updates, and now the page lsit
        # "1: Buy peacok feathers" as an item in to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacok feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box invitting her to add another item. She
        # enters"Use peacok feathers to make afly"
        self.fail('Finish the rest of test!')

        # The page updates again, and now shows both items onher list

        # Now wonders whether the site will rembember her list.
        # Notices the site has generated a unique URL with some explanatory text to that effect

        # She vistis that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    


