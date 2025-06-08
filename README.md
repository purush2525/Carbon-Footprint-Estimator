Carbon Footprint Estimator


Introduction
This project is a web-based application that estimates an individual's weekly carbon footprint based on their lifestyle choices. The application uses a linear regression model to predict the carbon footprint based on user input.

Features
- User-friendly interface to input lifestyle choices
- Estimates weekly carbon footprint in kg/week
- Displays actual vs predicted carbon footprint graph
- Calculates mean squared error of the model

Requirements
- Python 3.11.5
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

Installation
To run the application, install the required libraries using pip:


bash
pip install streamlit pandas numpy scikit-learn matplotlib


Usage
1. Run the application using Streamlit:


bash

streamlit run app.py


2.  Open the application in your web browser.
3.  Select your diet type, weekly travel distance, and weekly electricity usage.
4.  The application will estimate your weekly carbon footprint and display it on the screen.
5.  You can also view the actual vs predicted carbon footprint graph by checking the "Show model performance graph" box.

Model Explanation
The application uses a linear regression model to predict the carbon footprint based on user input. The model is trained on synthetic data generated using random values for diet, transport, and electricity usage. The model takes into account the following features:

*   Diet type (vegan, vegetarian, meat-heavy)
*   Weekly travel distance (in km)
*   Weekly electricity usage (in kWh)

The model predicts the weekly carbon footprint in kg/week.

Limitations
*   The model is trained on synthetic data and may not accurately reflect real-world scenarios.
*   The application does not take into account other factors that may affect carbon footprint, such as air travel, food waste, and consumption patterns.

Future Improvements
*   Train the model on real-world data to improve accuracy.
*   Incorporate additional features that affect carbon footprint.
*   Develop a more comprehensive model that takes into account multiple factors.
