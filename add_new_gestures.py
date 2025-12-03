import os
import cv2
import time

"""
Script to add NEW gesture classes to your sign language recognition system.
Perfect for adding common words, phrases, or custom gestures beyond A-Z and 0-9.
"""

# Path to your dataset directory
DATA_DIR = r'C:\Users\KIIT\Desktop\College\6thSem\MinorProj\MinorProject\datasets'

print("=" * 70)
print("ADD NEW GESTURE CLASSES")
print("=" * 70)
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
print(f"📊 Current classes ({len(existing_classes)}):")
for i, cls in enumerate(existing_classes, 1):
    num_images = len([f for f in os.listdir(os.path.join(DATA_DIR, cls)) if f.endswith(('.jpg', '.png', '.jpeg'))])
    print(f"  {cls} ({num_images} images)", end="")
    if i % 6 == 0:  # New line every 6 classes
        print()
    else:
        print(" | ", end="")
print("\n")

# Suggest common sign language gestures
print("=" * 70)
print("💡 SUGGESTED NEW GESTURES TO ADD:")
print("=" * 70)
print()
print("Common Words:")
print("  • HELLO     • GOODBYE    • PLEASE     • THANK_YOU")
print("  • YES       • NO         • SORRY      • HELP")
print("  • WATER     • FOOD       • BATHROOM   • STOP")
print()
print("Common Phrases:")
print("  • I_LOVE_YOU    • GOOD_MORNING    • GOOD_NIGHT")
print("  • HOW_ARE_YOU   • NICE_TO_MEET_YOU")
print()
print("Useful Actions:")
print("  • EAT       • DRINK      • SLEEP      • WALK")
print("  • SIT       • STAND      • COME       • GO")
print()
print("Emotions:")
print("  • HAPPY     • SAD        • ANGRY      • CONFUSED")
print()
print("Custom Gestures:")
print("  • Any gesture you want! (e.g., PEACE, THUMBS_UP, OK)")
print("=" * 70)
print()

# Ask user what gestures to add
print("How many NEW gesture classes do you want to add?")
num_new_classes = int(input("Enter number: ").strip())

new_classes = []
for i in range(num_new_classes):
    print(f"\n--- New Gesture {i + 1}/{num_new_classes} ---")
    
    while True:
        class_name = input("Enter gesture name (e.g., HELLO, THANK_YOU, PEACE): ").strip().upper()
        
        # Validate class name
        if not class_name:
            print("❌ Class name cannot be empty!")
            continue
        
        if class_name in existing_classes:
            print(f"❌ Class '{class_name}' already exists!")
            print("   Use 'add_training_data.py' to add more images to existing classes.")
            continue
        
        if class_name in new_classes:
            print(f"❌ You already added '{class_name}' in this session!")
            continue
        
        # Valid class name
        new_classes.append(class_name)
        print(f"✓ Added '{class_name}' to the list")
        break

print()
print("=" * 70)
print("📋 SUMMARY - New Classes to Create:")
print("=" * 70)
for i, cls in enumerate(new_classes, 1):
    print(f"  {i}. {cls}")
print("=" * 70)
print()

# Ask how many images per class
print("How many images do you want to capture for EACH new gesture?")
print("Recommended: 100-200 images per gesture for good accuracy")
num_images_per_class = int(input("Enter number: ").strip())

print()
print("=" * 70)
print("📸 CAPTURE INSTRUCTIONS:")
print("=" * 70)
print("For BEST results, vary the following for each gesture:")
print()
print("1. HAND POSITION:")
print("   - Left, center, right of frame")
print("   - Top, middle, bottom of frame")
print()
print("2. DISTANCE:")
print("   - Close to camera (hand fills frame)")
print("   - Medium distance")
print("   - Far from camera (hand is smaller)")
print()
print("3. LIGHTING:")
print("   - Bright lighting (near window)")
print("   - Normal room lighting")
print("   - Dim lighting")
print()
print("4. BACKGROUND:")
print("   - Plain wall")
print("   - Cluttered background")
print("   - Different colored backgrounds")
print()
print("5. HAND VARIATIONS:")
print("   - Slight rotations")
print("   - Different angles")
print("   - Natural variations (not perfectly positioned)")
print()
print("6. BOTH HANDS (if applicable):")
print("   - Left hand")
print("   - Right hand")
print("   - Both hands (for two-handed gestures)")
print()
print("TIP: Capture in multiple sessions for maximum diversity!")
print("=" * 70)
print()

input("Press ENTER when you're ready to start capturing...")

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam!")
    exit()

# Capture images for each new class
total_captured = 0

