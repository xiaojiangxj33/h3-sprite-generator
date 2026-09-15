# -*- coding: utf-8 -*-
"""游戏特效序列帧生成器 —— 只用来让 ComfyUI 伺服 web/ 目录，不注册任何节点。

ComfyUI 会把声明了 WEB_DIRECTORY 的自定义节点的那个目录挂在
/extensions/<本目录名>/ 上，所以本仓库放进 custom_nodes/ 后，
界面地址就是 http://127.0.0.1:8188/extensions/<本目录名>/h3ui.html 。

删掉整个目录 = 界面消失，不影响 ComfyUI 和其它节点。
"""

WEB_DIRECTORY = "./web"

# 空字典（不是 None）—— 纯副作用型插件显式声明，避免加载器打
# "lack of NODE_CLASS_MAPPINGS" 警告。
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

__all__ = ["WEB_DIRECTORY", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
