# monitor.py

import time
from playwright.sync_api import sync_playwright
from utils import config
from visa import Visa
import logging

# 设置日志
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_browser():
    # 使用Playwright创建并返回一个浏览器实例
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 设置headless=False可查看浏览器界面
        logger.info("Browser launched")
        return browser

def monitor():
    try:
        browser = init_browser()
        page = browser.new_page()  # 打开一个新的浏览器页面
        visa = Visa(page)  # 创建Visa类的实例
        # 执行其他监控逻辑
    except Exception as e:
        logger.error(f"Monitor runtime error: {e}")
    finally:
        browser.close()
        logger.info("Browser closed")

if __name__ == "__main__":
    monitor()


