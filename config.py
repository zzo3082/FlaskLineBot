import os
from logging_config import setup_logging

class ZZOConfig:
    # 初始化日誌
    logger = setup_logging(app_name='ZZOConfig', log_file='logs/ZZOConfig.log')

    # ZZOConfig的屬性 兩個字串LINE_ACCESS_TOKEN LINE_CHANNEL_SECRET
    LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
    LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')

    # 方法 驗證使否有拿到環境變數
    @staticmethod
    def validate():
        if not ZZOConfig.LINE_ACCESS_TOKEN or not ZZOConfig.LINE_CHANNEL_SECRET:
            print("print > LINE_ACCESS_TOKEN or LINE_CHANNEL_SECRET is not set")
            ZZOConfig.logger.error("ZZOConfig > LINE_ACCESS_TOKEN or LINE_CHANNEL_SECRET is not set")
            raise ValueError("ValueError > LINE_ACCESS_TOKEN or LINE_CHANNEL_SECRET is not set")