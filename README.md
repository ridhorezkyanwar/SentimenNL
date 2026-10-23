# SentimenNLP

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=2600&pause=850&color=58A6FF&center=true&vCenter=true&width=520&lines=Build+%E2%80%A2+Test+%E2%80%A2+Improve" alt="Animated banner: Build, Test, Improve" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python badge" />
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas badge" />
  <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn badge" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow badge" />
</p>


## Description

SentimenNLP is a sentiment analysis project for Shopee reviews in Indonesian. It demonstrates an end-to-end NLP workflow: loading and cleaning review data, normalizing slang, extracting TF-IDF features, training classification models, and evaluating performance.

## Project Overview

This repository includes:

- `dataset_shopee.csv`: Shopee review dataset
- `pelatihan_dan_inferensi.ipynb`: notebook for training, evaluation, and inference
- `scraping.py`: optional script for collecting additional review data
- `requirements.txt`: Python dependencies
- `model_sentimen_terbaik.pkl`: serialized Logistic Regression model and fitted TF-IDF vectorizer produced by the notebook

## Key Features

- Indonesian text preprocessing and normalization
- Handling of Shopee-specific slang and basic stopwords
- Stratified train/test split
- TF-IDF feature extraction with n-grams
- Binary sentiment classification: negative (ratings 1-2) and positive (ratings 4-5); neutral (rating 3) is excluded
- Training multiple models: Logistic Regression, Random Forest, Deep Neural Network
- Evaluation with accuracy, precision, recall, F1-score, and confusion matrix
- Real-time inference examples using saved model

## Technology Stack

- Python 3
- pandas
- numpy
- scikit-learn
- tensorflow
- matplotlib
- seaborn
- google-play-scraper

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Start the notebook:

   ```powershell
   jupyter notebook pelatihan_dan_inferensi.ipynb
   ```

## Usage

- Open `pelatihan_dan_inferensi.ipynb` and run the cells in order.
- The notebook loads the dataset, cleans the text, trains models, evaluates performance, and runs example predictions.
- To use the saved model manually, load `model_sentimen_terbaik.pkl` with Python and apply the saved TF-IDF vectorizer.

## Results

The notebook reports:

- The previous recorded Logistic Regression run reported 88.22% test accuracy and macro F1 of about 0.85 on its 80/20 split.
- Re-run the notebook after the binary-label cleanup to regenerate current outputs and verify the metrics before citing them.
- Example predictions:
  - "Aplikasi Shopee jelek sekali, loadingnya lemot dan sering keluar sendiri!" → Negative
  - "Sangat puas belanja di sini, barang cepat sampai dan banyak diskon gratis ongkir!" → Positive

## GitHub Repository Description

`Sentiment analysis for Shopee reviews in Indonesian using NLP and machine learning.`

## How to Publish on GitHub

1. Create a new repository on GitHub named `sentimen-nlp` or `SentimenNL`.
2. Add a short repository description, for example:
   - `Sentiment analysis for Shopee reviews in Indonesian using NLP and machine learning.`
3. From the project folder, initialize Git if needed:

   ```powershell
   git init
   git add .
   git commit -m "Initial commit: add SentimenNLP project"
   git branch -M main
   git remote add origin https://github.com/<username>/sentimen-nlp.git
   git push -u origin main
   ```

4. Confirm that the files appear in the GitHub repository and that the README renders correctly.


## Contact

- Name: [Ridho Rezky Anwar]
- Email: [ridhorezky.dev@gmail.com]
- LinkedIn: [https://linkedin.com/in/ridho-rezky-anwar-98bb3a370]
