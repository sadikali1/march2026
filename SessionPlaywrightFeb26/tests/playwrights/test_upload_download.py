import os
from pathlib import Path
from playwright.sync_api import Page, expect


def test_demoqa_upload_and_download(page: Page, tmp_path: Path):
    page.goto("https://demoqa.com/upload-download")

    # Download file and verify the download completes.
    download_path = tmp_path / "downloaded_sampleFile.jpeg"
    with page.expect_download() as download_info:
        page.click("//a[@id='downloadButton']")
    download = download_info.value
    download.save_as(str(download_path))
    assert download_path.exists(), f"Expected downloaded file at {download_path}"

    # Upload file and verify the upload result.
    upload_file = Path(r"C:\Users\pc\Downloads\Tokens.pdf")
    if not upload_file.exists():
        raise FileNotFoundError(f"Upload file not found: {upload_file}")

    page.locator("//input[@id='uploadFile']").set_input_files(str(upload_file))
    uploaded_text = page.locator("//p[@id='uploadedFilePath']")
    expect(uploaded_text).to_be_visible(timeout=10000)
    expect(uploaded_text).to_contain_text(upload_file.name)
