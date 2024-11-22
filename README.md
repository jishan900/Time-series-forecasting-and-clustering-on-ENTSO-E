# ENTSO-E Data Analysis and Machine Learning (Time series forecasting and clustering on ENTSO-E)

This project focuses on analyzing and clustering time series data from the European Network of Transmission System Operators for Electricity (ENTSO-E). It incorporates advanced machine learning methods, including **K-Means**, **K-Medoids**, and **Hierarchical Clustering**, to extract meaningful patterns. These methods are further enhanced by **Principal Component Analysis (PCA)** for dimensionality reduction.

This project focuses on the analysis and clustering of time series data from the European Network of Transmission System Operators for Electricity (ENTSO-E). The data, collected using the ENTSO-E API, underwent a comprehensive analysis and machine learning process, incorporating advanced statistical, dimensionality reduction, and clustering techniques to extract meaningful insights.

The dataset was retrieved through a Python script leveraging the ENTSO-E API, ensuring a systematic and automated data collection process. Initial data preprocessing included handling missing values, renaming columns for clarity, and ensuring consistent data types for accuracy and reliability.

The dataset comprises time series data sampled every 15 minutes over one year. Initial analysis included key statistical measures such as mean, median, variance, minimum, and maximum values, calculated for all variables. Weekly-based time series data (52 weeks) were visualized to identify temporal trends and patterns.

Descriptive statistics, including mean, median, quantile, and percentile, were computed and visualized for a comprehensive understanding of the data distribution. This facilitated identifying outliers and understanding the variability within the dataset.

### Dimensionality Reduction
Given the high dimensionality of the dataset, **Principal Component Analysis (PCA)** was employed to reduce the dimensionality while retaining approximately 95% of the variance. This enabled efficient processing and visualization of the dataset.

### Clustering Approaches
Multiple clustering techniques were applied to the PCA-transformed data to uncover inherent patterns:
1. **K-means Clustering**: 
   - The optimal number of clusters was determined using the **Elbow Method** and **Silhouette Scores**.
   - Clustering results were visualized, and the clusters were interpreted in relation to the dataset's original features.

2. **K-Medoids Clustering**:
   - An alternative to K-means, focusing on minimizing dissimilarities within clusters.
   - Performance and silhouette scores were compared with K-means to evaluate clustering stability.

3. **Hierarchical Clustering**:
   - This approach involved clustering based on a dendrogram to explore data hierarchies.
   - The silhouette scores for various cluster numbers were evaluated to select the optimal number of clusters.


### Reconstructed Dataset
The PCA-transformed and clustered data were reconstructed back into the original feature space to validate clustering accuracy and interpretability. The reconstructed data was saved to a new CSV file for downstream analysis. Comparative analyses, including clustering graph visualizations and original time series trends, provided additional insights into the clustering's effectiveness.

### Comprehensive Comparisons
The project included detailed comparisons of clustering methods:
- **Silhouette Score Analysis**: Evaluated clustering performance across PCA components and methods.

This iterative process of dimension reduction, clustering, and reconstruction ensured robust insights into the ENTSO-E time series data and the identification of meaningful clusters.







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
- How does K-medoids clustering compare to K-means in identifying clusters, especially in terms of silhouette scores and robustness?
- How can hierarchical clustering (using Ward linkage) be applied to the PCA-transformed data to explore hierarchical relationships between clusters?
- What is the optimal number of clusters for hierarchical clustering based on silhouette scores, and how do these clusters compare to those found by K-means and K-medoids?


#### Reconstruction and Validation

- How can the original time series data be reconstructed from the results of PCA and clustering methods (e.g., K-means, K-medoids, hierarchical) to ensure it closely resembles the initial dataset?
- What metrics and methods can be used to validate the accuracy, integrity, and representativeness of the reconstructed time series data?


#### Further Analysis on Reconstructed Data

- How does the analysis of the reconstructed dataset compare to the original dataset in terms of statistical measures, temporal trends, and visual patterns?
- What additional insights can be gained from reapplying PCA and clustering methods (K-means, K-medoids, hierarchical) to the reconstructed dataset?
- How do the clusters identified in the reconstructed dataset corroborate or refine the findings from the original clustering analysis?


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
- Change the dataset path and all folders path. 
- To execute the program, run the Script in Jupyter Notebook for data analysis, visualization, time series implementation, clustering, saving new CSV from the cluster, etc.
- Then, step by step, execute the cell of the Jupyter Notebook and view the analysis results. 
- Execute the program and run the Script_1 in Jupyter Notebook for new CSV data analysis, visualization, time series implementation, and clustering. This CSV will be saved from the previous script in a new directory and come from clustering and data reconstruction.
- Follow the step 6 for the Script_2.
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

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jishan900/Time-series-forecasting-and-clustering-on-ENTSO-E/blob/master/LICENSE.txt) file for details.

## Citation 
For citation of this project - see the [CITATION](https://github.com/jishan900/Time-series-forecasting-and-clustering-on-ENTSO-E/blob/master/CITATION.cff) file for details.






## Contact Information

For questions or issues, please contact:

- Md Asifuzzaman Jishan - [jishan900@gmail.com](mailto:jishan900@gmail.com)
- GitHub: [jishan900](https://github.com/jishan900)

## Acknowledgements

We would like to express our gratitude to [ENTSO-E](https://www.entsoe.eu/) (European Network of Transmission System Operators for Electricity) for their invaluable support in providing the data that was crucial for the completion of this project. Their comprehensive data sets and timely assistance were instrumental in enabling the analysis and insights presented in this work. Thank you for your commitment to fostering research and development in the field of energy systems.
