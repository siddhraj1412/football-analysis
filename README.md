# ⚽ Football Match Analysis using Computer Vision

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Project-Active-success)

## 📌 Project Overview

This project performs **automated football match analysis** using **traditional computer vision techniques**.

It processes a **~30 second football match video** and tracks:

* Players from **both teams**
* **Goalkeepers**
* **Referee**
* **Football (ball)**

Additionally, it computes and displays **ball possession percentages** for both teams based on tracking data.

⚠️ **Important:**
This project **does NOT use AI / Machine Learning / Deep Learning**.
All logic is implemented using **classical computer vision and tracking algorithms**.

---

## 🎯 Why This Project Matters (For Recruiters)

* Demonstrates **strong fundamentals in Computer Vision**
* Shows **object tracking & motion analysis**
* Real-world **sports analytics problem**
* Clean pipeline: **video → detection → tracking → analytics**
* No black-box AI — logic is **transparent and explainable**

This makes it ideal for:

* CV Internships
* Software Engineering roles
* Sports Analytics roles
* Academic & research demonstrations

---

## 🚀 Features

✔ Tracks **both team players**

✔ Detects **goalkeepers & referee**

✔ Tracks the **football continuously**

✔ Calculates **team-wise possession**

✔ Visualizes tracking directly on video

✔ Fully **offline execution** (no website, no UI)

---

## 🧠 How It Works

1. Input: A short football video (~30 seconds)
2. Frame-by-frame processing using OpenCV
3. Detection based on:

   * Color segmentation
   * Motion analysis
   * Spatial heuristics
4. Object tracking across frames
5. Ball proximity logic to estimate:

   * Which team is in control
   * Overall possession percentage
6. Output: Annotated video with live analytics

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **NumPy**
* **Classical Object Tracking Algorithms**
* **Video Processing Pipelines**

> No AI • No ML • No Deep Learning

---

## 📂 Project Structure

```
football-analysis/
│
├── data/           # Input football videos
├── outputs/        # Processed videos with tracking
├── utils/          # Helper & tracking functions
├── main.py         # Entry point
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/siddhraj1412/football-analysis.git
cd football-analysis
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add video

Place a football video inside the `data/` directory.

### 4️⃣ Run analysis

```bash
python main.py
```

### 5️⃣ Output

* Tracked & annotated video
* Possession statistics overlay
  Saved inside the `outputs/` folder.

---

## 🚫 No Web Interface

This project:

* ❌ Has no frontend
* ❌ Has no website
* ❌ Has no user input UI

It is designed as a **backend / analysis-focused system**.

---

## 📈 Future Enhancements

* Player heatmaps
* Pass detection
* Shot detection
* Set-piece recognition
* Live camera feed support
* Optional dashboard integration

---

## 👨‍💻 Author

**Siddhraj Anilkumar Thakor**
Computer Vision | Sports Analytics | Python Developer

🔗 GitHub: [https://github.com/siddhraj1412](https://github.com/siddhraj1412)

---

## ⭐ If You Like This Project

* Give it a **star**
* Fork it
* Open issues or improvements
* Use it in academic or demo projects

---
