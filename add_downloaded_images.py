import os
import shutil
from pathlib import Path

"""
Helper script to add downloaded images to your dataset.
This script helps you organize downloaded hand sign images into the correct folder structure.
"""

# Path to your dataset directory
DATA_DIR = r'C:\Users\KIIT\Desktop\College\6thSem\MinorProj\MinorProject\datasets'

print("=" * 70)
print("ADD DOWNLOADED IMAGES TO DATASET")
print("=" * 70)
print()

# Check if dataset directory exists
if not os.path.exists(DATA_DIR):
    print(f"❌ Error: Dataset directory not found at {DATA_DIR}")
    print("Please update the DATA_DIR variable in this script.")
    exit()

print(f"Dataset directory: {DATA_DIR}")
print()

# Show existing classes
existing_classes = sorted([d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))])
print(f"📊 Existing classes ({len(existing_classes)}):")
for i, cls in enumerate(existing_classes, 1):
    num_images = len([f for f in os.listdir(os.path.join(DATA_DIR, cls)) if f.endswith(('.jpg', '.png', '.jpeg'))])
    print(f"  {cls} ({num_images} images)", end="")
    if i % 6 == 0:
        print()
    else:
        print(" | ", end="")
print("\n")

# Ask user what they want to do
print("What would you like to do?")
print("1. Add downloaded images to an EXISTING gesture class")
print("2. Create a NEW gesture class with downloaded images")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == '1':
    # Add to existing class
    print("\nSelect the gesture class:")
    for i, cls in enumerate(existing_classes, 1):
        print(f"  {i}. {cls}")
    
    class_idx = int(input("Enter class number: ").strip()) - 1
    
    if class_idx < 0 or class_idx >= len(existing_classes):
        print("❌ Invalid class number!")
        exit()
    
    class_name = existing_classes[class_idx]
    class_dir = os.path.join(DATA_DIR, class_name)
    
elif choice == '2':
    # Create new class
    class_name = input("\nEnter new gesture name (e.g., 'HELLO', 'PEACE'): ").strip().upper()
    class_dir = os.path.join(DATA_DIR, class_name)
    
    if os.path.exists(class_dir):
        print(f"⚠️  Class '{class_name}' already exists!")
        print("Images will be added to existing class.")
    else:
        os.makedirs(class_dir)
        print(f"✓ Created new class directory: {class_dir}")
else:
    print("❌ Invalid choice!")
    exit()

print()
print("=" * 70)
print(f"Adding images to: {class_name}")
print("=" * 70)
print()

# Ask for source directory
print("Where are your downloaded images located?")
print("Enter the full path to the folder containing the images:")
print("Example: C:\\Users\\KIIT\\Downloads\\sign_language_images\\A")
print()
source_dir = input("Source folder path: ").strip()

# Remove quotes if user copied path with quotes
source_dir = source_dir.strip('"').strip("'")

if not os.path.exists(source_dir):
    print(f"❌ Error: Source directory not found: {source_dir}")
    exit()

# Get all image files from source directory
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
source_images = [f for f in os.listdir(source_dir) if f.lower().endswith(image_extensions)]

if not source_images:
    print(f"❌ No image files found in {source_dir}")
    print(f"Looking for files with extensions: {image_extensions}")
    exit()

print(f"\n✓ Found {len(source_images)} images in source folder")
print()

# Get starting index for new images
existing_images = [f for f in os.listdir(class_dir) if f.lower().endswith(image_extensions)]
if existing_images:
    # Extract numbers from filenames
    existing_numbers = []
    for img in existing_images:
        try:
            num = int(os.path.splitext(img)[0])
            existing_numbers.append(num)
        except ValueError:
            pass
    
    if existing_numbers:
        start_idx = max(existing_numbers) + 1
    else:
        start_idx = len(existing_images)
else:
    start_idx = 0

print(f"Starting index for new images: {start_idx}")
print()

# Ask for confirmation
print("=" * 70)
print("SUMMARY:")
print("=" * 70)
print(f"Gesture class: {class_name}")
print(f"Source folder: {source_dir}")
print(f"Number of images to copy: {len(source_images)}")
print(f"Destination: {class_dir}")
print(f"New images will be numbered from {start_idx} to {start_idx + len(source_images) - 1}")
print("=" * 70)
print()

confirm = input("Proceed with copying? (y/n): ").strip().lower()

if confirm != 'y':
    print("❌ Operation cancelled.")
    exit()

# Copy and rename images
print()
print("📋 Copying images...")
print()

copied_count = 0
failed_count = 0

for i, img_file in enumerate(source_images):
    try:
        # Source path
        src_path = os.path.join(source_dir, img_file)
        
        # Get file extension
        _, ext = os.path.splitext(img_file)
        
        # Destination path with new sequential name
        dst_path = os.path.join(class_dir, f"{start_idx + i}{ext}")
        
        # Copy file
        shutil.copy2(src_path, dst_path)
        
        copied_count += 1
        
        # Progress indicator
        if (i + 1) % 10 == 0:
            print(f"  ✓ Copied {i + 1}/{len(source_images)} images...")
    
    except Exception as e:
        print(f"  ❌ Failed to copy {img_file}: {e}")
        failed_count += 1

print()
print("=" * 70)
print("✅ COPY COMPLETE!")
print("=" * 70)
print(f"Successfully copied: {copied_count} images")
if failed_count > 0:
    print(f"Failed: {failed_count} images")
print(f"Total images in '{class_name}': {len(os.listdir(class_dir))}")
print()

print("=" * 70)
print("📋 NEXT STEPS:")
print("=" * 70)
print()
print("1. VERIFY images were copied correctly:")
print(f"   Check folder: {class_dir}")
print()
print("2. If you added a NEW gesture class, UPDATE labels_dict:")
print("   python update_labels.py")
print()
print("3. REGENERATE dataset with new images:")
print("   python step2.py")
print()
print("4. RETRAIN model:")
print("   python step4RFC.py")
print()
print("5. TEST the improved model:")
print("   python step5RFC.py")
print()
print("=" * 70)
print()
print("💡 TIP: Check a few images in the folder to make sure they look correct!")
print("=" * 70)
