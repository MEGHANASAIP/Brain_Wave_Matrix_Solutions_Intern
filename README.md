# Brain_Wave_Matrix_Solutions_Intern
# Task 1 - Create a sale data analysis of any commercial store.
## Supermarket Sales Data Analysis | Data Analytics

---

### 📋 Project Overview  
This project delivers an **end-to-end exploratory data analysis (EDA)** and **data preprocessing workflow** on a commercial supermarket sales dataset, performed using **Python** in **Google Colab**. The goal is to extract actionable business insights by analyzing sales patterns, customer behavior, and product performance.

---

### 🎯 Objective  
To perform a comprehensive sales analysis of a supermarket business by applying:

- **Data Cleaning & Preprocessing**  
- **Feature Engineering (time-based features)**  
- **Descriptive Statistics & Correlations**  
- **Visual Exploratory Data Analysis**

---

### 🗂 Dataset Details  
- **Name:** Supermarket Sales Dataset  
- **Format:** CSV (Public Dataset)  
- **Key Features:**  
  - Invoice ID, Branch, City  
  - Customer Type, Gender  
  - Product Line, Total, Payment Method  
  - Date & Time of Sale, Tax, Gross Income, COGS

---

### 🛠 Tools & Libraries  
- **Python**  
- **Google Colab** (Jupyter Notebook environment)  
- **Pandas & NumPy** (Data processing)  
- **Seaborn & Matplotlib** (Visualizations)  
- **WordCloud** (Product popularity)

---

### 🔍 Analysis Breakdown  

1. **Data Preprocessing**  
   - Converted Date and Time columns to datetime objects  
   - Engineered new time features: day, month, year, and hour  
   - Handled missing and inconsistent data  

2. **Descriptive Analysis**  
   - Correlation matrix to understand relationships among Tax, Total, Gross Income, and COGS  
   - Calculated and visualized average customer ratings  

3. **Custom Visualization Functions**  
   - Reusable functions created for:  
     - Countplots  
     - Boxplots  
     - Lineplots  
     - Relational plots  

---

### 📊 Business Insights Explored  

- Which city or branch generates the highest revenue?  
- What time of day drives peak sales?  
- Customer preferences by product line and branch  
- Impact of customer type on sales and ratings  
- Popular payment methods  
- Most loved product categories visualized with WordCloud  

---

### 📈 Visual Insights  

- Hourly and monthly sales trends by branch  
- Distribution of product lines across branches  
- Customer payment method preferences  
- Product popularity showcased through WordCloud visualization  

---

### 💡 Conclusion  
This project reflects a complete commercial sales data analysis workflow, showcasing:

- Raw data preprocessing and cleansing  
- Feature engineering for temporal insights  
- Identification of key business patterns  
- Effective visual storytelling with Python

---

## 🧠 Task 2 - Social Media Sentiment Analysis | NLP & Text Classification

### 📋 Project Overview  
This project presents a complete workflow for sentiment classification on social media text data using **Natural Language Processing (NLP)**. Implemented in **Google Colab with Python**, the project aims to classify user comments into **Positive**, **Neutral**, or **Negative** sentiments. The pipeline covers data preprocessing, feature extraction, model training, and evaluation.

### 🎯 Objective  
To perform sentiment classification on textual data by applying:

- Text Cleaning & Preprocessing  
- Class Balancing  
- TF-IDF Vectorization  
- Model Training & Evaluation  
- Multi-class Performance Analysis  

### 🗂 Dataset Details  
- **Name**: Social Media Sentiment Dataset  
- **Format**: CSV (Provided for internship)  
- **Key Features**:  
  - `clean_comment`: Cleaned text data  
  - `category`: Sentiment label  
    - `1` – Positive  
    - `0` – Neutral  
    - `-1` – Negative  

### 🛠 Tools & Libraries  
- Python  
- Google Colab  
- `pandas`, `numpy` – Data processing  
- `scikit-learn` – TF-IDF, Logistic Regression, evaluation metrics  

### 🔍 Workflow Summary  

#### Data Preprocessing
- Removed null values  
- Balanced sentiment classes using stratified sampling  
- Split data into training and testing sets  

#### Feature Extraction
- Applied **TF-IDF Vectorization** to convert text into numeric features  

#### Model Training & Evaluation
- Trained a **Logistic Regression** classifier  
- Evaluated model performance using precision, recall, F1-score, and accuracy  

### 📊 Sentiment Insights Explored  
- Class distribution and balance  
- Model performance per sentiment category  
- Evaluation metrics to assess classifier effectiveness  

### 📈 Performance
- Achieved **83% accuracy** on the test data  

### 💡 Conclusion  
This project demonstrates a complete end-to-end NLP pipeline for sentiment analysis, including:

- Clean and balanced textual data  
- Effective vectorization techniques  
- Multi-class model evaluation  
- Real-world application of NLP techniques  
