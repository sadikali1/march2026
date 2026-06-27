import os
from playwright.sync_api import Page, Browser


os.makedirs("reports", exist_ok=True)


def test_add_webtable_entry(page: Page):
	"""Navigate to web tables, add a new record and verify it appears."""
	page.goto("https://demoqa.com/webtables")

	# Start tracing to record the execution of this test
	page.context.tracing.start(screenshots=True, snapshots=True)

	# Open registration form
	page.click("#addNewRecordButton")

	# Fill the form
	page.fill("#firstName", "John")
	page.fill("#lastName", "Doe")
	page.fill("#userEmail", "john.doe@example.com")
	page.fill("#age", "30")
	page.fill("#salary", "50000")
	page.fill("#department", "IT")

	# Submit
	page.click("#submit")

	# Verify the new entry appears in the table
	# Save a screenshot after adding
	page.screenshot(path="reports/webtable_after_add.png", full_page=True)
	table = page.locator("table.table")
	table_text = table.text_content()
	print("Table contents after adding new record:\n", table_text)
	assert "john.doe@example.com" in table_text

	# Iterate rows and columns to find the record
	rows = page.locator("table.table > tbody > tr")
	row_count = rows.count()
	found_row = None
	for i in range(row_count):
		row = rows.nth(i)
		cells = row.locator("td")
		cell_count = cells.count()
		if cell_count < 6:
			continue
		first = cells.nth(0).text_content().strip()
		last = cells.nth(1).text_content().strip()
		age = cells.nth(2).text_content().strip()
		email = cells.nth(3).text_content().strip()
		salary = cells.nth(4).text_content().strip()
		dept = cells.nth(5).text_content().strip()
		print(f"Row {i}: {first} {last}, {email}, Age: {age}, Salary: {salary}, Dept: {dept}")
		# verify values for this row
		if first == "John" and last == "Doe" and email == "john.doe@example.com":
			assert age == "30"
			assert salary == "50000"
			assert dept == "IT"
			found_row = row
			print(f"Found the added record in row {i}")
			break
        
	assert found_row is not None, "Added record not found in table"

	# Click the Delete button for the found row and verify removal
	found_row.locator("span[title='Delete']").click()
	page.wait_for_timeout(500)
	# stop tracing and save trace
	trace_path = "reports/webtable_add_trace.zip"
	page.context.tracing.stop(path=trace_path)
	print(f"Trace saved to {trace_path}")
	assert "john.doe@example.com" not in table.text_content()


def test_add_webtable_entry_record_video(browser: Browser):
	"""Add a webtable record while recording a video of the context."""
	os.makedirs("reports/videos", exist_ok=True)
	ctx = browser.new_context(record_video_dir="reports/videos", record_video_size={"width": 1280, "height": 720})
	page = ctx.new_page()
	page.goto("https://demoqa.com/webtables")

	# Open registration form and fill
	page.click("#addNewRecordButton")
	page.fill("#firstName", "John")
	page.fill("#lastName", "Doe")
	page.fill("#userEmail", "john.doe@example.com")
	page.fill("#age", "30")
	page.fill("#salary", "50000")
	page.fill("#department", "IT")
	page.click("#submit")

	# verify added
	#assert "john.doe@example.com" in page.locator("div.rt-tbody").text_content()

	# close page to finalize video file and get path
	page.close()
	# video file is written after closing the page/context
	# locate the video file generated
	# Note: page.video.path() is only available before closing the context in some versions; we search the dir instead
	ctx.close()

	videos = [p for p in os.listdir("reports/videos") if p.endswith(".webm") or p.endswith(".mp4") or p.endswith(".zip")]
	assert len(videos) > 0, "No video file found in reports/videos"
	print("Video files:", videos)

