import os

"""
Helper script to update labels_dict in your code files after adding new gesture classes.
This will automatically add new gesture labels to step5RFC.py, step6.py, and Final.py
"""

# Path to your dataset directory
DATA_DIR = r'C:\Users\KIIT\Desktop\College\6thSem\MinorProj\MinorProject\datasets'

# Files that need labels_dict updated
FILES_TO_UPDATE = [
    'step5RFC.py',
    'step6.py', 
    'Final.py'
]

print("=" * 70)
print("UPDATE LABELS_DICT HELPER")
print("=" * 70)
print()

# Get all classes from dataset directory
if not os.path.exists(DATA_DIR):
    print(f"❌ Error: Dataset directory not found at {DATA_DIR}")
    exit()

all_classes = sorted([d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))])

print(f"📊 Found {len(all_classes)} gesture classes in dataset:")
print()

# Display in columns
for i, cls in enumerate(all_classes, 1):
    print(f"  {cls}", end="")
    if i % 5 == 0:
        print()
    else:
        print(" | ", end="")
print("\n")

# Generate the new labels_dict code
print("=" * 70)
print("📝 GENERATED labels_dict CODE:")
print("=" * 70)
print()

labels_dict_code = "labels_dict = {"

# Add each class
for i, cls in enumerate(all_classes):
    if i % 3 == 0:  # New line every 3 items for readability
        labels_dict_code += "\n    "
    labels_dict_code += f"'{cls}': '{cls}', "

labels_dict_code += "\n}"

print(labels_dict_code)
print()

# Save to a file for easy copying
with open('labels_dict_code.txt', 'w') as f:
    f.write(labels_dict_code)

print("✓ Saved to 'labels_dict_code.txt'")
print()

print("=" * 70)
print("📋 MANUAL UPDATE INSTRUCTIONS:")
print("=" * 70)
print()
print("You need to update labels_dict in these files:")
for file in FILES_TO_UPDATE:
    print(f"  • {file}")
print()
print("Steps:")
print("1. Open each file")
print("2. Find the line starting with: labels_dict = {")
print("3. Replace the entire labels_dict definition with the code above")
print("4. Save the file")
print()
print("=" * 70)
print()

# Ask if user wants automatic update
print("Would you like me to automatically update these files? (y/n)")
choice = input("Enter choice: ").strip().lower()

if choice == 'y':
    print()
    print("🔄 Updating files...")
    print()
    
    for file in FILES_TO_UPDATE:
        if not os.path.exists(file):
            print(f"⚠️  Skipping {file} (file not found)")
            continue
        
        try:
            # Read the file
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find and replace labels_dict
            # Look for the pattern: labels_dict = {...}
            import re
            
            # Pattern to match labels_dict = {...} (including multiline)
            pattern = r"labels_dict\s*=\s*\{[^}]*\}"
            
            if re.search(pattern, content):
                # Replace with new labels_dict
                new_content = re.sub(pattern, labels_dict_code.replace('\n', '\n'), content)
                
                # Write back to file
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ Updated {file}")
            else:
                print(f"⚠️  Could not find labels_dict in {file}")
                print(f"   Please update manually using the code above")
        
        except Exception as e:
            print(f"❌ Error updating {file}: {e}")
            print(f"   Please update manually")
    
    print()
    print("=" * 70)
    print("✅ AUTOMATIC UPDATE COMPLETE!")
    print("=" * 70)
else:
    print()
    print("=" * 70)
    print("📋 MANUAL UPDATE REQUIRED")
    print("=" * 70)
    print()
    print("Copy the labels_dict code above and paste it into:")
    for file in FILES_TO_UPDATE:
        print(f"  • {file}")
    print()
    print("Or open 'labels_dict_code.txt' to copy from there.")

print()
print("=" * 70)
print("🎯 NEXT STEPS AFTER UPDATING:")
print("=" * 70)
print()
print("1. Regenerate dataset:")
print("   python step2.py")
print()
print("2. Retrain model:")
print("   python step4RFC.py")
print()
print("3. Test with new gestures:")
print("   python step5RFC.py")
print()
print("=" * 70)
