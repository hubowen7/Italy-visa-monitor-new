# monitor.py
from playwright.sync_api import sync_playwright
import json


def run_monitor():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 从文件中加载Cookies
        with open('visa.vfsglobal.com.json', 'r') as cookies_file:
            cookies = json.load(cookies_file)

        # 确保每个Cookie的sameSite属性是有效的
        for cookie in cookies:
            if 'sameSite' in cookie and cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                cookie['sameSite'] = "None"  # 或者选择 "Strict" 或 "Lax" 根据需要

            # 针对过期时间的处理
            if 'expirationDate' in cookie:
                cookie['expires'] = cookie.pop('expirationDate')

        context.add_cookies(cookies)

        # 使用应用了cookies的上下文访问受保护的页面
        page.goto('https://visa.vfsglobal.com/chn/zh/ita/application-detail')
        # 等待“选择签证申请中心”的元素出现
        selector = 'text="选择签证申请中心"'
        # 等待最多60000毫秒（60秒）
        page.wait_for_selector(selector, timeout=60000)

        print("找到了‘选择签证申请中心’的元素，页面已加载。")



if __name__ == '__main__':
    run_monitor()





