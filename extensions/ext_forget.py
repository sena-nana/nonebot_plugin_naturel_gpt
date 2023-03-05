from .Extension import Extension


# 拓展的配置信息，用于ai理解拓展的功能 *必填*
ext_config:dict = {
    "name": "forget",   # 拓展名称，用于标识拓展
    "arguments": {
        'key': 'str',   # 记忆的键
        'value': 'str', # 记忆的值
    },
    "description": "Delete the memory according to the key. (usage in response: /#forget&topic#/)))",
    # 参考词，用于上下文参考使用，为空则每次都会被参考(消耗token)
    "refer_word": [],
    # 每次消息回复中最大调用次数，不填则默认为99
    "max_call_times_per_msg": 5,
    # 作者信息
    "author": "KroMiose",
    # 版本
    "version": "0.0.1",
    # 拓展简介
    "intro": "主动遗忘模块",
}

class CustomExtension(Extension):
    async def call(self, arg_dict: dict, ctx_data: dict) -> dict:
        """ 当拓展被调用时执行的函数 *由拓展自行实现*
        
        参数:
            arg_dict: dict, 由ai解析的参数字典 {参数名: 参数值(类型为str)}
        """
        custom_config:dict = self.get_custom_config()  # 获取yaml中的配置信息

        # 从arg_dict中获取参数
        key = arg_dict.get('key', None)
        if key is None:
            raise ValueError('记忆的键不能为空')

        return {
            'memory': {'key': key},
        }

    def __init__(self, custom_config: dict):
        super().__init__(ext_config.copy(), custom_config)
