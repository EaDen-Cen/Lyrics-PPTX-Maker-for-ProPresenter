import os
import json

CONFIG_FILE = "settings.json"

# 读取.json文件数据

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        SETTINGS = json.load(f)
else:
    print("找不到 " + CONFIG_FILE)
    exit()

# 设置.json文件数据

def set_setting(key, value):
    SETTINGS[key] = value
    save_settings()

# 保存.json文件数据

def save_settings():
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(
            SETTINGS,
            f,
            indent=4,
            ensure_ascii=False
        )