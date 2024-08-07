# ENTSO-E Data Analysis and Machine Learning (Time series forecasting and clustering on ENTSO-E)

This project focuses on the analysis and clustering of time series data from the European Network of Transmission System Operators for Electricity (ENTSO-E). The data, collected using the ENTSO-E API, was subjected to a comprehensive analysis and machine learning process, employing various statistical and data visualization techniques to extract meaningful insights.

The dataset was retrieved through a Python script leveraging the ENTSO-E API, ensuring a systematic and automated data collection process. Initial data analysis included handling missing values, renaming columns for clarity, and fixing data types to ensure consistency and accuracy.

The dataset comprises time series data sampled every 15 minutes over one year. Key statistical measures such as mean, median, variance, minimum, and maximum values were calculated for all variables. Weekly-based time series data (52 weeks) were visualized to observe trends and patterns over time.

Descriptive statistics including mean, median, quantile, and percentile were computed for all variables to provide a comprehensive understanding of the data distribution. These statistics were visualized to facilitate an intuitive grasp of the dataset's characteristics.

Given the high dimensionality of the dataset, Principal Component Analysis (PCA) was employed to reduce the dimensionality while retaining approximately 95% of the variance. This reduction facilitated more efficient processing and analysis.

Subsequently, K-means clustering was applied to the PCA-transformed data to identify inherent patterns and groupings within the dataset. The optimal number of clusters was determined using the Elbow Method and silhouette scores, ensuring robust and meaningful clustering results.


The PCA and K-means clustering results were used to reconstruct the original time series data. This involved mapping the reduced dimensions back to the original feature space, ensuring that the reconstructed data closely resembled the initial dataset. The reconstructed data was then saved to a new CSV file for further analysis.


The newly reconstructed dataset underwent additional rounds of analysis to verify the integrity and accuracy of the clustering and reconstruction process. Missing values were addressed, data types were corrected, and comprehensive visualizations of weekly time series data were produced.


The project culminated in applying PCA for dimension reduction and K-means clustering to the reconstructed dataset, reaffirming the robustness of the clustering model and providing a detailed understanding of the underlying patterns in the ENTSO-E time series data.






## The research question of the project

#### Data Collection and Preprocessing

- How can the ENTSO-E API be effectively utilized to collect comprehensive time series data on electricity consumption and transmission across Europe?
- What are the best practices for handling missing values, renaming columns, and fixing data types in the ENTSO-E dataset?

#### Time Series Analysis

- What are the key statistical characteristics (mean, median, variance, minimum, maximum) of the electricity consumption and transmission data over a one-year period?
- How do these statistical measures vary on a weekly basis throughout the year?

#### Descriptive Statistical Analysis

- What are the distributions of mean, median, quantiles, and percentiles for all variables in the dataset?
- How can visualizations of these distributions help in understanding the underlying patterns in electricity consumption and transmission?

#### Dimensionality Reduction

- How effective is Principal Component Analysis (PCA) in reducing the dimensionality of high-dimensional time series data while retaining a significant amount of variance?
- What is the optimal number of principal components needed to retain around 95% of the variance in the dataset?

#### Clustering Analysis

- How can K-means clustering be applied to the PCA-transformed data to identify distinct patterns or groups in the electricity consumption and transmission data?
- What is the optimal number of clusters as determined by the Elbow Method and silhouette scores?
- How do the identified clusters differ in terms of their statistical and temporal characteristics?


#### Reconstruction and Validation

- How can the original time series data be reconstructed from the PCA and K-means clustering results to ensure it closely resembles the initial dataset?
- What methods can be used to validate the accuracy and integrity of the reconstructed time series data?


#### Further Analysis on Reconstructed Data

- How does the analysis of the reconstructed dataset compare to the original dataset in terms of statistical measures and visual patterns?
- What additional insights can be gained from reapplying PCA and K-means clustering to the reconstructed dataset?



## Requirements
- **Programming Language:** Python 3.9.13
- **Computing platform:** Jupyter Notebook
- **Library:** Numpy, Pandas, OS, Matplotlib, Seaborn, Scikit-learn, Plotly
- **Tools:** Git Bash



## Dataset 
The data, collected using the ENTSO-E API, was subjected to a comprehensive analysis and machine learning process, employing various statistical and data visualization techniques to extract meaningful insights. The dataset was retrieved through a Python script leveraging the ENTSO-E API, ensuring a systematic and automated data collection process. Initial data analysis included handling missing values, renaming columns for clarity, and fixing data types to ensure consistency and accuracy.

**Data collection URL :** [ENTSO-E](https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime=12.03.2024+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=12.03.2024+00:00|CET|DAYTIMERANGE&area.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A82H&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2))




## How to Run the Analysis 
First, make sure that Python 3.9.13 is installed in the Jupyter Notebook along with the other required libraries mentioned in the requirements.

- Clone the git repository or download the ZIP file.
- Navigate to the project directory.
- To execute the program, run the Script in Jupyter Notebook for data analysis, visualization, time series implementation, clustering, saving new CSV from the cluster, etc.
- Then, step by step, execute the cell of the Jupyter Notebook and view the analysis results. 
- Execute the program and run the Script_1 in Jupyter Notebook for new CSV data analysis, visualization, time series implementation, and clustering. This CSV will be saved from the previous script in a new directory and come from clustering and data reconstruction.
- Then, step by step, execute the cell of the Jupyter Notebook and view the analysis results. 



## Installation

To run this project, you need to have the following software installed:
- Python 3.6 or later
- Jupyter Notebook

You can install the required Python packages using `pip`:

```bash
pip install numpy pandas matplotlib seaborn plotly os scikit-learn
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation 
[CITATION](https://github.com/jishan900/Time-series-forecasting-and-clustering-on-ENTSO-E/blob/master/CITATION.cff)



## Contact Information

For questions or issues, please contact:

- Md Asifuzzaman Jishan - [jishan900@gmail.com](mailto:jishan900@gmail.com)
- GitHub: [jishan900](https://github.com/jishan900)

## Acknowledgements

- [ENTSO-E](https://www.entsoe.eu/) for providing the data.
