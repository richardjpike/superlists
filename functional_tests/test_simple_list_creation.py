from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online todo app.  She goes to checkout it's homepage.
		self.browser.get(self.server_url)

		# She notices the page title and header menton to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.get_item_input_box()
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
				)

		# She types 'Buy Peacock Feathers' into a text box - Ediths hobby is tying fishing lures.
		inputbox.send_keys('Buy Peacock Feathers')

		# When she hits enter the page updates.  Now the page lists:  1:  Buy peacock feathers in the todo list.
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		#delay for viewing output on error
		# import time
		#time.sleep(10)

		self.check_for_row_in_list_table('1: Buy Peacock Feathers')

		# There is still a text box inviting her to add another item.  She enters 'Use peacock feathers to make a fly'
		inputbox = self.get_item_input_box()
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# THe page updates again and shows both items in her list.
		self.check_for_row_in_list_table('1: Buy Peacock Feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


		# New user Francis comes along to the site.

		# Generate new browser session
		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

		# Francis visits the homepage - there is no sign of Ediths list.
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy Peacock Feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# Francis starts a new list
		inputbox = self.get_item_input_box()
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# Francis gets his own URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# Again no trace of Ediths list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy Peacock Feathers', page_text)
		self.assertIn('Buy milk', page_text)

		# Satisfied - they both go back to sleep.
