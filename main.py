# coding:utf-8
import os
import pytest
# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest.main(["-sq", "--alluredir", "./allure-results"])
    os.system("allure generate ./allure-results/ -o ./allure-report/ --clean")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
