from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

def inputfield(username, password):
    opt=webdriver.ChromeOptions()
    opt.add_argument('headless')
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
    driver.get("https://qahomeworktest.printercloud.com/admin/index.php")
    #Open an instance of chromedriver and direct it to my environment's URL
    userElem = driver.find_element_by_xpath("//input[@id='relogin_user']")
    passElem = driver.find_element_by_xpath("//input[@id='relogin_password']")
    #Set variables to the 'first' input field that matches the specified id; find username and password fields
    userElem.clear()
    userElem.send_keys(username)
    passElem.clear()
    passElem.send_keys(password)
    passElem.send_keys(Keys.RETURN)
    #send login information to the webpage and enter
    time.sleep(1.5)
    if ('"user-menu">'+username in driver.page_source):
        #checks if the username variable can be found next to a specific peice of html code, which signifies whether login was successful or not
        driver.quit()
        return True
    driver.quit()
    return False
        
class TestLoginAttempt(unittest.TestCase):
    def test_all_combos(self):
        usernames=["badname","1","0.0123","!@#$%^&*()-=\/*+[]{}|';:?.>,<`~","-99999999999999999999"]
        passwords=["badpass","1","0.0123","!@#$%^&*()-=\/*+[]{}|';:?.>,<`~","-99999999999999999999"]
        #bad creds, integer, float, special characters, integer overflow(I think 20 9s is enough)
        for u in usernames:
            for p in passwords:
                with self.subTest(p=p,u=u):
                    self.assertEqual(inputfield(u,p), False)
                    #Test all bad combinations, expecting failure
        goodNames=["egoller","goodname"]
        goodPass=["abc12345","goodpass1"]
        #Good credentials, expecting success 50% of the time
        for i in range(len(goodNames)*2):
            with self.subTest(i=i):
                if i<2:
                    self.assertEqual(inputfield(goodNames[i],goodPass[i]), True)
                    #Keep the usernames and passwords aligned, such that each value of goodNames and goodPass AT "i" is one whole good credential
                else:
                    self.assertEqual(inputfield(goodNames[i-2],"badpass"), False)
                    #loop through a second time but with a bad password
        #self.assertEqual(inputfield(usernames[0],passwords[0]), True)
        #^ single out a specific login
        return

if __name__=='__main__':
    unittest.main()


