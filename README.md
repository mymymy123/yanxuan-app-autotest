# 网易严选 App UI 自动化测试

基于 Appium + Pytest 的网易严选 App UI 自动化测试项目（个人学习用途，非官方）。


## 功能特性

- 📱 支持 Android 真机 / 模拟器运行
- 🧩 Page Object 设计模式，页面元素与用例逻辑分离
- 📊 Allure 可视化测试报告，附运行截图
- 🔧 配置与代码解耦，敏感信息通过 `.env` 管理
- 📦 数据驱动测试，用例参数化覆盖多场景

## 测试范围

| 模块 | 测试脚本 | 断言点 |
|------|----------|--------|
| 启动首页 | `test_01_enter_home.py` | 成功进入 App 首页 |
| 登录 | `test_02_login.py` | 邮箱号密码登录成功 |
| 登录（参数化） | `test_02_login copy.py` | 正常/异常账号登录，校验提示文案与页面状态 |
| 搜索商品 | `test_03_search.py` | 结果列表非空且包含关键词 |
| 加入购物车 | `test_04_cart.py` | 加入购物车弹窗 / 提示出现 |

## 技术栈

| 类别 | 技术 |
|------|------|
| 语言 | Python 3.10+ |
| 自动化框架 | Appium + UiAutomator2 |
| 测试框架 | Pytest |
| 测试报告 | Allure |
| 配置管理 | environs / python-dotenv（读取 `.env`） |
| 日志 | logging（封装于 utils） |

## 目录结构

```text
├── .vscode/                  # VSCode 项目配置
├── base/                     # 页面基础操作封装（查找、点击、输入等）
├── data/                     # 参数化测试数据
├── img/                      # 测试用例运行截图
├── log/                      # 运行日志输出目录
├── lx/                       # 项目相关资源或特定模块
├── pages/                    # Page Object 页面对象
│   ├── __init__.py
│   ├── cart_page.py          # 购物车页
│   ├── enter_home_page.py    # 启动/首页
│   ├── login_page.py         # 登录页
│   └── search_page.py        # 搜索页
├── report/                   # Allure/HTML 测试报告输出目录
├── scripts/                  # 测试用例
│   ├── __init__.py
│   ├── test_01_enter_home.py # 启动首页测试
│   ├── test_02_login.py      # 登录测试
│   ├── test_02_login copy.py # 登录参数化测试
│   ├── test_03_search.py     # 搜索测试
│   └── test_04_cart.py       # 购物车测试
├── utils/                    # 工具类
│   ├── __init__.py
│   └── tools.py              # driver 封装、日志、截图等工具
├── .env                      # 环境变量（真实配置，不入库）
├── .env.example              # 环境变量示例
├── .gitignore                # Git 忽略文件配置
├── config.py                 # 全局配置（设备、包名等）
├── conftest.py               # pytest fixture（driver 初始化/销毁）
├── pytest.ini                # pytest 配置
└── README.md                 # 项目说明文档