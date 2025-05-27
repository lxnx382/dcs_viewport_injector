import os
from dcs_viewport_injector.utils import Colors, read_config, backup_file, VIEWPORT_CODE_TEMPLATE

def patch_file(file_path, viewport_name):
    """Appends the viewport code to the Lua file if not already present."""
    if not os.path.exists(file_path):
        print(f"{Colors.FAIL}❌ File not found: {file_path}{Colors.RESET}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if f'try_find_assigned_viewport("{viewport_name}")' in content:
        print(f"{Colors.WARN}⏭️  Viewport '{viewport_name}' already present in {file_path}{Colors.RESET}")
        return

    backup = backup_file(file_path)
    code_to_add = VIEWPORT_CODE_TEMPLATE.format(viewport_name=viewport_name)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + code_to_add + "\n")

    print(f"{Colors.OK}✅ Viewport '{viewport_name}' added to {file_path} (Backup: {backup}){Colors.RESET}")

def run_injection(config_path="config.json"):
    print(f"{Colors.HEADER}🔧 DCS Viewport Injector by Lennart\n{Colors.RESET}")

    config = read_config(config_path)
    if not config:
        return

    for entry in config:
        patch_file(entry["file"], entry["viewport"])

    print(f"\n{Colors.HEADER}🚀 Injection complete. Happy flying! – Lennart{Colors.RESET}")
