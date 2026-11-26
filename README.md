# 网易严选 App UI 自动化测试

基于 Appium + Pytest 的网易严选 App UI 自动化测试项目（个人学习用途，非官方）。

## 测试范围

- 登录（手机号 + 验证码 / 账号密码）
- 搜索商品（关键词搜索，断言结果非空且包含关键词）
- 加入购物车（断言购物车数量 +1、商品名匹配）
- 登录用例参数化（数据驱动，覆盖正常/异常账号）

## 技术栈

- Python 
- Appium  + UiAutomator2
- Pytest 
- Allure（测试报告）
- environs（读取 .env 配置）

## 目录结构
├── config # 配置（设备、App 包名等）
├── data/ # 参数化测试数据
├── img/ # 测试用例截图
├── base/ # 页面基础操作（查找、点击、输入等）
├── pages/ # Page Object 页面对象
├── scripts/ # 测试用例
├── utils/ # 工具类（driver 封装、日志等）
├── conftest.py # pytest fixture
├── pytest.ini # pytest 配置
├── .env.example # 环境变量示例（真实 .env 不入库）
└── README.md