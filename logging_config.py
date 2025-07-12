import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import os

def setup_logging(app_name, log_level=logging.DEBUG, log_file='app.log'):
    # 確保日誌檔案的目錄存在
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)  # 創建目錄，如果不存在
        
    # 創建日誌記錄器
    logger = logging.getLogger(app_name)
    logger.setLevel(log_level)
    if not logger.handlers:  # 只加一次 handler
        fh = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # logger.propagate = False  # 防止訊息往上傳

    # 避免重複添加處理器
    # if not logger.handlers:
    #     # 設置日誌格式
    #     formatter = logging.Formatter(
    #         '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    #     )

        # # 控制台處理器
        # stream_handler = logging.StreamHandler()
        # stream_handler.setFormatter(formatter)
        # logger.addHandler(stream_handler)

        # # 檔案處理器（按大小輪替）
        # file_handler = RotatingFileHandler(
        #     log_file,
        #     maxBytes=1000000,  # 1MB
        #     backupCount=5
        # )
        # file_handler.setFormatter(formatter)
        # logger.addHandler(file_handler)

        # # 可選：按時間輪替的檔案處理器
        # timed_file_handler = TimedRotatingFileHandler(
        #     log_file,
        #     when='midnight',
        #     interval=1,
        #     backupCount=7
        # )
        # timed_file_handler.setFormatter(formatter)
        # logger.addHandler(timed_file_handler)

    # logger.propagate = False  # 防止訊息往上傳

    return logger