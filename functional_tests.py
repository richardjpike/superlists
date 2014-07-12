from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	""" Tests must start with the word test to run """
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online todo app.  She goes to checkout it's homepage.
		self.browser.get('http://localhost:8000')

		# She notices the page title and header menton to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test')

		# She is invited to enter a to-do item straight away

		# She types 'Buy Peacock Feathers' into a text box - Ediths hobby is tying fishing lures.

		# When she hits enter the page updates.  Now the page lists:  1:  Buy peacock feathers in the todo list.

		# There is still a text box inviting her to add another item.  She enters 'Use peacock feathers to make a fly'

		# THe page updates again and shows both items in her list.

		# Edith wonders if the site will remember her list.  Then she sees a URL that the site generated - a unique URL for her
		# There is some explainatory text to that affect.

		# She visits that URL - her list is still there.

		# Satisfied - she goes back to sleep.


if __name__ == '__main__':
	unittest.main(warnings='ignore')

