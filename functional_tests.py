from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
				)

		# She types 'Buy Peacock Feathers' into a text box - Ediths hobby is tying fishing lures.
		inputbox.send_keys('Buy Peacock Feathers')

		# When she hits enter the page updates.  Now the page lists:  1:  Buy peacock feathers in the todo list.
		inputbox.send_keys(Keys.ENTER)

		#delay for viewing output on error
		# import time
		#time.sleep(10)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy Peacock Feathers', [row.text for row in rows])

		# There is still a text box inviting her to add another item.  She enters 'Use peacock feathers to make a fly'
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# THe page updates again and shows both items in her list.
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy Peacock Feathers', [row.text for row in rows])
		self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

		# Edith wonders if the site will remember her list.  Then she sees a URL that the site generated - a unique URL for her
		# There is some explainatory text to that affect.
		self.fail('Finish the test!')

		# She visits that URL - her list is still there.

		# Satisfied - she goes back to sleep.


if __name__ == '__main__':
	unittest.main(warnings='ignore')

