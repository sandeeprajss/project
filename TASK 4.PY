# Step 1: Import Required Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Load the Dataset
# Download the dataset from https://www.kaggle.com/uciml/sms-spam-collection-dataset
df = pd.read_csv('spam.csv', encoding='latin-1')

# Step 3: Preprocess the Data
df = df[['v1', 'v2']]  # Keep only necessary columns
df.columns = ['label', 'message']  # Rename columns
df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Convert labels to binary

# Step 4: Split the Data into Training and Testing Sets
X = df['message']  # Features (email messages)
y = df['label']  # Labels (spam or ham)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature Extraction
vectorizer = CountVectorizer()  # Convert text to numerical features
X_train_vec = vectorizer.fit_transform(X_train)  # Fit and transform training data
X_test_vec = vectorizer.transform(X_test)  # Transform testing data

# Step 6: Train the Model
model = MultinomialNB()  # Initialize Naive Bayes model
model.fit(X_train_vec, y_train)  # Train the model

# Step 7: Make Predictions
y_pred = model.predict(X_test_vec)  # Predict on the test set

# Step 8: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)  # Calculate accuracy
print(f"Accuracy: {accuracy:.4f}\n")  # Print accuracy
print("Classification Report:")
print(classification_report(y_test, y_pred))  # Print classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))  # Print confusion matrix