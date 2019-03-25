from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from .settings import Settings


def get_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920x1080')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    # Configure Proxy Option
    proxy = Proxy()

    if Settings.socks_proxy is None and Settings.https_proxy is None and Settings.https_proxy is None:
        proxy.proxy_type = ProxyType.DIRECT
    else:
        proxy.proxy_type = ProxyType.MANUAL

        if Settings.socks_proxy is not None:
            options.add_argument("--proxy-server=" + Settings.get_full_socks_proxy())
        else:
            if Settings.http_proxy is not None:
                proxy.http_proxy = Settings.http_proxy
            if Settings.https_proxy is not None:
                proxy.ssl_proxy = Settings.https_proxy

    # Configure capabilities
    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    return webdriver.Chrome(options=options, desired_capabilities=capabilities)


def add_cookie_from_settings(driver):
    for c in Settings.cookies:
        driver.add_cookie(c)


def save_screenshot(url=None, pagecode=None):
    driver = get_webdriver()

    if url is not None:
        driver.get(url)
    elif pagecode is not None:
        driver.get("data:text/html;charset=utf-8,{}".format(pagecode))
    else:
        raise Exception("parameters error!")

    driver.get_screenshot_as_file("screenshot.png")

