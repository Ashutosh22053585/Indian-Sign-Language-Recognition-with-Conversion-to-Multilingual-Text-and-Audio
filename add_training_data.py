import os
import cv2
import time

"""
Script to capture new training images for sign language gestures.
This will help you expand your dataset and improve model accuracy.
"""

# Path to your dataset directory
DATA_DIR = r'C:\Users\KIIT\Desktop\College\6thSem\MinorProj\MinorProject\datasets'

print("=" * 60)
print("SIGN LANGUAGE DATASET EXPANSION TOOL")
print("=" * 60)
print()

# Check if dataset directory exists
if not os.path.exists(DATA_DIR):
    print(f"Error: Dataset directory not found at {DATA_DIR}")
    print("Please update the DATA_DIR variable in this script.")
    exit()

print(f"Dataset directory: {DATA_DIR}")
print()

# Show existing classes
existing_classes = sorted([d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))])
print(f"Existing classes ({len(existing_classes)}):")
for i, cls in enumerate(existing_classes, 1):
    num_images = len([f for f in os.listdir(os.path.join(DATA_DIR, cls)) if f.endswith(('.jpg', '.png', '.jpeg'))])
    print(f"  {i}. {cls} ({num_images} images)")
print()

# Ask user what they want to do
print("What would you like to do?")
print("1. Add images to an existing class")
print("2. Create a new class")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == '1':
    # Add to existing class
    print("\nSelect the class to add images to:")
    for i, cls in enumerate(existing_classes, 1):
        print(f"  {i}. {cls}")
    
    class_idx = int(input("Enter class number: ").strip()) - 1
    
    if class_idx < 0 or class_idx >= len(existing_classes):
        print("Invalid class number!")
        exit()
    
    class_name = existing_classes[class_idx]
    class_dir = os.path.join(DATA_DIR, class_name)
    
elif choice == '2':
    # Create new class
    class_name = input("\nEnter new class name (e.g., 'A', 'B', '0', '1'): ").strip()
    class_dir = os.path.join(DATA_DIR, class_name)
    
    if os.path.exists(class_dir):
        print(f"Class '{class_name}' already exists!")
        print("Use option 1 to add images to existing class.")
        exit()
    
    # Create directory
    os.makedirs(class_dir)
    print(f"Created new class directory: {class_dir}")
else:
    print("Invalid choice!")
    exit()

# Ask how many images to capture
num_images = int(input(f"\nHow many images do you want to capture for class '{class_name}'? "))

# Get starting index (to avoid overwriting existing images)
existing_images = [f for f in os.listdir(class_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
if existing_images:
    # Extract numbers from filenames like "0.jpg", "1.jpg", etc.
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

print(f"\nImages will be saved starting from index {start_idx}")
print()

# Instructions
print("=" * 60)
print("INSTRUCTIONS:")
print("=" * 60)
print("1. Position your hand to show the gesture clearly")
print("2. Keep your hand steady when the camera captures")
print("3. Try different:")
print("   - Hand positions (left, center, right)")
print("   - Distances from camera (near, far)")
print("   - Lighting conditions")
print("   - Backgrounds")
print("4. Press 'q' at any time to quit")
print("=" * 60)
print()

input("Press ENTER when you're ready to start capturing...")

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam!")
    exit()

print(f"\nCapturing {num_images} images for class '{class_name}'...")
print("Get ready!\n")

captured_count = 0

for i in range(num_images):
    print(f"Image {i + 1}/{num_images} - Get ready...")
    
    # Countdown
    for countdown in range(3, 0, -1):
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame!")
            break
        
        # Display countdown on frame
        display_frame = frame.copy()
        cv2.putText(display_frame, f"Class: {class_name}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(display_frame, f"Image {i + 1}/{num_images}", (10, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(display_frame, f"Capturing in: {countdown}", (10, 120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        
        cv2.imshow('Capture Training Data', display_frame)
        cv2.waitKey(1000)  # Wait 1 second
    
    # Capture the image
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame!")
        break
    
    # Display "CAPTURED!" message
    display_frame = frame.copy()
    cv2.putText(display_frame, "CAPTURED!", (10, 120), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
    cv2.imshow('Capture Training Data', display_frame)
    cv2.waitKey(500)  # Show for 0.5 seconds
    
    # Save the image
    img_path = os.path.join(class_dir, f'{start_idx + i}.jpg')
    cv2.imwrite(img_path, frame)
    print(f"✓ Saved: {img_path}")
    
    captured_count += 1
    
    # Short pause before next capture
    time.sleep(0.5)
    
    # Check for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\nCapture interrupted by user.")
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()

print()
print("=" * 60)
print("CAPTURE COMPLETE!")
print("=" * 60)
print(f"Captured {captured_count} images for class '{class_name}'")
print(f"Images saved to: {class_dir}")
print()
print("NEXT STEPS:")
print("1. Run 'step2.py' to regenerate the dataset with new images")
print("2. Run 'step4RFC.py' to retrain the model")
print("3. Test the improved model with 'step5RFC.py'")
print("=" * 60)
