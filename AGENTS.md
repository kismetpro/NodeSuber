# 项目概况

这是一个异步的 Python 项目，用于管理 V2Ray 配置。它从 `config.json` 中定义的 URL 列表中获取订阅链接，然后将它们按协议分类。

# 技术栈

- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

# 命令

要运行该项目，请使用以下命令：

```bash
python main.py
```
所有配置都在 `config.json` 中处理。

# 架构

该项目是一个由 `config.json` 驱动的数据处理流水线：
1. `app_logic.py`：获取并解码订阅链接。
2. `sort_logic.py`：对解码后的配置进行分类。
3. `utils.py`：提供辅助函数。

# 代码风格

- PEP 8
- 双语（英语/中文）日志和注释

# 测试

- 该项目目前没有测试设置。