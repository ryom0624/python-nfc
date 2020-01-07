import nfc
from nfc.clf import RemoteTarget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# print("Please Touch")
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])

while True:

    with nfc.ContactlessFrontend('usb') as clf:

        target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))

        while target:
            tag = nfc.tag.activate(clf, target)

            try:
                # print(tag.ndef.records[0].uri)

                try:
                    driver.current_url
                    # print("driver開いてますのでなにもしません。")
                    break
                except:
                    # print("driverないのでchrome開きます")
                    driver = webdriver.Chrome(options=chromeOptions)
                    driver.get(tag.ndef.records[0].uri)
                    while target:
                        break
            except:
                # print('Released')
                try:
                    # print("driver closeします")
                    driver.quit()
                    driver = None
                except:
                    # print("driver立ち上がってないのでなにもしません。")
                    pass
            break

        else:
            # print('Released')
            try:
                # print("driver closeします")
                driver.quit()
                driver = None
            except:
                # print("driver立ち上がってないのでなにもしません。")
                pass
