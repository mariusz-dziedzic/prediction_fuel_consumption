Before starting:
- The program is available in a version to run in Jupyter Notebook and in a standard Python file.
- Make sure you have all packages necessary for booting installed. They should be installed by default in Jupiter, but when running a script from a Python file, you may get an error related to importing the library. In this case, execute the following commands in CMD:
pip install scikit-learn
pip install pandas

Description:
- The program uses the machine learning technique to create a model that will be able to predict how much fuel a given car will use with the given parameters. Based on the available data (csv file), the model divides the data into 2 samples: the learning sample (80%) and the test sample (20%). The learned model then makes predictions on the data.
- At the end, the user can enter the data of the new vehicle (according to the predefined scheme), and then he will receive information about the predicted fuel consumption. Then the user can add the car data to the csv file automatically. Then the user can enter another car and add the data to the database.
- The next time the script is run, the model is re-evaluated with new cars data, which should improve the accuracy of the predictions made by the model.

##########################################################
Head table description:

Column		|		Description			|	Feature Type	|
------		|		----------			|	------------	|
l/100km 	| 	The amount of fuel consumed per 100 km	| 	Target		|
Cylinders	| 	Number of engine cylinders		| 	Numerical	|
Horsepower 	| 	The power of the car			| 	Numerical	|
Weight		| 	Weight in kg				| 	Numerical	|
Acceleration 	| 	Acceleration in seconds 		| 	Numerical	|