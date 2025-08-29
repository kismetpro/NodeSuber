import asyncio
import logging
import time
from src.app_logic import main as app_main
from src.sort_logic import sort_configs as sort_main

# Configure logging
# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler for v2ray_config.log
file_handler = logging.FileHandler("v2ray_config.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(file_handler)

# Create a stream handler for console output
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

async def main():
    """
    Main function to run the entire workflow.
    """
    start_time = time.time()
    logging.info("Starting the V2Ray config processing workflow. / 开始处理 V2Ray 配置。")

    try:
        # Step 1: Run the asynchronous config fetching and aggregation
        logging.info("Running the app logic to fetch and aggregate configs... / 正在运行应用逻辑以获取和聚合配置...")
        await app_main()
        logging.info("App logic finished successfully. / 应用逻辑成功完成。")
        print("✅ Subscription sources downloaded and aggregated. / 订阅源下载和聚合完成。")

        # Step 2: Run the config sorting
        logging.info("Running the sort logic to classify configs... / 正在运行排序逻辑以对配置进行分类...")
        sort_main()
        logging.info("Sort logic finished successfully. / 排序逻辑成功完成。")
        print("✅ Configurations sorted by protocol. / 配置已按协议分类。")

    except Exception as e:
        logging.error(f"An error occurred during the workflow: {e} / 工作流程中发生错误: {e}", exc_info=True)
        print(f"❌ An error occurred. Check v2ray_config.log for details. / 发生错误。请查看 v2ray_config.log 了解详情。")
    
    end_time = time.time()
    logging.info(f"V2Ray config processing workflow finished in {end_time - start_time:.2f} seconds. / V2Ray 配置处理工作流程在 {end_time - start_time:.2f} 秒内完成。")
    print(f"🎉 Workflow complete! Total execution time: {end_time - start_time:.2f} seconds. / 工作流程完成！总执行时间：{end_time - start_time:.2f} 秒。")

if __name__ == "__main__":
    asyncio.run(main())