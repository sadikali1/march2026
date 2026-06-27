from playwright.sync_api import Page, expect


def test_demoqa_alerts(page: Page):
    page.goto("https://demoqa.com/alerts")

    # Simple alert — accept immediately via a one-time handler
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("//button[@id='alertButton']")

    # Timer alert (appears after a short delay) — accept when it appears
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("//button[@id='timerAlertButton']")

    # Confirm alert - dismiss via a one-time handler
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.click("//button[@id='confirmButton']")
    expect(page.locator("//span[@id='confirmResult']")).to_have_text("You selected Cancel")

    # Prompt alert - provide text
    page.once("dialog", lambda dialog: dialog.accept("Playwright"))
    page.click("//button[@id='promtButton']")
    expect(page.locator("//span[@id='promptResult']")).to_contain_text("You entered Playwright")
