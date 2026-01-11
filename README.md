# 🛒 BigMart - E-commerce Web Application

BigMart is a robust, full-stack e-commerce platform built with **Django**. It bridges the gap between traditional retail and modern AI by featuring an **Auto Review Rating System** that uses Deep Learning to analyze customer feedback.

---

## 🚀 Features

### 🧑‍💻 User Experience
* **Authentication:** Secure Sign-up, Login, and Logout functionality.
* **Product Browsing:** Detailed product pages with high-quality images and descriptions.
* **Shopping Cart:** Real-time quantity updates and seamless item removal.
* **Checkout:** Streamlined order summary and checkout process.

### 🤖 AI-Powered Insights
* **Auto Review Rating System:** * Automatically predicts and assigns product ratings based on user review text.
    * Utilizes a **Deep Learning (NLP)** model to perform sentiment analysis.
    * Ensures consistent, unbiased ratings even if a user forgets to select a star count.

### 🛠️ Administration
* **Store Management:** A dedicated admin panel to Add, Update, and Delete products and manage inventory.
* **Image Handling:** Automated product image uploads and storage.

---

## 🏗️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript, **Bootstrap 5** |
| **Backend** | Python, **Django** |
| **Database** | SQLite |
| **AI / ML** | **TensorFlow**, Natural Language Processing (NLP) |
| **Tools** | Git, GitHub |

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```
   git clone [(https://github.com/1Jayakrishnan/Bigmart-with-auto-review.git)]
   cd bigmart
   ```
2. **Create a Virtual Environment**
   ```bash
  python -m venv venv

3. **Install Dependencies**
   ```bash
  pip install -r requirements.txt

4. **Run Migrations**
   ```bash
  python manage.py migrate
  
5. **Start the Server**
   ```bash
  python manage.py runserver
  
  ```

