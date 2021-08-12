# 文件 framwork_utils.py
from pathlib import Path

def router(path, method, handlers):            # URL路由装饰器
    def decorater(handler):
        handlers[method][path] = handler
        return handler
    return decorater

def load_static(static_path):                  # 加载静态文件
    statci_dict = dict()
    for f_type in ['html', 'js', 'css']:
        for file in Path(static_path).glob(f'*.{f_type}'):
            with open(file) as f:
                statci_dict[file.name] = f.read()
    return statci_dict

page404 = '''<html><head><title>404</title></head><body>
        <center><br><h1>404: page note found</h1></center>
        </body></html>'''