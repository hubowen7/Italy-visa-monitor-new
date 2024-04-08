# basic.py
# Playwright版本的基础操作类

from playwright.sync_api import sync_playwright
import logging

# 设置日志
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Basic:
    def __init__(self, page):
        self.page = page  # Playwright的页面对象

    def click_el(self, selector):
        """点击页面上的元素"""
        self.page.click(selector)
        logger.info(f"Clicked on element: {selector}")

    def wait_for_loading(self, selector):
        """等待元素加载完成"""
        self.page.wait_for_selector(selector, state="attached")
        logger.info(f"Element loaded: {selector}")

    def enter_message(self, message, selector):
        """在指定元素中输入信息"""
        self.page.fill(selector, message)
        logger.info(f"Entered message on element {selector}: {message}")

    def wait_for_secs(self, secs=1):
        """等待指定的秒数"""
        self.page.wait_for_timeout(secs * 1000)  # Playwright中的等待时间以毫秒为单位
        logger.info(f"Waited for {secs} seconds")


