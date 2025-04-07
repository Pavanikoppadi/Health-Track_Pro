# from flask import Flask, request, jsonify
# import pickle
# import pandas as pd
# import numpy as np

# app = Flask(__name__)

# # Load the model from the pickle file
# with open('model.pkl', 'rb') as file:
#     pipeline = pickle.load(file)

# @app.route('/')
# def home():
#     return '''
#         <h1>Enter Patient Details</h1>
#         <form action="/predict" method="post">
#             <label for="Age">Age:</label>
#             <input type="text" id="Age" name="Age" value="25"><br><br>

#             <label for="Gender">Gender:</label>
#             <input type="text" id="Gender" name="Gender" value="Female"><br><br>

#             <label for="HeartRate">Heart Rate:</label>
#             <input type="text" id="HeartRate" name="HeartRate" value="75"><br><br>

#             <label for="Symptoms">Symptoms:</label>
#             <input type="text" id="Symptoms" name="Symptoms" value="headache"><br><br>

#             <label for="MedicalHistory">Medical History:</label>
#             <input type="text" id="MedicalHistory" name="MedicalHistory" value="none"><br><br>

#             <label for="Smoker">Smoker:</label>
#             <input type="text" id="Smoker" name="Smoker" value="no"><br><br>

#             <label for="Drinker">Drinker:</label>
#             <input type="text" id="Drinker" name="Drinker" value="no"><br><br>

#             <label for="Exercise">Exercise:</label>
#             <input type="text" id="Exercise" name="Exercise" value="5 days/week"><br><br>

#             <label for="SleepHours">Sleep Hours:</label>
#             <input type="text" id="SleepHours" name="SleepHours" value="7"><br><br>

#             <label for="Weight">Weight:</label>
#             <input type="text" id="Weight" name="Weight" value="70"><br><br>

#             <label for="BodyTemperature">Body Temperature:</label>
#             <input type="text" id="BodyTemperature" name="BodyTemperature" value="98.6"><br><br>

#             <label for="Lifestyle">Lifestyle:</label>
#             <input type="text" id="Lifestyle" name="Lifestyle" value="Active"><br><br>

#             <label for="SystolicPressure">Systolic Pressure:</label>
#             <input type="text" id="SystolicPressure" name="SystolicPressure" value="120"><br><br>

#             <label for="DiastolicPressure">Diastolic Pressure:</label>
#             <input type="text" id="DiastolicPressure" name="DiastolicPressure" value="80"><br><br>

#             <input type="submit" value="Submit">
#         </form>
#     '''

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Retrieve input data from the form
#         input_data = {
#             'Age': [int(request.form['Age'])],
#             'Gender': [request.form['Gender']],
#             'HeartRate': [int(request.form['HeartRate'])],
#             'Symptoms': [request.form['Symptoms']],
#             'MedicalHistory': [request.form['MedicalHistory']],
#             'Smoker': [request.form['Smoker']],
#             'Drinker': [request.form['Drinker']],
#             'Exercise': [request.form['Exercise']],
#             'SleepHours': [int(request.form['SleepHours'])],
#             'Weight': [int(request.form['Weight'])],
#             'BodyTemperature': [float(request.form['BodyTemperature'])],
#             'Lifestyle': [request.form['Lifestyle']],
#             'SystolicPressure': [int(request.form['SystolicPressure'])],
#             'DiastolicPressure': [int(request.form['DiastolicPressure'])]
#         }

#         # Create a DataFrame from the input data
#         input_df = pd.DataFrame(input_data)
        
#         # Ensure that all expected columns are present
#         expected_columns = ['Age', 'Gender', 'HeartRate', 'Symptoms', 'MedicalHistory', 'Smoker', 
#                             'Drinker', 'Exercise', 'SleepHours', 'Weight', 'BodyTemperature', 
#                             'Lifestyle', 'SystolicPressure', 'DiastolicPressure']
        
#         if not all(col in input_df.columns for col in expected_columns):
#             return jsonify({"error": "Missing input columns"})

#         # Predict using the loaded model
#         prediction = pipeline.predict(input_df)

