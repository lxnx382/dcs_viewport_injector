# 🎯 DCS Viewport Injector

Automatically reinjects custom **viewport configurations** into specific DCS Lua files after updates — made for **FA-18C Hornet modules** and others.

> ✈️ Developed by **lxnx382**, electronics engineer & simulator builder.

---

## 💡 What It Does

DCS updates overwrite `*_init.lua` files, which removes custom `ViewportHandling` logic (used to place MFDs or instruments on external monitors). This tool automatically:

- Detects missing viewport blocks
- Appends the required code if needed
- Creates safe timestamped backups
- Uses a simple, editable `config.json`

---

## ✅ Example Use Case

| Panel     | Path                                                                 | Viewport Name    |
|-----------|----------------------------------------------------------------------|------------------|
| IFEI      | `Mods/aircraft/FA-18C/Cockpit/Scripts/IFEI/indicator/IFEI_init.lua` | `FA_18C_IFEI`    |
| RWR (TEWS)| `Mods/aircraft/FA-18C/Cockpit/Scripts/TEWS/indicator/RWR_ALR67_init.lua` | `FA_18C_RWR` |

```lua
--ViewportHandling (automatically injected by lxnx382's script)
dofile(LockOn_Options.common_script_path.."ViewportHandling.lua")
update_screenspace_diplacement(1, true, 0)
try_find_assigned_viewport("FA_18C_IFEI")
