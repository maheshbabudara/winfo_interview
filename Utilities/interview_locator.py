from selenium.webdriver.chrome.webdriver import WebDriver

def locator_gen(url,attribute,value):
    driver=WebDriver()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        element=driver.find_element("xpath","//*[@placeholder='User name or email']")

        element_tagname=element.tag_name
        element_text=element.text
        class_value=element.get_attribute("class")
        id_value=element.get_attribute("id")

        #xpath:
        # print(f'//{element_tagname}[@{attribute}={value}]')
        username_loc=('xpath',f'//*[@{attribute}={value}]')
        password_loc=('xpath',f'//*[@{attribute}={value}]')
        submit_btn=('xpath',f'//*[@{attribute}={value}]')

        return username_loc,password_loc,submit_btn

    except:
        print("Not found locator")

if __name__=='__main__':
    url=input("Enter URL:")
    attribute=input("Enter element ettribute:")
    value=input("Enter element value:")
    Login_locators=list(locator_gen(url=url, attribute=attribute, value=value))
    # print(list(locator_gen(url, attribute, value)))











#locatords:
Breadcrumb=('xpath','//a[@title="Oracle Logo Home"]/../preceding-sibling::td//a[@title="Navigator"]')
General_counting=('xpath','//div[@title="General Accounting"]')
journals=('xpath','//span[text()="Journals"]')
journal_task=('xpath','//div[@title="Tasks"]')
create_journals=('xpath','//a[text()="Create Journal"]')
journal_batch=('xpath','//label[text()="Journal Batch"]/../following-sibling::td/input')
Description=('xpath','//label[text()="Journal Batch"]/../../following-sibling::tr//label[text()="Description"]')
Accounting_period=('xpath','//span[@aria-label="Accounting Period"]/input[@aria-label="Accounting Period"]')













