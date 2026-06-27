from playwright.sync_api import Page


def test_window_handling(page: Page):
	"""Navigate to the demo page and verify new tab/window/message contents."""
	page.goto("https://demoqa.com/browser-windows")

	# Click New Tab and verify text
	with page.context.expect_page() as new_tab_info:
		page.click("#tabButton")
	new_tab = new_tab_info.value
	new_tab.wait_for_load_state()
	heading = new_tab.locator("#sampleHeading").text_content()
	assert heading == "This is a sample page"
	new_tab.close()

	# Click New Window and verify text
	with page.context.expect_page() as new_win_info:
		page.click("#windowButton")
	new_win = new_win_info.value
	new_win.wait_for_load_state()
	heading2 = new_win.locator("#sampleHeading").text_content()
	assert heading2.strip() == "This is a sample page"
	new_win.close()

	# Click New Window Message and verify text contains expected phrase
	with page.context.expect_page() as aa:
		page.click("#messageWindowButton")
	msg_page = aa.value
	msg_page.wait_for_load_state()
	body_text = msg_page.locator("body").text_content()
	assert "Knowledge increases" in body_text
	msg_page.close()


