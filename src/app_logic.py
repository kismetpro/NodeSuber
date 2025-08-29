import asyncio
import aiohttp
import json
import logging
import os
from .utils import decode_base64

# Constants
CONFIG_FILE = 'config.json'
TIMEOUT = 15  # seconds

async def fetch_url(session, url):
    """
    Fetches content from a URL asynchronously and logs its status.
    """
    try:
        async with session.get(url, timeout=TIMEOUT) as response:
            if response.status == 200:
                logging.info(f"[VALID] {url}")
                return await response.read()
            else:
                logging.info(f"[INVALID] {url}")
                logging.warning(f"Failed to fetch {url}: Status {response.status} / 获取 {url} 失败：状态 {response.status}")
                return None
    except Exception as e:
        logging.info(f"[INVALID] {url}")
        logging.error(f"Error fetching {url}: {e} / 获取 {url} 时出错：{e}")
        return None

async def main():
    """
    Main asynchronous function to fetch, decode, and process configs.
    """
    # Load configuration
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        protocols = config.get("protocols", [])
        links = config.get("links", [])
        dir_links = config.get("dir_links", [])
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {CONFIG_FILE} / 配置文件未找到：{CONFIG_FILE}")
        return
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {CONFIG_FILE} / 从 {CONFIG_FILE} 解码 JSON 时出错")
        return

    all_configs = []
    valid_links = 0
    invalid_links = 0

    async with aiohttp.ClientSession() as session:
        # Fetch and decode base64 links
        tasks = [fetch_url(session, link) for link in links]
        results = await asyncio.gather(*tasks)
        for i, content in enumerate(results):
            if content:
                valid_links += 1
                decoded_content = decode_base64(content)
                if decoded_content:
                    all_configs.extend(decoded_content.strip().split('\\n'))
            else:
                invalid_links += 1
        
        # Fetch direct links
        dir_tasks = [fetch_url(session, link) for link in dir_links]
        dir_results = await asyncio.gather(*dir_tasks)
        for i, content in enumerate(dir_results):
            if content:
                valid_links += 1
                all_configs.extend(content.decode('utf-8').strip().split('\\n'))
            else:
                invalid_links += 1

    # Filter and remove duplicates
    seen_configs = set()
    filtered_configs = []
    for config in all_configs:
        config = config.strip()
        if config and not config.startswith('#') and any(p in config for p in protocols):
            if config not in seen_configs:
                filtered_configs.append(config)
                seen_configs.add(config)

    logging.info(f"Found {len(filtered_configs)} unique configs. / 找到 {len(filtered_configs)} 个独立配置。")

    # Ensure output directory exists
    output_dir = 'out'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write to output file
    output_path = os.path.join(output_dir, 'All_Configs_Sub.txt')
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for config in filtered_configs:
                f.write(config + '\\n')
        logging.info(f"Successfully wrote configs to {output_path} / 成功将配置写入 {output_path}")
    except IOError as e:
        logging.error(f"Failed to write to {output_path}: {e} / 写入 {output_path} 失败：{e}")

    # Log summary
    total_links = len(links) + len(dir_links)
    logging.info("\n\n---")
    logging.info(f"Total Links: {total_links}")
    logging.info(f"Valid: {valid_links}")
    logging.info(f"Invalid: {invalid_links}")

if __name__ == '__main__':
    asyncio.run(main())