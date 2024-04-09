# visa.py
from utils.basic import Basic
from utils import config
import logging
import time

# 设置日志
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Visa(Basic):
    def login(self):
        """
        登录到签证申请网站。
        """
        self.navigate(config.OPENED_PAGE)
        self.enter_message('input[name="email"]', config.EMAIL)
        self.enter_message('input[name="password"]', config.PASSWORD)
        # 假设登录按钮的选择器为'button[name="login"]'
        self.click_el('button[name="login"]')
        logger.info("Attempted to log in")

    def select_centre(self):
        """
        根据config.py中的配置选择签证中心。
        """
        # 填充相应的选择逻辑
        logger.info(f"Selected centre: {config.CENTER}")

    def check_available_dates(self):
        """
        点击页面上的“检查日期”按钮来查看是否有可用日期。
        """
        # 此处需要根据实际情况填充选择器
        self.click_el('button[name="checkDate"]')
        logger.info("Checked available dates")



