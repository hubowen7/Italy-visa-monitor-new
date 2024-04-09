# monitor.py
from playwright.sync_api import sync_playwright
from visa import Visa
from utils import config
import time
import logging

# 设置日志
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_monitor():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 使用非无头模式以便于观察浏览器操作
        page = browser.new_page()

        visa = Visa(page)
        visa.navigate(config.OPENED_PAGE)  # 打开签证申请页面
        visa.login()  # 执行登录操作
        visa.select_centre()  # 选择签证中心

        while True:
            try:
                visa.check_available_dates()  # 检查可用日期
                time.sleep(180)  # 每3分钟检查一次
            except KeyboardInterrupt:
                logger.info("Monitoring stopped by user.")
                break
            except Exception as e:
                logger.error(f"Error during monitoring: {e}")

        browser.close()


if __name__ == '__main__':
    run_monitor()




