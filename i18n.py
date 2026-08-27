"""
国际化 (i18n) 系统
用于管理应用程序的多语言支持

使用方式:
    from i18n import i18n
    text = i18n.t("ui.button.ok")  # 获取翻译文本
"""

import os
import json
from typing import Dict, Any, Optional
from pathlib import Path


class I18n:
    """国际化管理器"""
    
    def __init__(self, default_lang: str = "zh"):
        """
        初始化国际化系统
        
        Args:
            default_lang: 默认语言代码 (zh: 中文, en: 英文)
        """
        self.default_lang = default_lang
        self.current_lang = default_lang
        self.translations: Dict[str, Dict[str, Any]] = {}
        
        # 翻译文件目录
        self.lang_dir = Path(__file__).parent / "locales"
        
        # 初始化加载翻译
        self._load_all_languages()
    
    def _load_all_languages(self) -> None:
        """加载所有可用的语言文件"""
        if not self.lang_dir.exists():
            print(f"警告: 翻译目录不存在: {self.lang_dir}")
            return
        
        for lang_file in self.lang_dir.glob("*.json"):
            lang_code = lang_file.stem
            try:
                with open(lang_file, "r", encoding="utf-8") as f:
                    self.translations[lang_code] = json.load(f)
                print(f"✓ 已加载语言: {lang_code}")
            except Exception as e:
                print(f"✗ 加载语言文件失败 {lang_file}: {e}")
    
    def set_language(self, lang_code: str) -> bool:
        """
        切换语言
        
        Args:
            lang_code: 语言代码 (zh, en, etc.)
            
        Returns:
            是否切换成功
        """
        if lang_code not in self.translations:
            print(f"警告: 不支持的语言: {lang_code}")
            return False
        
        self.current_lang = lang_code
        print(f"✓ 已切换语言到: {lang_code}")
        return True
    
    def get_available_languages(self) -> Dict[str, str]:
        """
        获取所有可用语言
        
        Returns:
            {language_code: language_name} 字典
        """
        return {
            "zh": "中文",
            "en": "English",
            "ja": "日本語",
            "ko": "한국어",
        }
    
    def t(self, key: str, default: str = None) -> str:
        """
        获取翻译文本 (translate)
        
        使用点号表示法访问嵌套键:
            t("ui.button.ok") -> 获取 translations[lang]["ui"]["button"]["ok"]
        
        Args:
            key: 翻译键，使用点号分隔 (e.g., "ui.button.ok")
            default: 如果找不到翻译，返回默认值
            
        Returns:
            翻译的文本，或默认值，或原键名
        """
        try:
            # 分割键
            keys = key.split(".")
            
            # 在当前语言中查找
            value = self.translations[self.current_lang]
            for k in keys:
                value = value[k]
            
            return value
        except (KeyError, TypeError):
            # 如果找不到，尝试默认语言
            if self.current_lang != self.default_lang:
                try:
                    value = self.translations[self.default_lang]
                    for k in keys:
                        value = value[k]
                    return value
                except (KeyError, TypeError):
                    pass
            
            # 返回默认值或原键名
            return default or key
    
    def t_with_args(self, key: str, **args) -> str:
        """
        获取翻译文本并替换参数
        
        使用 {param} 占位符:
            t_with_args("message.error", filename="test.txt")
            -> "文件 test.txt 不存在"
        
        Args:
            key: 翻译键
            **args: 替换参数
            
        Returns:
            替换参数后的文本
        """
        text = self.t(key)
        try:
            return text.format(**args)
        except (KeyError, ValueError):
            return text
    
    def get_all(self, lang_code: str = None) -> Dict[str, Any]:
        """获取整个语言的所有翻译"""
        lang = lang_code or self.current_lang
        return self.translations.get(lang, {})


# 全局国际化实例
i18n = I18n(default_lang="zh")


# 便利函数 - 在代码中直接使用
def _(key: str, default: str = None) -> str:
    """快捷翻译函数"""
    return i18n.t(key, default)


def _args(key: str, **kwargs) -> str:
    """快捷翻译函数 - 带参数"""
    return i18n.t_with_args(key, **kwargs)
