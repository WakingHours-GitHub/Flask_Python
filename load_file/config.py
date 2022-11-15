from pathlib import Path
import sys
runtime_path = Path(sys.path[0])

UPLOAD_FOLDER = runtime_path / "file/" # 保存路径

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'avi', 'mp4', '']) # 允许的文件类型。
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB # 文件大小限制



image_upload_path = "image"
video_upload_path = "video"

processed_image_path = "processed_image"
processed_video_path = "processed_video"

image_limitation_list = ['png', 'jpg', 'jpeg']
video_limitation_list = ["mp4", 'avi']





