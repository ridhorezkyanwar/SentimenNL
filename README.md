# SentimenNLP — Analisis Sentimen Ulasan Shopee

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow" />
</p>

This project demonstrates an NLP workflow for classifying Indonesian-language Shopee reviews as positive or negative. It includes preprocessing, slang normalization, TF-IDF feature extraction, model training, and evaluation in a Jupyter notebook.

## Dataset and label policy

- Reviews with ratings 1–2 are treated as **negative**.
- Reviews with ratings 4–5 are treated as **positive**.
- Rating 3 reviews are excluded from the binary classification task.

## Repository contents

- `dataset_shopee.csv` — the committed review dataset (contact-like strings are redacted before committing).
- `privacy.py` and `tests/test_privacy.py` — standard-library personal-data redaction and regression checks.
- `pelatihan_dan_inferensi.ipynb` — notebook for preprocessing, training, evaluation, and example inference.
- `scraping.py` — optional script that attempts to collect Indonesian Shopee reviews through Google Play review data.
- `requirements.txt` — Python dependencies.

The current repository root does not contain the serialized `model_sentimen_terbaik.pkl` file mentioned in an earlier version of this README. Run the notebook to recreate models and results rather than assuming a trained artifact is already available.

## Setup

Use Python and pip. A virtual environment is recommended.

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Install Jupyter if it is not available in the environment, then open the notebook:

```bash
python -m pip install jupyter
jupyter notebook pelatihan_dan_inferensi.ipynb
```

Run the notebook cells in order. It loads the dataset, preprocesses text, fits the selected models, evaluates predictions, and demonstrates inference.

## Results and reproducibility

An earlier README revision recorded 88.22% test accuracy and macro-F1 of about 0.85 for Logistic Regression on an 80/20 split. The same note says the labels were subsequently cleaned up; therefore, those figures should be treated as historical, not as verified current performance. Re-run the notebook and refresh the reported metrics before using them as a benchmark.

## Limitations

- Classification is binary; neutral reviews are excluded by the label policy above.
- Model performance depends on the dataset split, preprocessing, and label quality.
- The scraping script depends on an external review source and may be limited or break as that source changes.
- The scraper redacts email-like strings and likely Indonesian phone numbers from review text; the committed dataset is checked by CI for those patterns.
- This notebook is a learning and experimentation project, not a production review-moderation service.

## Contact

- Email: [ridhorezky.dev@gmail.com](mailto:ridhorezky.dev@gmail.com)
- LinkedIn: [Ridho Rezky Anwar](https://linkedin.com/in/ridho-rezky-anwar-98bb3a370)
