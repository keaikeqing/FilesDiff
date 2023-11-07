# 对比两个文件是否完全一致
1. 对比两个文件：修改两个文件目录
2. 对比文件和哈希值：修改文件目录和哈希算法及哈希值

### TODO
-[ ] 打包为可执行文件

### python打包为exe文件
```shell
pyinstaller --onefile --noconsole --icon=rename.ico --add-data="rename.ico;." rename_files_tk.py -n rename
```
1. pyinstaller: 这是用于调用 PyInstaller 程序的命令。 
2. --onefile: 这个选项告诉 PyInstaller 将所有的代码、库和依赖打包成单个可执行文件。默认情况下，PyInstaller 会创建一个包含多个文件的文件夹，但使用 --onefile 会创建一个独立的文件，使分发和运行变得更加简单。 
3. --noconsole: 该选项用于 Windows 系统，意味着当可执行文件运行时，不会打开命令行窗口。这对于图形用户界面(GUI)应用程序很有用，因为你通常不希望看到背后的控制台窗口。 
4. --icon=rename.ico: 这告诉 PyInstaller 你想使用 rename.ico 作为打包应用的图标。这个图标将显示在 Windows 系统中的可执行文件上。 
5. --add-data="rename.ico;.": 这个选项用于向打包的应用程序添加额外的文件。在这里，rename.ico 是要添加的文件，. 表示这个文件应该被添加到可执行文件的根目录中。在 --add-data 中，分号 ; 在 Windows 中用作路径分隔符，而在 Linux 和 macOS 中应该使用冒号 :。 
6. rename_files_tk.py: 这是你的 Python 脚本的名称，它包含了你的 Tkinter 代码，PyInstaller 将会打包这个脚本。 
7. -n rename: 这个选项指定了输出文件的名称，即打包后生成的可执行文件将被命名为 rename。
##### 获取资源
```python
# 获取当前可执行文件的目录
import sys
import os
# 当用 PyInstaller 打包时，如果程序被“冻结”（也就是被打包成一个文件），sys.frozen 的值为 True，否则为 False。
if getattr(sys, 'frozen', False):
    # 当前目录为当前可执行文件所在目录
    application_path = sys._MEIPASS
else:
    # 当前目录为当前脚本所在目录
    application_path = os.path.dirname(__file__)
# 获取资源文件的路径
icon_path = os.path.join(application_path, 'rename.ico')
```