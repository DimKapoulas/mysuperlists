from selenium import webdriver
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

        # She notices the page title is to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do straight away

        # She types "Buy peacok feathers" into a text box

        # Whe she hits enter, the page updates, and now the page lsit
        # "1: Buy peacok feathers" as an item in to-do list

        # There is still a text box invitting her to add another item. She
        # enters"Use peacok feathers to make afly"

        # The page updates again, and now shows both items onher list

        # Now wonders whether the site will rembember her list.
        # Notices the site has generated a unique URL with some explanatory text to that effect

        # She vistis that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    


