from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'area': [float(request.form['area'])],
            'bedrooms': [int(request.form['bedrooms'])],
            'bathrooms': [int(request.form['bathrooms'])],
            'stories': [int(request.form['stories'])],
            'mainroad': [request.form['mainroad']],
            'guestroom': [request.form['guestroom']],
            'basement': [request.form['basement']],
            'hotwaterheating': [request.form['hotwaterheating']],
            'airconditioning': [request.form['airconditioning']],
            'parking': [int(request.form['parking'])],
            'prefarea': [request.form['prefarea']],
            'furnishingstatus': [request.form['furnishingstatus']]
        }
        df = pd.DataFrame(data)
        prediction = model.predict(df)[0]
        predicted_price = round(float(prediction), 2)
        return render_template('result.html', prediction=f"Predicted Price: ₹{predicted_price}")
    except Exception as e:
        return render_template('result.html', prediction=f"Error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
