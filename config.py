import os
import json
import shutil

CONFIG_FILE = "settings.json"
EXAMPLE_CONFIG_FILE = "settings.example.json"


# ==========================
# 创建默认设置
# ==========================

def create_default_settings():
    if not os.path.exists(EXAMPLE_CONFIG_FILE):
        print("找不到 " + EXAMPLE_CONFIG_FILE)
        exit()

    shutil.copyfile(
        EXAMPLE_CONFIG_FILE,
        CONFIG_FILE
    )

    print("已创建默认设置：" + CONFIG_FILE)


# ==========================
# 读取设置
# ==========================

if not os.path.exists(CONFIG_FILE):
    create_default_settings()

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    SETTINGS = json.load(f)


# ==========================
# 修改设置
# ==========================

def set_setting(key, value):
    SETTINGS[key] = value
    save_settings()


# ==========================
# 保存设置
# ==========================

def save_settings():
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(
            SETTINGS,
            f,
            indent=4,
            ensure_ascii=False
        )