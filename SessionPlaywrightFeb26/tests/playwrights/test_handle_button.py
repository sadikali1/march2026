from playwright.sync_api import Page, expect


def test_demoqa_button_clicks(page: Page):
    page.goto("https://demoqa.com/buttons")

    double_click_btn = page.locator("//button[@id='doubleClickBtn']")
    right_click_btn = page.locator("//button[@id='rightClickBtn']")
    single_click_btn = page.locator("//button[text()='Click Me']")

    double_click_btn.dblclick()
    expect(page.locator("//p[@id='doubleClickMessage']")).to_have_text(
        "You have done a double click"
    )

    right_click_btn.click(button="right")
    expect(page.locator("//p[@id='rightClickMessage']")).to_have_text(
        "You have done a right click"
    )

    single_click_btn.click()
    expect(page.locator("//p[@id='dynamicClickMessage']")).to_have_text(
        "You have done a dynamic click"
    )
