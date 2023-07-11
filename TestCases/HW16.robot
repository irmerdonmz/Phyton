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
Resource  ../Resources/resources.robot

*** Variables ***
${url}      https://www.demoblaze.com/
${browser}  chrome
${userName}  iremerd
${password}  010203

*** Test Cases ***
TC1
    ${PageTitle} =  launchBrowser    ${url}     ${browser}
    log to console  ${pageTitle}
    log   ${PageTitle}
    input text  name: userName    iremerd
    input text  password: password    010203
    assert customerName == "Welcome iremerd"
