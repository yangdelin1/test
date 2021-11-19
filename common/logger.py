# coding:utf-8
import os
import sys
import logbook
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
from logbook import Logger, StreamHandler, FileHandler, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler


def log_type(record, handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date=record.time,  # 日志时间
        level=record.level_name,  # 日志等级
        filename=os.path.split(record.filename)[-1],  # 文件名
        func_name=record.func_name,  # 函数名
        lineno=record.lineno,  # 行号
        msg=record.message  # 日志内容
    )
    return log


# 日志存放路径

print(LOG_PATH)
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
# 日志打印到屏幕
log_std = ColorizedStderrHandler(bubble=True)
log_std.formatter = log_type
# 日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(LOG_PATH, '%s.log' % 'log'), date_format='%Y-%m-%d', bubble=True, encoding='utf-8')
log_file.formatter = log_type

# 脚本日志
run_log = Logger("global_log")


def init_logger():
    logbook.set_datetime_format("local")
    run_log.handlers = []
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_std)
    return ""


'''
日志等级：
critical    严重错误，会导致程序退出
error	    可控范围内的错误
warning	    警告信息
notice	    大多情况下希望看到的记录
info	    大多情况不希望看到的记录
debug	    调试程序时详细输出的记录
'''
# 实例化，默认调用
logger = init_logger()

if __name__ == "__main__":
    run_log.debug("测试日志模块")
