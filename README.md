# Sentiment Analyzer for Product Reviews

A simple Python-based tool that analyzes the sentiment of product reviews and classifies them as **Positive**, **Negative**, or **Neutral**.

Built as a BYOP (Bring Your Own Project) submission for the **Fundamentals of AI & ML** course on the VITyarthi platform.

---

## What Does It Do?

Every day, thousands of products are reviewed online on platforms like Amazon and Flipkart. Reading every review manually is time-consuming. This tool solves that problem — you paste a review, and it instantly tells you whether the customer was happy, unhappy, or neutral.

---

## Features

- Analyze any product review in plain English
- Detects **Positive**, **Negative**, and **Neutral** sentiments
- Handles negation (e.g., "not good" is correctly treated as negative)
- View **history** of all reviews analyzed in the current session
- View a **summary** of how many positive, negative, and neutral reviews were entered
- Simple menu-driven interface — no GUI required

---

## Requirements

- Python 3.x (any version of Python 3 works)
- No external libraries needed — uses only built-in Python

---

## How to Run

**Step 1:** Make sure Python is installed on your system.

You can check by running:
```
python --version
```

**Step 2:** Download or clone this repository.

```
git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer
```

**Step 3:** Run the program.

```
python sentiment_analyzer.py
```

---

## How to Use

Once the program starts, you will see a menu:

```
MENU:
1. Analyze a Review
2. View History
3. View Summary
4. Exit
```

- Choose **1** and type any product review to analyze it.
- Choose **2** to see all reviews you analyzed in this session.
- Choose **3** to see a count of positive, negative, and neutral reviews.
- Choose **4** to exit the program.

---

## Example

**Input:**
```
Enter the product review: This product is amazing and works perfectly. Highly recommended!
```

**Output:**
```
==================================================
REVIEW   : This product is amazing and works perfectly. Highly recommended!
SENTIMENT: POSITIVE
Score    : +3 Positive  |  -0 Negative
==================================================
```

---

## How It Works

The program uses a **keyword-based approach**:

1. The review is converted to lowercase and cleaned.
2. Each word is checked against a list of **positive words** and **negative words**.
3. If a negation word (like "not", "never") appears before a positive/negative word, the score is flipped.
4. The final sentiment is decided based on which score is higher.

This approach keeps the logic simple and understandable without needing any machine learning libraries.

---

## Project Structure

```
sentiment-analyzer/
│
├── sentiment_analyzer.py   # Main program file
└── README.md               # This file
```

---

## Author

**Dhairya**
B.Tech — Artificial Intelligence & Machine Learning
VIT Bhopal University
VITyarthi — Fundamentals of AI & ML (CO5 BYOP)
