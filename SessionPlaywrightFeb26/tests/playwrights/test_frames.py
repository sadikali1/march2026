from playwright.sync_api import Page


def test_frames_handling(page: Page):
    """Navigate to frames page, read main context and frame contents."""
    page.goto("https://demoqa.com/frames")

    # Get text from main context (page header)
    main_header = page.locator("h1").text_content()
    print("Main header:", main_header)
    assert main_header.strip() == "Frames"

    # Get and print text from the first frame
    frame1_text = page.frame_locator("#frame1").locator("h1#sampleHeading").text_content()
    print("Frame1 text:", frame1_text)
    assert frame1_text.strip() == "This is a sample page"

    # Get text from the second frame and verify
    frame2_text = page.frame_locator("#frame2").locator("h1#sampleHeading").text_content()
    print("Frame2 text:", frame2_text)
    assert frame2_text.strip() == "This is a sample page"
