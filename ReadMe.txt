CS685A: Data Mining Project 2021 
###########################################################################################################################################################################

This project is done by 

Anuj Shrivastava (21111013) anujs21@iitk.ac.in
Jegan Balaji BS (21111404) jeganb21@iitk.ac.in
Himanshu Lal (21111403) himanshul21@iitk.ac.in
Manish (21111306) manishv21@iitk.ac.in
Shivam Tripathi (21111408) shivamtr21@iitk.ac.in

###########################################################################################################################################################################

Libraries Required:
tensorflow: version 2.3.0
keras: version 2.4.0
opencv: version 4.0.1
numpy: version 1.20.1
pandas: version 1.2.4
matplotlib: version  3.3.4
notebook: version 1.0.0
plotly: version 2.0.9
seaborn: version 0.11.1
json: version 2.0.9
cufflinks: version 0.17.3


all code are written in ipynb and py file.

###########################################################################################################################################################################

For simplicity, Code and Datasets are structured in directories.
Code: All the codes are present in this Directory
Datasets -> cleaned-datasets: All the output file generated in the project lies here.
Datasets -> raw-datasets: All the dataset that was used during the project lies here.
Datasets -> plots: This contains GIF files and sliders graph

###########################################################################################################################################################################

To run the complete project execute the following command in bash
"bash project.sh"

###########################################################################################################################################################################


Note: When Individually running the ipynb notebooks, run them in the same order as written below.

1) GHG_Cleaning.ipynb: This file contains the code used for cleaning the GHG Emissions dataset. It combines the information of 19 datasets of ghg emission and preprocesses it for further use.

2) Population_Cleaning.ipynb: This file contains the code used for cleaning the population dataset.

3) GHG_Analytics.ipynb: This file contains the code for analytics done on GHG Dataset. This file contains the top 5 countries that produce the most and least greenhouse gas. The contribution of each gas and most prominent source of ghg emission. The relation between population and greenhouse gas emission.

4) Data_Cleaning_for_Temperature_Change.ipynb: It runs the cleaning process on temperature change data and saves necessary files to be used later.

5) Package_required_for_temperature_change_analysis.py: This is the util package for running the Analysis_of_Temperature_Change.ipynb

6) Analysis_of_Temperature_Change.ipynb: This file runs the analysis of Temperature change data

7) Glaciers_sealevel_plastics.ipynb: This file contains the code for analytics on melting glaciers, rising sea level, and plastics pollution in oceans. It shows the correlation between the melting of glaciers and the rise in sea level. It also shows the harmful effect of ocean plastics on climate.

8) natural_disaster_analytics.ipynb: This file contains the code for analytics on natural disasters and climate anomalies and their correlation with climate change. The analysis shows the increase in the number of occurrences of natural disasters because of climate change.

9) Temperature_and_Deforestation.ipynb: This file contains the code for analytics done on temperature and deforestation. It shows the temperature anomalies across the globe and how deforestation affects climate change.

10) time_series_forecasting.py: This python file contains the code to forecast any future prediction for any time-series data given to it. It uses TensorFlow and Keras libraries.


###########################################################################################################################################################################

Note: All code and plots are in ipynb python notebooks. Check the individual notebook file for descriptive plots.

The File 'Analysis_of_Temperature_Change.ipynb' runs an interactive code. Suggested to run the file individually and pass the parameters to check the plots.



###########################################################################################################################################################################