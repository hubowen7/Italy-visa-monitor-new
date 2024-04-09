# utils/basic.py
from utils import config
import logging

# 初始化日志记录器
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Basic:
    def __init__(self, page):
        """
        初始化基础页面操作类。
        :param page: Playwright页面对象。
        """
        self.page = page

    def click_el(self, selector):
        """
        点击指定选择器的元素。
        :param selector: 页面元素的选择器。
        """
        self.page.click(selector)
        logger.info(f"Clicked element: {selector}")

    def wait_for_loading(self, selector):
        """
        等待元素加载。
        :param selector: 页面元素的选择器。
        """
        self.page.wait_for_selector(selector)
        logger.info(f"Element loaded: {selector}")

    def enter_message(self, selector, message):
        """
        在指定元素中输入文本。
        :param selector: 页面元素的选择器。
        :param message: 要输入的文本。
        """
        self.page.fill(selector, message)
        logger.info(f"Entered text into element {selector}: {message}")

    def navigate(self, url):
        """
        导航到指定URL。
        :param url: 网址。
        """
        self.page.goto(url)
        logger.info(f"Navigated to {url}")



