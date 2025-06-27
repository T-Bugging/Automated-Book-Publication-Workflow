from playwright.sync_api import sync_playwright 
import os

def scrape(url):
    outputDir = 'output'   # The name of directory to save the output
    ssDir = os.path.join(outputDir, 'screenshots')  # Directory for screenshots
    rawTextDir = os.path.join(outputDir, 'Raw_text')  # Directory for raw text files
    spunTextDir = os.path.join(outputDir, 'Spun_text')  # Directory for spun and reviewed text files

    # Create the directories if they do not exist
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    if not os.path.exists(ssDir):
        os.mkdir(ssDir)

    if not os.path.exists(rawTextDir):
        os.mkdir(rawTextDir)

    if not os.path.exists(spunTextDir):
        os.mkdir(spunTextDir)

    # Launching browser
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Taking and saving screenshots
    
        existingSS = [f for f in os.listdir(ssDir) if f.startswith("screenshot_") and f.endswith(".png")]
        numberOfScreenshots = len(existingSS) + 1
        ssPath = os.path.join(ssDir, f'screenshot_{numberOfScreenshots}.png')
        page.screenshot(path=ssPath, full_page=True)
        print(f'Screenshot saved at {ssPath}')
        numberOfScreenshots += 1

        # Extracting text content
        existingTxt = [f for f in os.listdir(rawTextDir) if f.startswith("text_") and f.endswith(".txt")]
        numberOftextFiles = len(existingTxt) + 1
        textpath = os.path.join(rawTextDir, f'text_{numberOftextFiles}.txt')
        content = page.locator("div#mw-content-text").inner_text()
        with open(textpath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Text content saved at {textpath}')
        numberOftextFiles += 1

        # Close the browser
        browser.close()
        print("Scraping completed successfully.")
