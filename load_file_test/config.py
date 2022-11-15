from pathlib import Path
import sys


runtime_path = Path(sys.path[0])

UPLOADED_PATH = runtime_path / "file/" # 保存路径

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'avi', 'mp4', '']) # 允许的文件类型。
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB # 文件大小限制