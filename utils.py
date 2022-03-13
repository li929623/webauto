#日志
import logging
import os
Base_Dir=os.path.dirname(os.path.abspath(__file__))
class app():
    #日志
    def log(self):
        # 创建日志器
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # 创建控制，文件处理器
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            path = Base_Dir + '/log/log.text'
            file_handler = logging.FileHandler(path, mode='a', encoding='UTF-8')
            # 设置输出格式
            console_fmt = "%(name)s****%(levelname)s****    %(message)s"
            file_fmt = "%(name)s****%(levelname)s****    %(message)s"
            # 格式话
            fmt1 = logging.Formatter(console_fmt)
            fmt2 = logging.Formatter(file_fmt)
            # 添加处理器
            console_handler.setFormatter(fmt1)
            file_handler.setFormatter(fmt2)
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
            return logger