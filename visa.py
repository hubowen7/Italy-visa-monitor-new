# visa.py
# 使用Playwright重写的Visa类，适用于处理签证申请流程

from utils.basic import Basic
from utils import config
import logging

# 配置日志记录器
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Visa(Basic):
    def __init__(self, page):
        """
        初始化Visa类的实例。
        :param page: Playwright的Page对象，用于页面操作。
        """
        super().__init__(page)

    def open_page(self):
        """
        打开配置文件中指定的URL。
        """
        self.page.goto(config.OPENED_PAGE)
        logger.info(f"Opened page: {config.OPENED_PAGE}")

    def login(self):
        """
        使用配置文件中的电子邮件和密码登录。
        """
        # 根据实际页面元素调整选择器
        self.page.fill('input[name="email"]', config.EMAIL)
        self.page.fill('input[name="password"]', config.PASSWORD)

        # 点击登录按钮，这里的选择器也需要根据实际页面调整
        self.page.click('text="Log in"')  # 假设登录按钮包含文本“Log in”
        logger.info("Attempted to log in with provided credentials.")

    def select_centre(self):
        """
        根据配置文件中的信息选择签证中心。
        """
        # 注意：以下选择器和操作过程需要根据实际页面的结构和需求进行调整
        self.wait_for_secs(2)
        self.page.select_option('select[name="JurisdictionId"]', config.CENTER[0])
        self.wait_for_secs(2)
        self.page.select_option('select[name="centerId"]', config.CENTER[1])
        self.wait_for_secs(2)
        self.page.select_option('select[name="category"]', config.CENTER[2])
        self.wait_for_secs(2)
        self.click_el('text="Check Dates"')  # 假设检查日期的按钮包含文本“Check Dates”
        logger.info(f"Selected centre with provided configuration: {config.CENTER}")

    def check_available_dates(self):
        """
        检查并返回可用的预约日期。
        :return: 一个包含可用日期的字典。
        """
        # 这个方法的实现将高度依赖于具体的网页结构和逻辑。
        # 你需要根据实际情况来编写代码以获取可用的预约日期。
        available_dates = {}
        # 示例代码：点击并解析日期选择器中的可用日期
        # 注意：实际实现需要根据网页结构调整
        logger.info("Checked available dates")
        return available_dates



