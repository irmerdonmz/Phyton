from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckDriverManager

def get_driver_path_with_browser_name(browser_name):
    if browser_name.lower == 'chrome':
        driver_path = ChromeDriverManager().install()
    elif browser_name.lower() == 'firefox':
        river_path = GeckDriverManager().install()
    print(driver_path)
    return driver_path

*** Settings ***
Library SeleniumLibrary


*** Keywords ***
launchBrowser
    [Arguments]  ${appurl}     ${appbrowser}
    open browser ${appurl}     ${appbrowser}
    maximize browser window
    ${title} =  get title
    [Return]    ${title}