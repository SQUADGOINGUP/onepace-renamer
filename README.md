# 🏴‍☠️ One Pace Renamer

A simple, open-source renaming utility for **One Pace** episode collections.  
It automatically synchronizes filenames between `.mp4` episode files and their matching `.nfo` / `.ini` system information files — including automatic chapter matching and `[En Sub]` cleanup.

## Features
-  **Smart Episode Matching:** Detects and pairs files using numeric chapter or episode ranges like `[700–703]`
-  **System Info Sync:** Copies `.nfo` or `.ini` files to match their correct `.mp4` video file
-  **Automatic Cleanup:** Removes `[En Sub]` tags if not found in the system info file
-  **Recursive Search:** Scans all subfolders (e.g., Dressrosa, Wano, etc.)
-  **Dry-Run Mode:** Preview changes before committing

   Common Issues
Issue	Fix
Nothing renamed -	Ensure .mp4 and .nfo/.ini share the same number range [###–###]
Wrong matches -	Run in smaller subfolder scopes or rename ambiguous files manually
[En Sub] not removed - Only removed if not found in the matched system info file
