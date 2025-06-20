
# Basic Image Processing

This repository contains implementations of basic image processing operations using Python, OpenCV, and NumPy. These tasks were completed as part of the EC7212 – Computer Vision and Image Processing course.

---

## 🧠 Tasks Overview

### 1. **Reduce Intensity Levels (Quantization)**
Reduces the number of grayscale intensity levels in an image from 256 to a user-defined number that is a power of 2 (e.g., 2, 4, 8, 16, ..., 256).

- Input: Grayscale image
- Output: Posterized image with reduced levels
- Example: 256 levels → 4 levels → Output has pixel values like 0, 64, 128, 192

### 2. **Spatial Averaging (Smoothing)**
Performs spatial filtering (blurring) using averaging kernels:
- 3×3
- 10×10
- 20×20

Effect: Smoothens the image and reduces local intensity variations.

### 3. **Image Rotation**
Rotates the input grayscale image by:
- 45 degrees using affine transformation
- 90 degrees using built-in OpenCV rotation

### 4. **Block-wise Resolution Reduction**
Simulates resolution reduction by averaging non-overlapping blocks of:
- 3×3
- 5×5
- 7×7

All pixels within a block are replaced with the average intensity of the block, producing a pixelated effect.

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/basic-image-processing.git
cd basic-image-processing
```

### 2. Set Up the Environment

```bash
pip install opencv-python numpy matplotlib
```

### 3. Run the Code

Make sure the `input/tree.png` image is present, then run:

```bash
python main.py
```

### 4. View the Results

Check the `output/` folder for processed images.

---

## 🧑‍💻 Technologies Used

- Python 3.x
- OpenCV (cv2)
- NumPy
- Matplotlib (optional visualization)

---
