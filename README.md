## 订阅链接

- **所有配置订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/out/All_Configs_Sub.txt
  ```

- **Hysteria2 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/hy2.txt
  ```

- **Shadowsocks 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ss.txt
  ```

- **ShadowsocksR 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ssr.txt
  ```

- **Trojan 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/trojan.txt
  ```

- **Tuic 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/tuic.txt
  ```

- **Vless 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vless.txt
  ```

- **Vmess 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vmess.txt
  ```

# NodeSuber

## Project Overview
This is an asynchronous Python project for managing V2Ray configurations. It fetches subscription links from a list of URLs defined in `config.json` and then categorizes them by protocol.

## Tech Stack
- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

## Installation
To install the dependencies, run the following command:
```bash
pip install -r Files/requirements.txt
```

## Usage
To run the project, use the following command:
```bash
python main.py
```
All configurations are handled in `config.json`.

## Architecture
The project is a data processing pipeline driven by `config.json`:
1. `app_logic.py`: Fetches and decodes subscription links.
2. `sort_logic.py`: Sorts the decoded configurations.
3. `utils.py`: Provides helper functions.

## Code Style
- PEP 8
- Bilingual (English/Chinese) logging and comments

## Testing
- This project currently has no test setup.

---

# NodeSuber

## 项目概况
这是一个异步的 Python 项目，用于管理 V2Ray 配置。它从 `config.json` 中定义的 URL 列表中获取订阅链接，然后将它们按协议分类。

## 技术栈
- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

## 安装
要安装依赖，请运行以下命令：
```bash
pip install -r Files/requirements.txt
```

## 命令
要运行该项目，请使用以下命令：
```bash
python main.py
```
所有配置都在 `config.json` 中处理。

## 架构
该项目是一个由 `config.json` 驱动的数据处理流水线：
1. `app_logic.py`：获取并解码订阅链接。
2. `sort_logic.py`：对解码后的配置进行分类。
3. `utils.py`：提供辅助函数。

## 代码风格
- PEP 8
- 双语（英语/中文）日志和注释

## 测试
- 该项目目前没有测试设置。