import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# 1. Generate simple data
X = np.array([[i] for i in range(1, 101)])  # Numbers 1 to 100
y = np.array([i % 2 for i in range(1, 101)])  # 0 if even, 1 if odd

# 2. Train a model
model = DecisionTreeClassifier()
model.fit(X, y)

# 3. Streamlit app
st.title("Arunaachalam")
st.title("Even or Odd Number Classifier")

number = st.number_input("Enter a number", min_value=0, step=1)

if st.button("Check"):
    prediction = model.predict([[number]])[0]
    if prediction == 0:
        st.success(f"{number} is Even ✅")
    else:
        st.warning(f"{number} is Odd 🔢")
