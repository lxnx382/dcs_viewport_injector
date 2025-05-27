import json
import shutil
import datetime
import os

# === Terminal color codes ===
class Colors:
    HEADER = "\033[95m"
    OK = "\033[92m"
    WARN = "\033[93m"
    FAIL = "\033[91m"
    RESET = "\033[0m"

# === Viewport code template ===
VIEWPORT_CODE_TEMPLATE = '''
--ViewportHandling (automatically injected by lxnx382's script)
dofile(LockOn_Options.common_script_path.."ViewportHandling.lua")
update_screenspace_diplacement(1, true, 0)
try_find_assigned_viewport("{viewport_name}")
'''.strip()

def read_config(config_file):
    if not os.path.exists(config_file):
        print(f"{Colors.FAIL}❌ Configuration file '{config_file}' not found.{Colors.RESET}")
        return None

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"{Colors.FAIL}❌ Failed to read config: {e}{Colors.RESET}")
        return None

def backup_file(file_path):
    """Creates a timestamped backup of the given file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path + f".bak_{timestamp}"
    shutil.copyfile(file_path, backup_path)
    return backup_path
