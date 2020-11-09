from selenium import webdriver
from time import sleep
from time import time
from getpass import getpass


class My_insta_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome("driver/chromedriver.exe")

        self.driver.get("https://instagram.com")
        sleep(1)

        username_button = self.driver.find_element_by_name("username")
        username_button.send_keys(self.username)

        password_button = self.driver.find_element_by_name("password")
        password_button.send_keys(self.password)

        log_In = self.driver.find_element_by_tag_name('form')
        log_In.submit()
        sleep(5)

        saveinfo_not_now = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button')
        saveinfo_not_now.click()
        sleep(1)

        notification_not_now = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notification_not_now.click()

        profile = self.driver.find_element_by_class_name("gmFkV")
        profile.click()
        sleep(1)

    def get_followers(self):
        followers_button = self.driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > ul > li:nth-child(2) > a")
        followers_button.click()
        sleep(1)

        scrollbox = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP")
        followers = self.__getnames__(scrollbox)
        self.driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg").click()
        return followers

    def get_following(self):
        following_button = self.driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > ul > li:nth-child(3) > a")
        following_button.click()
        sleep(1)

        scrollbox = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP")
        following = self.__getnames__(scrollbox)
        self.driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg").click()
        return following

    def __getnames__(self, scrollbox):
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script('''
                arguments[0].scrollTo(0,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                ''', scrollbox)
        links = scrollbox.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        return names

    def quit(self):
        self.driver.close()


if __name__ == "__main__":
    start = time()
    try:
        username = input("Enter Your Phone number/Username/email : ")
        print("\nPassword you type wouldn't appear on the screen")
        password = getpass("\nEnter your password : ")
        print("\nPlease be patient, it might take upto 5 to 10 mins")
        sleep(1.5)
        bot = My_insta_bot(username, password)
        following = bot.get_following()
        followers = bot.get_followers()
        unfollowers = [user for user in following if user not in followers]
        print("\nUsers that don't follow you : \n")
        for unfollower in unfollowers:
            print(' '*10,unfollower)
        print("\nNo of users that don't follow you are : ",len(unfollowers))
        bot.quit()
    except:
        print("\nThere must've been some interruptions or wrong login credentials")

    end = time()
    print ("\nThe execution time of the script is : ",int(end-start)," sec")