#         # Construct the response
#         output = {
#             'Report': prediction[0][0],
#             'Suggestions': prediction[0][1],
#             'Habit': prediction[0][2],
#             'Food': prediction[0][3]
#         }

#         return jsonify(output)
    
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '_main_':
#     app.run(debug=True)




# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd
# import numpy as np

# app = Flask(__name__)

# # Load the model from the pickle file
# with open('model.pkl', 'rb') as file:
#     pipeline = pickle.load(file)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Retrieve input data from the form
#         input_data = {
#             'Age': [int(request.form['Age'])],
#             'Gender': [request.form['Gender']],
#             'HeartRate': [int(request.form['HeartRate'])],
#             'Symptoms': [request.form['Symptoms']],
#             'MedicalHistory': [request.form['MedicalHistory']],
#             'Smoker': [request.form['Smoker']],
#             'Drinker': [request.form['Drinker']],
#             'Exercise': [request.form['Exercise']],
#             'SleepHours': [int(request.form['SleepHours'])],
#             'Weight': [int(request.form['Weight'])],
#             'BodyTemperature': [float(request.form['BodyTemperature'])],
#             'Lifestyle': [request.form['Lifestyle']],
#             'SystolicPressure': [int(request.form['SystolicPressure'])],
#             'DiastolicPressure': [int(request.form['DiastolicPressure'])]
#         }

#         # Create a DataFrame from the input data
#         input_df = pd.DataFrame(input_data)
        
#         # Ensure that all expected columns are present
#         expected_columns = ['Age', 'Gender', 'HeartRate', 'Symptoms', 'MedicalHistory', 'Smoker', 
#                             'Drinker', 'Exercise', 'SleepHours', 'Weight', 'BodyTemperature', 
#                             'Lifestyle', 'SystolicPressure', 'DiastolicPressure']
        
#         if not all(col in input_df.columns for col in expected_columns):
#             return jsonify({"error": "Missing input columns"})

#         # Predict using the loaded model
#         prediction = pipeline.predict(input_df)

#         # Construct the response
#         output = {
#             'Report': prediction[0][0],
#             'Suggestions': prediction[0][1],
#             'Habit': prediction[0][2],
#             'Food': prediction[0][3]
#         }

#         return jsonify(output)
    
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd
# import numpy as np

# app = Flask(__name__, static_url_path='/static', static_folder='templates', template_folder='templates')

# # Load the model from the pickle file
# with open('model.pkl', 'rb') as file:
#     pipeline = pickle.load(file)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Retrieve input data from the form
#         input_data = {
#             'Age': [int(request.form['Age'])],
#             'Gender': [request.form['Gender']],
#             'HeartRate': [int(request.form['HeartRate'])],
#             'Symptoms': [request.form['Symptoms']],
#             'MedicalHistory': [request.form['MedicalHistory']],
#             'Smoker': [request.form['Smoker']],
#             'Drinker': [request.form['Drinker']],
#             'Exercise': [request.form['Exercise']],
#             'SleepHours': [int(request.form['SleepHours'])],
#             'Weight': [int(request.form['Weight'])],
#             'BodyTemperature': [float(request.form['BodyTemperature'])],
#             'Lifestyle': [request.form['Lifestyle']],
#             'SystolicPressure': [int(request.form['SystolicPressure'])],
#             'DiastolicPressure': [int(request.form['DiastolicPressure'])]
#         }

#         # Create a DataFrame from the input data
#         input_df = pd.DataFrame(input_data)
        
#         # Ensure that all expected columns are present
#         expected_columns = ['Age', 'Gender', 'HeartRate', 'Symptoms', 'MedicalHistory', 'Smoker', 
#                             'Drinker', 'Exercise', 'SleepHours', 'Weight', 'BodyTemperature', 
#                             'Lifestyle', 'SystolicPressure', 'DiastolicPressure']
        
#         if not all(col in input_df.columns for col in expected_columns):
#             return jsonify({"error": "Missing input columns"})

#         # Predict using the loaded model
#         prediction = pipeline.predict(input_df)

