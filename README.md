# One Pace Renamer

A simple, open-source renamer utility for One Pace episode collections.  
It automatically synchronizes filenames based on matching episode or chapter ranges  
and even pairs `.nfo` or `.ini` system information files with the correct `.mp4`.

## ✨ Features
- Auto-detects and renames episodes based on `[###-###]` patterns
- Copies system info files to their corresponding video
- Works recursively across subfolders
- Supports **dry run** and **commit** modes
- Now supports drag-and-drop `.exe` use on Windows

## 🧰 Usage
### 1. Python Version
```bash
python onepace_sync_names.py --recurse
