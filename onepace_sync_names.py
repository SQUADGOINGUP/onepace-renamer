import os
import re
import shutil
import argparse

def normalize(s):
    """Normalize a string for easier matching."""
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def extract_range(filename):
    """Extract the numeric episode/chapter range like [700-703]."""
    match = re.search(r'\[(\d+)(?:-(\d+))?\]', filename)
    if match:
        start, end = match.groups()
        return int(start), int(end or start)
    return None

def remove_en_sub(name):
    """Remove '[En Sub]' tag if it exists."""
    return re.sub(r'\s*\[En Sub\]', '', name, flags=re.IGNORECASE)

def find_best_match(file, candidates):
    """Find the best match among candidates based on numeric overlap."""
    file_range = extract_range(file)
    if not file_range:
        return None
    f_start, f_end = file_range
    for candidate in candidates:
        c_range = extract_range(candidate)
        if c_range and not ('Chapter' in file and not 'Chapter' in candidate):
            c_start, c_end = c_range
            # Overlapping numeric range
            if not (f_end < c_start or f_start > c_end):
                return candidate
    return None

def sync_names(root, dry_run=True):
    renamed, skipped, unresolved = 0, 0, 0
    all_files = []
    
    for dirpath, _, files in os.walk(root):
        for f in files:
            all_files.append(os.path.join(dirpath, f))

    video_files = [f for f in all_files if f.lower().endswith(('.mp4', '.mkv', '.avi'))]
    system_files = [f for f in all_files if f.lower().endswith(('.nfo', '.ini'))]

    for video in video_files:
        vdir, vfile = os.path.split(video)
        match = find_best_match(vfile, [os.path.basename(s) for s in system_files])

        if match:
            source_path = next(s for s in system_files if os.path.basename(s) == match)
            ext = os.path.splitext(source_path)[1]
            target_name = os.path.splitext(vfile)[0] + ext
            target_name = remove_en_sub(target_name)
            target_path = os.path.join(vdir, target_name)

            if dry_run:
                print(f"[RENAME] {match} -> {target_name}")
            else:
                shutil.move(source_path, target_path)
            renamed += 1
        else:
            unresolved += 1

    print(f"\n✅ Done [{'DRY-RUN' if dry_run else 'LIVE'}] – renamed: {renamed}, unresolved: {unresolved}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync One Pace episode filenames with system info files.")
    parser.add_argument("path", nargs="?", default=".", help="Path to folder (default: current)")
    parser.add_argument("--recurse", action="store_true", help="Scan subfolders recursively")
    parser.add_argument("--live", action="store_true", help="Apply changes (default: dry run)")
    args = parser.parse_args()

    sync_names(args.path, dry_run=not args.live)
