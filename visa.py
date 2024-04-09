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
        登录到签证申请网站，模拟真人行为。
        """
        self.navigate(config.OPENED_PAGE)
        time.sleep(10)
        # 等待邮箱输入框加载
        self.wait_for_loading('#mat-input-0')
        # 慢慢输入邮箱，假设每个字符之间延迟为1000毫秒
        self.type_text('#mat-input-0', config.EMAIL, 1000)
        # 慢慢输入密码，同样每个字符之间延迟为1000毫秒
        self.type_text('#mat-input-1', config.PASSWORD, 1000)
        # 假设在点击登录按钮前等待一段时间，比如1秒，来模拟真人的行为
        time.sleep(1)
        # 点击登录按钮
        self.click_el('body > app-root > div > div > app-login > section > div > div > mat-card > form > button > span.mat-button-wrapper')
        logger.info("Attempted to log in")

    def type_text(self, selector, text, delay):
        """
        在指定元素中慢慢输入文本。
        :param selector: 页面元素的选择器。
        :param text: 要输入的文本。
        :param delay: 输入每个字符之间的延迟（毫秒）。
        """
        for char in text:
            self.page.type(selector, char, delay=delay)
        logger.info(f"Typed text into element {selector}: {text}")

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




