# monitor.py
from playwright.sync_api import sync_playwright
from visa import Visa
import time


def run_monitor():
    with sync_playwright() as p:
        # 使用存储的登录状态来启动浏览器上下文
        browser = p.chromium.launch(headless=False)
        # 加载登录状态
        context = browser.new_context(storage_state="visa.vfsglobal.com.json")
        page = context.new_page()

        # 创建Visa类的实例，并执行自动化操作
        visa = Visa(page)
        # 调用Visa类中定义的方法，例如：
        visa.select_centre()  # 选择签证中心
        while True:
            visa.check_available_dates()  # 检查可用日期
            time.sleep(180)  # 每3分钟检查一次

        # 任务完成后关闭浏览器
        browser.close()


if __name__ == '__main__':
    run_monitor()





