# 🧠 Fashion MNIST Classification – Artificial Neural Network (ANN)

This project demonstrates building, training, and deploying an **Artificial Neural Network (ANN)** to classify images from the **Fashion MNIST dataset** into **10 categories of clothing items** (e.g., T-shirt, trousers, sneakers, etc.).

---

## 🚀 Features

* **Dataset:** [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) (loaded via `tensorflow.keras.datasets.fashion_mnist`)
* **Model:** Fully connected ANN built with **TensorFlow/Keras**
* **Preprocessing:** Normalization and reshaping of data for ANN input
* **Training:** **Categorical Crossentropy** loss, **SGD** optimizer
* **Deployment:** FastAPI for real-time inference
* **Environment:** Python, TensorFlow/Keras, FastAPI

---

## 🛠️ Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/AyaMYousef/Fashion_MNIST_deployed_Project_ANN.git
cd Fashion_MNIST_deployed_Project_ANN
```

2️⃣ **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset

The **Fashion MNIST** dataset consists of **28x28 grayscale images** of clothing items, categorized into 10 classes:

* 0 → T-shirt/top
* 1 → Trouser
* 2 → Pullover
* 3 → Dress
* 4 → Coat
* 5 → Sandal
* 6 → Shirt
* 7 → Sneaker
* 8 → Bag
* 9 → Ankle boot

Dataset is automatically loaded via:

```python
from tensorflow.keras.datasets import fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
```

---

## 🤖 Model Architecture

* **Input Layer:** 784 neurons (flattened 28x28 image)
* **Hidden Layers:** Dense layers with ReLU activation
* **Output Layer:** 10 neurons with Softmax activation

Example architecture:

```
Input(784) → Dense(128, ReLU) → Dense(64, ReLU) → Dense(32, ReLU) → Dense(10, Softmax)
```

---

## 📈 Training

* **Optimizer:** SGD
* **Loss:** Categorical Crossentropy
* **Metrics:** Accuracy
* **Epochs:** 20 (adjustable)

The trained model is saved as:

```
model.keras
```
---

## 🌐 Deployment

Run the FastAPI application locally:

```bash
python main.py
```

Then open your browser and go to:

```
http://127.0.0.1:8000/
```

Upload an image of clothing to get the predicted category.

---


