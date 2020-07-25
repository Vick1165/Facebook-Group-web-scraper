from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import SendToGoogleSheets
import config
import progressbar

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')

driver.get("https://www.facebook.com/login/")

keyword = ''


def FbLogin():


    print('Facebook Login')
    username = config.username
    password = config.password
    keyword  = input('Please Enter Keyword to Search  :')
    groupUrl = 'https://www.facebook.com/search/groups/?q=' + keyword + '&epa=SERP_TAB'
    # https: // www.facebook.com / search / groups /?q = cycle & epa = SERP_TAB
    username_fb = driver.find_element_by_id('email')
    username_fb.clear()
    username_fb.send_keys(username)

    password_fb = driver.find_element_by_id('pass')
    password_fb.clear()
    password_fb.send_keys(password)

    driver.find_element_by_id('loginbutton').click()
    time.sleep(2)
    string_url = driver.current_url;
    Fb_urls= []
    Fb_urls.append('https://www.facebook.com/')
    Fb_urls.append('https://www.facebook.com/?sk=welcome')


    for url in Fb_urls:
        if string_url == url:
            print('Login Sucessfull')
            driver.get(groupUrl)
            time.sleep(2)
            for x in range(4):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(2)
        #else:
            #print('UserName or Password is incorrect. Please run the script again')

    return keyword




def QuitDriver():
    time.sleep(30)
    driver.quit()


def GroupLinkScrap():
    elems = driver.find_elements_by_xpath("//a[@href]")
    group_links = []
    for elem in elems:
        group_links.append(elem.get_attribute("href"))

    group_links1 = [x for x in group_links if x.startswith('https://www.facebook.com/groups')]
    filtered_list = remove_duplicates(group_links1)
    return filtered_list


def remove_duplicates(l):
    return list(set(l))


def GroupDetailsScrap(keyword):

        group_links = GroupLinkScrap()
        bar = progressbar.ProgressBar(
            widgets=[progressbar.SimpleProgress()],
            max_value=len(group_links),
        ).start()
        i = 0
        for link in group_links:
            try:

                driver.get(link)
                time.sleep(2)
                group_name = driver.find_element_by_css_selector('#seo_h1_tag > a').text
                group_type = driver.find_elements_by_css_selector(
                    '#pagelet_group_about > div:nth-child(1) > div._j1y > div > div > div._3-8n._3qn7._61-0._2fyi._3qng > div:nth-child(2) > div._2ieo')

                if len(group_type) > 0:
                    group_type_name = group_type[0].text
                else:
                    group_type_name = driver.find_element_by_css_selector('#groupsDescriptionBox > div > div._3-8x > span > span').text

                #print(link,group_name,group_type_name)
                joinGroup(link,group_name,group_type_name,keyword)
                i = i+1
                time.sleep(0.1)
                bar.update(i)

            except NoSuchElementException:  # spelling error making this code not work as expected
                pass
        bar.finish()





def joinGroup(link,group_name,group_type_name,keyword):
    try:

        Stringxpath = driver.find_elements_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/a')
        if len(Stringxpath) > 0:
            Stringxpath = Stringxpath[0]
            Stringxpath.click()

        else :
            Stringxpath = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/span/button')
            Stringxpath.click()
            time.sleep(2)

            SelectProfile = driver.find_elements_by_xpath(
                '/html/body/div[24]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')
            if len(SelectProfile) > 0:
                SelectProfile = SelectProfile[0]
                SelectProfile.click()

            elif len(driver.find_elements_by_xpath(
                    '/html/body/div[15]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')) > 0:

                SelectProfile = driver.find_elements_by_xpath(
                    '/html/body/div[15]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')
                SelectProfile = SelectProfile[0]
                SelectProfile.click()
            elif len(driver.find_elements_by_xpath(
                    '/html/body/div[16]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')) > 0:

                SelectProfile=driver.find_elements_by_xpath(
                    '/html/body/div[16]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')
                SelectProfile = SelectProfile[0]
                SelectProfile.click()

            elif len(driver.find_elements_by_xpath(
                    '/html/body/div[17]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')) > 0:

                SelectProfile = driver.find_elements_by_xpath(
                    '/html/body/div[17]/div[2]/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')
                SelectProfile = SelectProfile[0]
                SelectProfile.click()



        time.sleep(2)



        #
        # checkbox = driver.find_elements_by_xpath(
        #     '//*[@id="facebook"]/body/div[15]/div[2]/div/div/div/div/div/div/div[2]/div/div[6]/div[1]/div[2]')

        # submit = driver.find_elements_by_css_selector(
        #     'body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div > div > div._4iyh._2pia._2pi4 > span._4iyi > div > div > button > div > div')


        # if len(checkbox) > 0:
        #     checkbox = checkbox[0]
        #     checkbox.click()
        #
        # if len(submit) > 0:
        #     submit = submit[0]
        #     submit.click()

        status = driver.find_elements_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/a/span[1]')
        if len(status) <= 0:
            status = driver.find_elements_by_xpath(
                 '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/a/span[1]')


        if len(status) > 0:
            status = status[0].text
            if status == 'Pending' or status == 'Joined':
                SendToGoogleSheets.send_to_Drive(keyword, group_name, group_type_name, link)
                # print('Joined Group')
            else:
                SendToGoogleSheets.send_to_Drive_Sheet2(keyword, group_name, group_type_name, link)
        else:
            SendToGoogleSheets.send_to_Drive_Sheet2(keyword, group_name, group_type_name, link)


    except Exception as e:
        print(e)



keyword = FbLogin()
GroupDetailsScrap(keyword)
QuitDriver()
