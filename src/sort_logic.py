import os
import json
import logging
from .utils import decode_base64

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sort_configs():
    """
    Sorts V2Ray configurations from a source file into separate files based on their protocol.
    """
    ptt = os.path.abspath(os.path.join(os.getcwd()))
    
    # Load configuration from config.json
    try:
        with open(os.path.join(ptt, 'config.json'), 'r') as f:
            config_data = json.load(f)
            protocols = config_data.get("protocols", [])
    except FileNotFoundError:
        logging.error("config.json not found. / 未找到 config.json。")
        return
    except json.JSONDecodeError:
        logging.error("Error decoding config.json. / 解码 config.json 时出错。")
        return

    output_dir = os.path.join(ptt, 'Splitted-By-Protocol')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Clear existing protocol files
    for protocol in protocols:
        file_path = os.path.join(output_dir, f'{protocol}.txt')
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                pass  # This will clear the file
        except IOError as e:
            logging.error(f"Error clearing/writing header to file {file_path}: {e} / 清除/写入文件头到 {file_path} 时出错：{e}")
            
    # Read from local All_Configs_Sub.txt file
    local_config_file = os.path.join(ptt, 'out', 'All_Configs_Sub.txt')
    
    # Initialize a counter for each protocol
    protocol_counts = {protocol: 0 for protocol in protocols}

    try:
        with open(local_config_file, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                for protocol in protocols:
                    if line.startswith(protocol):
                        output_file = os.path.join(output_dir, f'{protocol}.txt')
                        try:
                            with open(output_file, 'a', encoding='utf-8') as f_out:
                                f_out.write(line)
                            protocol_counts[protocol] += 1
                        except IOError as e:
                            logging.error(f"Error writing to {output_file}: {e} / 写入 {output_file} 时出错：{e}")
                        break
        
        # Log the summary
        summary_str = ", ".join([f"{count} {protocol}" for protocol, count in protocol_counts.items() if count > 0])
        logging.info(f"Sorting complete. Found: {summary_str}. / 分类完成。")

    except FileNotFoundError:
        logging.error(f"{local_config_file} not found. / 未找到 {local_config_file}。")
    except IOError as e:
        logging.error(f"Error reading {local_config_file}: {e} / 读取 {local_config_file} 时出错：{e}")

if __name__ == '__main__':
    sort_configs()