for class_idx, class_name in enumerate(new_classes, 1):
    print()
    print("=" * 70)
    print(f"📸 CAPTURING: {class_name} ({class_idx}/{len(new_classes)})")
    print("=" * 70)
    print(f"Images to capture: {num_images_per_class}")
    print()
    
    # Create directory for this class
    class_dir = os.path.join(DATA_DIR, class_name)
    os.makedirs(class_dir, exist_ok=True)
    print(f"✓ Created directory: {class_dir}")
    print()
    
    # Show gesture description (if available)
    gesture_tips = {
        'HELLO': 'Wave your hand side to side',
        'GOODBYE': 'Wave goodbye',
        'PLEASE': 'Circular motion on chest with flat hand',
        'THANK_YOU': 'Touch chin and move hand forward',
        'YES': 'Fist moving up and down (nodding)',
        'NO': 'Index and middle finger closing (like scissors)',
        'SORRY': 'Fist circling on chest',
        'HELP': 'Thumbs up on flat palm, lift both hands',
        'I_LOVE_YOU': 'Thumb, index, and pinky extended',
        'STOP': 'Flat hand, palm facing forward',
        'PEACE': 'Index and middle finger in V shape',
        'THUMBS_UP': 'Thumb pointing up, fist closed',
        'OK': 'Thumb and index finger forming circle',
    }
    
    if class_name in gesture_tips:
        print(f"💡 TIP: {gesture_tips[class_name]}")
        print()
    
    input(f"Position your hand for '{class_name}' gesture, then press ENTER...")
    
    print(f"\n🎬 Starting capture in 3 seconds...")
    time.sleep(3)
    
    # Capture loop
    for i in range(num_images_per_class):
        # Countdown
        for countdown in range(3, 0, -1):
            ret, frame = cap.read()
            if not ret:
                print("❌ Error: Failed to capture frame!")
                break
            
            # Display info on frame
            display_frame = frame.copy()
            
            # Class info
            cv2.putText(display_frame, f"Gesture: {class_name}", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Progress
            cv2.putText(display_frame, f"Image {i + 1}/{num_images_per_class}", (10, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Class progress
            cv2.putText(display_frame, f"Class {class_idx}/{len(new_classes)}", (10, 110), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Countdown
            cv2.putText(display_frame, f"Capturing in: {countdown}", (10, 160), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            
            # Tips
            if i < num_images_per_class // 3:
                tip = "Vary POSITION (left/center/right)"
            elif i < 2 * num_images_per_class // 3:
                tip = "Vary DISTANCE (near/far)"
            else:
                tip = "Vary ANGLE (rotate slightly)"
            
            cv2.putText(display_frame, tip, (10, display_frame.shape[0] - 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            
            cv2.imshow('Add New Gestures', display_frame)
            cv2.waitKey(1000)  # Wait 1 second
        
        # Capture the image
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Failed to capture frame!")
            break
        
        # Display "CAPTURED!" message
        display_frame = frame.copy()
        cv2.putText(display_frame, "CAPTURED!", (10, 160), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
        cv2.imshow('Add New Gestures', display_frame)
        cv2.waitKey(500)  # Show for 0.5 seconds
        
        # Save the image
        img_path = os.path.join(class_dir, f'{i}.jpg')
        cv2.imwrite(img_path, frame)
        
        # Progress indicator
        if (i + 1) % 10 == 0:
            print(f"  ✓ Captured {i + 1}/{num_images_per_class} images...")
        
        total_captured += 1
        
        # Short pause before next capture
        time.sleep(0.3)
        
        # Check for quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\n⚠️ Capture interrupted by user.")
            break
    
    print(f"✅ Completed '{class_name}': {num_images_per_class} images captured")
    
    # Pause between classes
    if class_idx < len(new_classes):
        print()
        print(f"Next gesture: {new_classes[class_idx]}")
        input("Press ENTER when ready for next gesture (or Ctrl+C to stop)...")

# Release webcam
cap.release()
cv2.destroyAllWindows()

print()
print("=" * 70)
print("🎉 CAPTURE COMPLETE!")
print("=" * 70)
print(f"Total new gesture classes added: {len(new_classes)}")
print(f"Total images captured: {total_captured}")
print()
print("New gesture classes:")
for cls in new_classes:
    print(f"  ✓ {cls}")
print()
print("=" * 70)
print("📋 NEXT STEPS:")
print("=" * 70)
print()
print("1. UPDATE labels_dict in your code files:")
print("   Files to update:")
print("   • step5RFC.py")
print("   • step6.py")
print("   • Final.py")
print()
print("   Add these lines to labels_dict:")
for cls in new_classes:
    print(f"   '{cls}': '{cls}',")
print()
print("2. REGENERATE dataset:")
print("   python step2.py")
print()
print("3. RETRAIN model:")
print("   python step4RFC.py")
print()
print("4. TEST new gestures:")
print("   python step5RFC.py")
print()
print("=" * 70)
print()
print("💡 TIP: The model will now recognize {} total gestures!".format(len(existing_classes) + len(new_classes)))
print("=" * 70)
