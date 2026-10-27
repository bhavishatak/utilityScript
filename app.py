import os
import shutil
from pathlib import Path

# Define file category mappings
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Archives": [".zip", ".tar", ".gz", ".rar"]
}

def organize_folder(target_dir):
    path = Path(target_dir)
    
    if not path.exists():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Organizing files in: {path.absolute()}\n")
    
    for item in path.iterdir():
        if item.is_dir():
            continue  # Skip subdirectories
            
        file_ext = item.suffix.lower()
        moved = False
        
        for category, extensions in DIRECTORIES.items():
            if file_ext in extensions:
                category_dir = path / category
                category_dir.mkdir(exist_ok=True)
                
                dest_path = category_dir / item.name
                shutil.move(str(item), str(dest_path))
                print(f"Moved: {item.name} ➡️ {category}/")
                moved = True
                break
        
        if not moved:
            # Move uncategorized files into an "Others" folder
            other_dir = path / "Others"
            other_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(other_dir / item.name))
            print(f"Moved: {item.name} ➡️ Others/")

    print("\n✅ Organization complete!")

if __name__ == "__main__":
    # Change this to the path you want to organize (e.g., your Downloads folder)
    target = input("Enter the folder path to organize: ").strip()
    if target:
        organize_folder(target)