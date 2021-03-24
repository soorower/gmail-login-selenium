
from colorama import init, Fore, Back, Style
from discord_webhook import DiscordWebhook, DiscordEmbed

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("user-agent=DN")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
            
#login to gmail
    logged = False
    while logged == False:
        try:
       
            time.sleep(3)
            driver.get('https://stackoverflow.com/')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/button[1]').click()
            time.sleep(0.5)
            driver.find_element_by_id('Email').send_keys(EMAIL VARIABLE)
            print(Fore.YELLOW + ' SENT EMAIL LOGIN ')
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div/div/input').click()
            time.sleep(0.5)
            driver.find_element_by_id('password').send_keys(PASSWORD VARIABLE)
            print(Fore.YELLOW + time_format() + ' SENT PASSWORD LOGIN ')
            driver.find_element_by_id('submit').click()
            print(Fore.BLUE + ' SUCCESSFULLY LOGGED IN ')
            logged = True
        except:
            print(Fore.RED + ' FAILED LOGIN ')
