import shutil
from datetime import datetime

NEW_CONFIG = "Host.exe-new.config"
TARGET_CONFIG = "Host.exe.config"

def extract_runtime_block(content):
    start_tag = "<runtime>"
    end_tag = "</runtime>"

    start_index = content.find(start_tag)
    end_index = content.find(end_tag)

    if start_index == -1 or end_index == -1:
        return None

    end_index += len(end_tag)
    return content[start_index:end_index]

def replace_runtime_block(target_content, new_runtime):
    start_tag = "<runtime>"
    end_tag = "</runtime>"

    start_index = target_content.find(start_tag)
    end_index = target_content.find(end_tag)

    if start_index == -1 or end_index == -1:
        raise Exception("Invalid config file structure.")

    end_index += len(end_tag)

    return target_content[:start_index] + new_runtime + target_content[end_index:]

def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    backup_name = f"{TARGET_CONFIG}.{timestamp}.bak"
    shutil.copyfile(TARGET_CONFIG, backup_name)
    print(f"Backup created: {backup_name}")

def main():
    with open(NEW_CONFIG, "r", encoding="utf-8") as f:
        new_content = f.read()

    with open(TARGET_CONFIG, "r", encoding="utf-8") as f:
        target_content = f.read()

    runtime_block = extract_runtime_block(new_content)
    if runtime_block is None:
        raise Exception("No <runtime> block found in new config.")

    create_backup()

    updated_content = replace_runtime_block(target_content, runtime_block)

    with open(TARGET_CONFIG, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Runtime block replaced successfully.")

if __name__ == "__main__":
    main()
