# AI Python 教程

[English Version](README.md)

![Banner](public/banner.png)

欢迎来到这个互动式 Python 教程！本课程旨在带你从完全的初学者成长为一名熟练的 Python 开发者，掌握现代工具与最佳实践。

## 使用方法

本教程共分为 53 课，每课涵盖一个特定主题。每课都有独立的目录，包含两个文件：

*   `instructions.md`：包含课程内容、说明和示例的 Markdown 文件。
*   `exercise.py`（FastAPI 课程为 `main.py`）：包含练习题的 Python 文件，供你完成。

---

## 🚀 环境配置（完全新手请从这里开始！）

在运行任何 Python 代码之前，你需要先配置好开发环境。请根据你的操作系统按照以下步骤操作。

### 第一步 — 安装 Python

> **推荐：** 安装 Python **3.11 或更高版本**。

#### Windows
1. 前往 [https://www.python.org/downloads/](https://www.python.org/downloads/) 下载最新的 Python 安装包。
2. 运行安装程序。**重要：** 在点击安装前，务必勾选 **"Add Python to PATH"** 复选框。
3. 打开**命令提示符**（在开始菜单中搜索 "cmd"），验证安装：
   ```bash
   python --version
   ```

#### macOS
1. 打开**终端**（使用 `Cmd + 空格` 打开 Spotlight，搜索 "Terminal"）。
2. 推荐通过 [Homebrew](https://brew.sh/) 安装。如果尚未安装 Homebrew，请先执行：
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. 然后安装 Python：
   ```bash
   brew install python
   ```
4. 验证安装：
   ```bash
   python3 --version
   ```

#### Linux（Ubuntu / Debian）
1. 打开**终端**。
2. 执行以下命令：
   ```bash
   sudo apt update && sudo apt install python3 python3-pip -y
   ```
3. 验证安装：
   ```bash
   python3 --version
   ```

---

### 第二步 — 安装代码编辑器

一个好的代码编辑器能让你写 Python 事半功倍。我们强烈推荐 **Visual Studio Code（VS Code）**：

1. 从 [https://code.visualstudio.com/](https://code.visualstudio.com/) 下载并安装 VS Code。
2. 安装 Microsoft 出品的 **Python 扩展**（在左侧扩展面板中搜索 "Python"）。
3. 安装 **Pylance** 扩展，获得更好的代码智能提示和自动补全功能。

> **提示：** 打开 VS Code 后，按 `Ctrl+` `` ` ``（Windows/Linux）或 `Cmd+` `` ` ``（macOS）可打开内置终端，无需离开编辑器即可运行 Python 命令。

---

### 第三步 — 获取本课程

**方式 A — 下载 ZIP 压缩包（适合初学者）：**
1. 点击本 GitHub 页面顶部的绿色 **Code** 按钮。
2. 选择 **Download ZIP**，然后将压缩包解压到你喜欢的位置。
3. 打开 VS Code，选择 **文件 → 打开文件夹**，然后选中解压后的文件夹。

**方式 B — 使用 Git 克隆（推荐给了解 Git 的用户）：**
```bash
git clone https://github.com/unrealandychan/learn-python-with-ai.git
cd learn-python-with-ai
```

---

### 第四步 — （可选但推荐）安装 `uv` 依赖管理工具

`uv` 是一个极速的 Python 包管理器，将在第 50 课中详细介绍。提前安装它，可以方便地在后续课程中安装所需的第三方包。

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows（PowerShell）
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安装完成后，在课程文件夹中创建虚拟环境：
```bash
uv venv
```
然后激活虚拟环境：
```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

## 快速开始

1.  **进入课程目录：** 从 `lesson_01_intro_to_python` 开始。
2.  **阅读说明：** 打开 `instructions.md` 文件，学习相关主题。
3.  **完成练习：** 打开 `exercise.py`，编写代码完成练习。
4.  **运行代码：** 在终端中使用以下命令运行练习文件：

    ```bash
    python lesson_01_intro_to_python/exercise.py
    ```

    > 在 macOS/Linux 上，你可能需要使用 `python3` 而不是 `python`。

5.  **查看答案：** 如果卡住了，可以查看同一文件夹中的 `solution.py` —— 但请先尝试自己完成！

### 初学者小贴士

*   **不要急。** 在进入下一课之前，先确保理解当前课程的内容。
*   **手动敲代码**，而不是直接复制粘贴 —— 这样能更好地建立编程的肌肉记忆。
*   **大胆尝试。** 修改示例中的值，看看会发生什么。出错也是学习的一部分！
*   **善用 AI 辅助学习。** 遇到不懂的地方，可以向 AI 助手（如 GitHub Copilot 或 ChatGPT）寻求更简单的解释。
*   **认真阅读报错信息。** Python 的错误信息会告诉你哪里出了问题，以及出错的行号 —— 它们是你的朋友，不是敌人。

## 入门课程

*   **第 01 课：Python 简介** — Python 入门与 "Hello, World!"
*   **第 02 课：变量与数据类型** — 变量与数据类型
*   **第 03 课：基本运算符** — 基本运算符
*   **第 04 课：用户输入与类型转换** — 用户输入与类型转换
*   **第 05 课：条件语句** — 流程控制：条件语句
*   **第 06 课：列表** — 列表：创建、索引与切片
*   **第 07 课：列表方法** — 列表方法与操作
*   **第 08 课：for 循环** — for 循环与遍历列表
*   **第 09 课：while 循环** — while 循环
*   **第 10 课：字典** — 字典
*   **第 11 课：元组与集合** — 元组与集合
*   **第 12 课：定义与调用函数** — 定义与调用函数
*   **第 13 课：函数参数与返回值** — 函数参数与返回值
*   **第 14 课：变量作用域** — 变量作用域（局部 vs. 全局）
*   **第 15 课：模块与导入** — 模块与导入
*   **第 16 课：文件读取** — 文件 I/O：读取文件
*   **第 17 课：文件写入** — 文件 I/O：写入文件
*   **第 18 课：错误处理** — 错误处理（Try/Except）
*   **第 19 课：面向对象编程入门** — 面向对象编程简介（类与对象）
*   **第 20 课：下一步** — 下一步与项目建议

## 进阶课程

*   **第 21 课：OOP 继承** — 面向对象编程：继承
*   **第 22 课：OOP 多态** — 面向对象编程：多态与方法重写
*   **第 23 课：OOP 封装** — 面向对象编程：封装（公有、受保护、私有）
*   **第 24 课：OOP Dunder 方法** — 面向对象编程：魔术方法（Dunder Methods）
*   **第 25 课：静态方法与类方法** — 静态方法与类方法
*   **第 26 课：列表推导式** — 列表推导式
*   **第 27 课：字典与集合推导式** — 字典与集合推导式
*   **第 28 课：Lambda 函数** — Lambda 函数
*   **第 29 课：map、filter、reduce** — `map()`、`filter()` 与 `reduce()` 函数
*   **第 30 课：生成器** — 生成器与 `yield` 关键字
*   **第 31 课：装饰器** — 装饰器
*   **第 32 课：collections 模块** — `collections` 模块
*   **第 33 课：日期与时间** — 日期与时间处理（`datetime` 模块）
*   **第 34 课：JSON 数据** — JSON 数据处理（`json` 模块）
*   **第 35 课：os 与 sys 模块** — 与操作系统交互（`os` 和 `sys` 模块）
*   **第 36 课：多线程** — 多线程（`threading` 模块）
*   **第 37 课：多进程** — 多进程（`multiprocessing` 模块）
*   **第 38 课：asyncio 入门** — 异步编程入门（`asyncio`）
*   **第 39 课：async/await** — 使用 `async` 与 `await` 进行异步 I/O
*   **第 40 课：进阶项目** — 进阶项目：综合运用

## 常用 Python 第三方包

*   **第 41 课：requests 模块** — `requests` - 发送 HTTP 请求
*   **第 42 课：BeautifulSoup4** — `BeautifulSoup4` - 网页爬虫
*   **第 43 课：Pandas** — `pandas` - 数据分析
*   **第 44 课：Matplotlib** — `matplotlib` - 数据可视化
*   **第 45 课：Seaborn** — `seaborn` - 统计数据可视化
*   **第 46 课：FastAPI** — `FastAPI` - 构建 Web API

## 专业开发实践

*   **第 47 课：Git 与 GitHub** — 使用 Git 与 GitHub 进行版本控制
*   **第 48 课：Pytest** — 使用 `pytest` 进行测试
*   **第 49 课：Ruff** — 使用 `ruff` 进行代码格式化与静态检查
*   **第 50 课：uv 依赖管理** — 使用 `uv` 进行现代化依赖与环境管理
*   **第 51 课：数据库** — 数据库操作（`SQLAlchemy` + `SQLite`）
*   **第 52 课：配置管理** — 配置管理（使用 `.env` 文件）
*   **第 53 课：Python MCP 与技能** — 构建迷你 MCP 风格的工具路由器与可复用 Python 技能模块

---

祝你学习愉快！🎉
