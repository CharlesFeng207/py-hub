# coding:utf8 #

from common import browser_utils,req_utils
from common.settings import Settings


def need_login(page_content):
    return str("请输入邮箱或手机" in page_content)


login_url = "https://www.tapd.cn/cloud_logins/login"
url = "https://www.tapd.cn/22461221/prong/stories/stories_list?left_tree=1"

print("requests需要登陆? " + need_login(req_utils.get_page_code(url)))

print("添加cookie..")
Settings.load_json_cookies("test/cookie.json")

print("requests需要登陆? " + need_login(req_utils.get_page_code(url)))

driver = browser_utils.get_webdriver()

driver.get(url)
print("driver需要登陆? " + need_login(driver.page_source))

print("添加cookie..")
browser_utils.add_cookie_from_settings(driver)
driver.refresh()

print("driver需要登陆? " + need_login(driver.page_source))

driver.quit()



