#!/usr/bin/env python3
"""
File Renaming Script for Swarna Panchayat Repository

This script renames Excel files to follow consistent naming conventions
and removes spaces and special characters that can cause issues.

⚠️ LEGAL DISCLAIMER:
EDUCATIONAL PURPOSE ONLY: These scripts are created solely for educational and learning purposes.
They are NOT authorized for use in automating government services without proper authorization.
USE AT YOUR OWN RISK: Users are responsible for legal compliance.
"""

import os
import shutil
from pathlib import Path

def rename_files():
    """Rename Excel files to follow consistent naming conventions."""
    
    # Define the renaming mappings
    rename_mappings = {
        "Pedapalem HT 2024-25 (1) (2).xlsx": "pedapalem_ht_2024_25.xlsx",
        "ARREAR FILE TAB4.xlsx": "arrear_file_tab4.xlsx",
        "FINAL TAB2.xlsx": "final_tab2.xlsx",
        "TAB1.xlsx": "tab1_data.xlsx",
        "TAB4.xlsx": "tab4_tax_data.xlsx"
    }
    
    print("🔄 Starting file renaming process...")
    print("=" * 50)
    
    # Create backup directory
    backup_dir = Path("backup_original_files")
    backup_dir.mkdir(exist_ok=True)
    print(f"📁 Created backup directory: {backup_dir}")
    
    renamed_count = 0
    skipped_count = 0
    
    for old_name, new_name in rename_mappings.items():
        if os.path.exists(old_name):
            # Create backup
            backup_path = backup_dir / old_name
            shutil.copy2(old_name, backup_path)
            print(f"💾 Backed up: {old_name} → {backup_path}")
            
            # Rename file
            try:
                os.rename(old_name, new_name)
                print(f"✅ Renamed: {old_name} → {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"❌ Failed to rename {old_name}: {e}")
                # Restore from backup
                shutil.copy2(backup_path, old_name)
                print(f"🔄 Restored: {old_name}")
        else:
            print(f"⚠️  File not found: {old_name}")
            skipped_count += 1
    
    print("=" * 50)
    print(f"📊 Renaming Summary:")
    print(f"   ✅ Successfully renamed: {renamed_count} files")
    print(f"   ⚠️  Skipped: {skipped_count} files")
    print(f"   💾 Backups stored in: {backup_dir}")
    
    if renamed_count > 0:
        print("\n🔧 Next Steps:")
        print("   1. Update script file paths to use new names")
        print("   2. Test scripts with renamed files")
        print("   3. Remove backup directory if everything works")
        print("\n📝 Files that need path updates in scripts:")
        for old_name, new_name in rename_mappings.items():
            if os.path.exists(new_name):
                print(f"   - {old_name} → {new_name}")

def update_script_paths():
    """Update file paths in Python scripts to use new file names."""
    
    script_updates = {
        "tab1.py": {
            "TAB1.xlsx": "tab1_data.xlsx"
        },
        "tab2.py": {
            "FINAL TAB2.xlsx": "final_tab2.xlsx"
        },
        "tab3.py": {
            "Pedapalem HT 2024-25 (1) (2).xlsx": "pedapalem_ht_2024_25.xlsx"
        },
        "tab4.py": {
            "Pedapalem HT 2024-25 (1) (2).xlsx": "pedapalem_ht_2024_25.xlsx"
        },
        "enroll_assesment_adjustment.py": {
            "TAB4.xlsx": "tab4_tax_data.xlsx",
            "ARREAR FILE TAB4.xlsx": "arrear_file_tab4.xlsx"
        }
    }
    
    print("\n🔧 Updating script file paths...")
    print("=" * 50)
    
    for script_file, path_updates in script_updates.items():
        if os.path.exists(script_file):
            print(f"📝 Updating {script_file}...")
            
            # Read script content
            with open(script_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply updates
            updated_content = content
            for old_path, new_path in path_updates.items():
                if old_path in content:
                    updated_content = updated_content.replace(old_path, new_path)
                    print(f"   ✅ {old_path} → {new_path}")
                else:
                    print(f"   ⚠️  Path not found: {old_path}")
            
            # Write updated content
            if updated_content != content:
                with open(script_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"   💾 Updated {script_file}")
            else:
                print(f"   ℹ️  No changes needed in {script_file}")
        else:
            print(f"⚠️  Script not found: {script_file}")

def main():
    """Main function to run the file renaming process."""
    
    print("🚀 Swarna Panchayat File Renaming Tool")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not any(f.endswith('.xlsx') for f in os.listdir('.')):
        print("❌ No Excel files found in current directory!")
        print("   Please run this script from the repository root directory.")
        return
    
    # Ask for confirmation
    print("This tool will:")
    print("1. Rename Excel files to follow consistent naming conventions")
    print("2. Create backups of original files")
    print("3. Update Python script file paths")
    print("4. Remove spaces and special characters from filenames")
    
    response = input("\nDo you want to proceed? (y/N): ").strip().lower()
    
    if response in ['y', 'yes']:
        rename_files()
        update_script_paths()
        print("\n🎉 File renaming process completed!")
    else:
        print("❌ Operation cancelled by user.")

if __name__ == "__main__":
    main()