#         # Construct the response
#         output = {
#             'Report': prediction[0][0],
#             'Suggestions': prediction[0][1],
#             'Habit': prediction[0][2],
#             'Food': prediction[0][3]
#         }

#         return jsonify(output)
    
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd

# app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

# # Load the model from the pickle file
# with open('model.pkl', 'rb') as file:
#     pipeline = pickle.load(file)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Retrieve input data from the form
#         input_data = {
#             'Age': [int(request.form['Age'])],
#             'Gender': [request.form['Gender']],
#             'HeartRate': [int(request.form['HeartRate'])],
#             'Symptoms': [request.form['Symptoms']],
#             'MedicalHistory': [request.form['MedicalHistory']],
#             'Smoker': [request.form['Smoker']],
#             'Drinker': [request.form['Drinker']],
#             'Exercise': [request.form['Exercise']],
#             'SleepHours': [int(request.form['SleepHours'])],
#             'Weight': [int(request.form['Weight'])],
#             'BodyTemperature': [float(request.form['BodyTemperature'])],
#             'Lifestyle': [request.form['Lifestyle']],
#             'SystolicPressure': [int(request.form['SystolicPressure'])],
#             'DiastolicPressure': [int(request.form['DiastolicPressure'])]
#         }

#         # Create a DataFrame from the input data
#         input_df = pd.DataFrame(input_data)

#         # Ensure that all expected columns are present
#         expected_columns = ['Age', 'Gender', 'HeartRate', 'Symptoms', 'MedicalHistory', 'Smoker', 
#                             'Drinker', 'Exercise', 'SleepHours', 'Weight', 'BodyTemperature', 
#                             'Lifestyle', 'SystolicPressure', 'DiastolicPressure']
        
#         if not all(col in input_df.columns for col in expected_columns):
#             return jsonify({"error": "Missing input columns"})

#         # Predict using the loaded model
#         prediction = pipeline.predict(input_df)

#         # Construct the response
#         output = {
#             'Report': prediction[0][0],
#             'Suggestions': prediction[0][1],
#             'Habit': prediction[0][2],
#             'Food': prediction[0][3]
#         }

#         return jsonify(output)
    
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__, static_url_path='/static', static_folder='templates', template_folder='templates')

# Load the model from the pickle file
with open('model.pkl', 'rb') as file:
    pipeline = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve input data from the form
        input_data = {
            'Age': [int(request.form['Age'])],
            'Gender': [request.form['Gender']],
            'HeartRate': [int(request.form['HeartRate'])],
            'Symptoms': [request.form['Symptoms']],
            'MedicalHistory': [request.form['MedicalHistory']],
            'Smoker': [request.form['Smoker']],
            'Drinker': [request.form['Drinker']],
            'Exercise': [request.form['Exercise']],
            'SleepHours': [int(request.form['SleepHours'])],
            'Weight': [int(request.form['Weight'])],
            'BodyTemperature': [float(request.form['BodyTemperature'])],
            'Lifestyle': [request.form['Lifestyle']],
            'SystolicPressure': [int(request.form['SystolicPressure'])],
            'DiastolicPressure': [int(request.form['DiastolicPressure'])]
        }

        # Create a DataFrame from the input data
        input_df = pd.DataFrame(input_data)
        
        # Ensure that all expected columns are present
        expected_columns = ['Age', 'Gender', 'HeartRate', 'Symptoms', 'MedicalHistory', 'Smoker', 
                            'Drinker', 'Exercise', 'SleepHours', 'Weight', 'BodyTemperature', 
                            'Lifestyle', 'SystolicPressure', 'DiastolicPressure']
        
        if not all(col in input_df.columns for col in expected_columns):
            return "Missing input columns"

        # Predict using the loaded model
        prediction = pipeline.predict(input_df)

        # Construct the response
        report = prediction[0][0]
        suggestions = prediction[0][1]
        habit = prediction[0][2]
        food = prediction[0][3]

        # Render the result template and pass the output data
        return render_template('result.html', report=report, suggestions=suggestions, habit=habit, food=food)

    except Exception as e:
        return str(e)

if __name__ == '_main_':
    app.run(debug=True)