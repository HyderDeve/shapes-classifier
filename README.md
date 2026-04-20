# Shapes Classifier

A neural network-based image classifier that identifies five geometric shapes from grayscale 28×28 images. Built with TensorFlow/Keras, this project demonstrates a complete machine learning pipeline — from dataset loading and preprocessing to model training, evaluation, and saving.

**Student ID:** 2307BSCS009

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Repository Structure](#repository-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Running the Notebook](#running-the-notebook)

---

## Project Overview

This project trains a fully connected neural network to classify images of five geometric shapes:

- Circle
- Triangle
- Square
- Diamond
- Pentagon

Images are loaded from a custom dataset, converted to grayscale, normalised, and then fed into a Sequential Keras model. The trained model is saved in the `.keras` format for later use.

---

## Dataset

The dataset is located in the `2307_BSCS009_Shapes_Dataset/` directory.

| Property        | Value                                 |
|-----------------|---------------------------------------|
| Total images    | 375                                   |
| Classes         | 5 (Circle, Triangle, Square, Diamond, Pentagon) |
| Images per class | 75                                   |
| Image size      | 28 × 28 pixels (grayscale)            |
| Format          | PNG                                   |

Each class has its own sub-folder, and the file `shapes_2307BSCS009_labels.csv` maps every image filename to its numeric label and class name.

**Label mapping:**

| Label | Class    |
|-------|----------|
| 0     | circle   |
| 1     | triangle |
| 2     | square   |
| 3     | diamond  |
| 4     | pentagon |

**Train / Test split:** 80 % training (300 images) / 20 % test (75 images), stratified by class.

---

## Model Architecture

A simple Sequential neural network built with Keras:

| Layer   | Output Shape | Parameters |
|---------|--------------|------------|
| Flatten | (None, 784)  | 0          |
| Dense (ReLU) | (None, 128) | 100,480 |
| Dense (Softmax) | (None, 5) | 645     |

- **Optimiser:** Adam  
- **Loss function:** Sparse Categorical Crossentropy  
- **Metric:** Accuracy  
- **Epochs:** 15  

---

## Results

| Metric        | Value   |
|---------------|---------|
| Test Accuracy | 100.00% |
| Test Loss     | 2.45%   |

The trained model is saved as `shapes_classifier_2307-BSCS009.keras`.

---

## Repository Structure


```
shapes-classifier/
├── 2307_BSCS009_Shapes_Dataset/
│   ├── Circle/                        # 75 circle images
│   ├── Diamond/                       # 75 diamond images
│   ├── Pentagon/                      # 75 pentagon images
│   ├── Square/                        # 75 square images
│   ├── Triangle/                      # 75 triangle images
│   └── shapes_2307BSCS009_labels.csv  # Image labels
├── Image Processing Script For Building Dataset.py  # Script for extracting shapes from images
├── image_organisation.py              # Script for renaming/organising images
├── whole_code.ipynb                   # Jupyter notebook (full pipeline)
├── shapes_classifier_2307-BSCS009.keras  # Saved trained model
├── requirements.txt                   # Python dependencies
├── env/                               # Python virtual environment (not needed for deployment)
├── sample/
│   └── Pentagons.jpg                  # Example image for dataset building
└── README.md
```

---

## Setup

### Prerequisites

- **Python 3.10 or later** — [Download Python](https://www.python.org/downloads/)
- **pip** — comes bundled with Python

### Create a Virtual Environment

Open a terminal in the project root directory and run:

**macOS / Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv env
env\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv env
env\Scripts\Activate.ps1
```

You should see `(env)` appear at the start of your terminal prompt, confirming the environment is active.

### Install Dependencies

With the virtual environment active, install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs TensorFlow, Keras, scikit-learn, NumPy, Pandas, Pillow, Matplotlib, Jupyter, and all other required libraries.

To deactivate the virtual environment when you are done:

```bash
deactivate
```

---

## Running the Notebook

Start Jupyter and open the notebook:

```bash
jupyter notebook whole_code.ipynb
```

Run all cells in order to:

1. Load and explore the dataset
2. Preprocess the images
3. Split the data into training and test sets
4. Build and train the neural network
5. Evaluate the model on the test set
6. Save the trained model to disk