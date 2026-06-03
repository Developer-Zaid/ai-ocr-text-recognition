# 🧠 OCR Text Recognition System

## 📌 Overview

This project was developed as part of **Week 4 of the Artificial Intelligence Internship Program at DecodeLabs**.

The objective of this project is to build an Optical Character Recognition (OCR) system capable of extracting text from images using image preprocessing and artificial intelligence techniques.

The system processes input images, improves image quality, and converts visual text into machine-readable text.

---

## 🎯 Project Objective

Build an OCR pipeline that:

- Accepts image input
- Preprocesses images for better recognition
- Extracts text using OCR
- Generates processed output
- Displays recognized text

---

## 🧠 AI Workflow

```text
Input Image
     ↓
Image Preprocessing
     ↓
OCR Engine
     ↓
Text Extraction
     ↓
Output Generation
```

---

## ⚙️ Technologies Used

- Python 3
- OpenCV
- Tesseract OCR
- Pytesseract
- Pillow
- NumPy

---

## 🚀 Features

✅ Image loading
✅ Grayscale conversion
✅ Image resizing
✅ Noise reduction
✅ Thresholding
✅ OCR extraction
✅ Output image generation
✅ Text recognition

---

## 📂 Project Structure

```text
ocr-text-recognition/
│
├── main.py
├── preprocess.py
├── README.md
├── requirements.txt
├── sample_images/
└── output/
```

---

## 🔄 OCR Processing Pipeline

### Step 1 — Load Image

User selects an image for processing.

Example:

```text
sample_images/test.png
```

---

### Step 2 — Image Preprocessing

The system applies:

- Grayscale Conversion
- Resize Enhancement
- Noise Reduction
- Threshold Processing

This improves OCR accuracy.

---

### Step 3 — Text Recognition

Tesseract OCR extracts readable text.

Configuration:

```text
OEM = 3
PSM = 6
```

---

### Step 4 — Generate Output

Outputs:

- Extracted Text
- Processed Image

---

## ▶️ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Tesseract OCR and verify:

```bash
tesseract --version
```

---

## ▶️ Run Project

```bash
python main.py
```

Enter:

```text
test.png
```

---

## 📈 Example Result

### Input Image

```text
HELLO AI
THIS IS OCR TEST
```

### OCR Output

```text
Detected Text:

HELLO AI
THIS IS OCR TEST
```

---

## 📚 Concepts Learned

- Computer Vision
- Optical Character Recognition (OCR)
- Image Preprocessing
- Thresholding
- Noise Reduction
- Text Recognition
- AI Integration

---

## 🏆 Internship Project

Artificial Intelligence Internship Program

Week 4 Project: OCR Text Recognition System

Developed as part of the DecodeLabs Industrial Training Program.

---

## 👨‍💻 Author

**Zaid dahar**

Artificial Intelligence Intern
