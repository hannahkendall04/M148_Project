# UCLA M148: Introduction to Data Science Project

## Introduction
Hello! This is the repository for our M148 project. Throughout the quarter, we applied the data science techniques we learned in class to analyze a dataset of our choice. We chose to analyze the [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset), with the initial goal of classifying songs into different genres based on their audio features. We also explored other aspects of the dataset, such as the relationship between audio features and popularity, and the distribution of genres in the dataset. 

The data set includes 114000 songs with 133 genres. Each track is defined by 19 audio features, described in the table below:

| Feature | Description |
| --- | --- |
| artists | Name of the artist(s) |
| album_name | The album name in which the track appears |
| popularity | The popularity of the track on a scale of 0-100 |
| duration_ms | The duration of the track in milliseconds |
| explicit | Whether the track has explicit lyrics (T/F) |
| danceability | A measure of how suitable a track is for dancing on a scale of 0-1, 1 being the most danceable |
| energy | A measure of intensity and activity on a scale of 0-1, 1 being the most intense |
| key | The key of the track: 0 = C, 1 = Csharp/Dflat, 2 = D and so on. No key is -1 |
| loudness | The overall loudness of the track in decibels (dB) |
| mode | The modality of the track: 0 = minor, 1 = major |
| speechiness | A measure of the presence of spoken words in the track on a scale of 0-1, 1 being the most speech-like |
| acousticness | A measure of the amount of acoustic sounds in the track on a scale of 0-1, 1 being the most acoustic |
| instrumentalness | A measure of the amount of instrumental sounds in the track on a scale of 0-1, 1 being the most instrumental |
| liveness | A measure of the presence of a live audience in the track on a scale of 0-1, 1 being the most live |
| valence | A measure of the musical positiveness conveyed by a track on a scale of 0-1, 1 being the most positive |
| tempo | The tempo of the track in beats per minute (BPM) |
| time_signature | The time signature of the track (3-7) |
| track_genre | The genre of the track |

## Main Goal
The main problem we addressed was the classification of songs into different genres based on their audio features. We used a variety of classification algorithms, such as Logistic Regression, Random Forest, and clustering algorithms, to classify songs into genres. We also used a neural network to classify songs into genres. We then evaluated the performance of the models using various error metrics.

## Model Overviews and Results
Since our model's response variable is categorical (genre), it would not make sense to apply linear regression as a predictive model. The first model we tried was Logistic Regression. However, since logistic regression measures the probability of each song belonging to a positive or negative class, the logistic regression could only determine if a song belongs to genre 1 or 2. For our investigation, we picked the two genres, chicago house and canto-pop, due to the fact that there were an equal number of samples of the genres in the original dataset and because they have distinct audio features. We used forward selection  (SequentialFeatureSelector) on our logistic regression training set to greedily select for features that maximized accuracy when we did cross-validation. From this we found that our best features were danceability,  acousticness, instrumentalness, and time signature. We had a high accuracy of 0.875, true positive rate of 0.9, and true negative rate of 0.85, suggesting that our logistic regression performed well. Our AUC was high at 0.946. We also used cross validation to evaluate model performance and got high accuracies. It is possible that our model is overfitting which is resulting in such high accuracy and AUC. However, it is also possible that our model is performing well because we specifically chose genres (canto-pop and chicago-house) that are very different from each other. Because of our high initial accuracy, we did not use regularization in our logistic regression model, or for the other machine learning models we utilized. Future work could involve using regularization to prevent overfitting and to improve the generalizability of our model.

We also classified the data using Decision Trees and the Random Forest algorithm, the results of which are summarized below:

```
Decision Tree Classifier Accuracy: 0.955
Decision Tree Classifier Error: 0.04500000000000004
Decision Tree Classifier F1 Score: 0.9538461538461539
Decision Tree Classifier Model TPR: 0.93
Decision Tree Classifier Model TNR: 0.98

Random Forest Model Accuracy: 0.98
Random Forest Model Error: 0.020000000000000018
Random Forest Model F1 Score: 0.9798994974874371
Random Model TPR: 0.975
Random Model TNR: 0.985
Random Forest Model AUC: 0.9958875
Random Forest Model CV AUC: 0.9984374999999999, 0.9896875, 0.9975, 1.0, 0.996875
Random Forest Model CV Accuracy: 0.975, 0.9625, 0.9625, 1.0, 0.95
```

The AUC is particularly interesting because it is a measure of how well the model can distinguish between the two classes. The AUC (which is 0.9958875) is close to 1.0. This indicates a nearly perfect model performance. This could be an indication of overfitting, but it could also be an indication that the model is performing well, which is not surprising given the distinct audio features of the two genres we chose to classify.

Despite our success with these machine learning methods, our primary methodology for classifying songs into genres was through PCA and clustering algorithms. We chose these as our primary methodology because we wanted to create a model that is easy to visualize, gives us lots of information about the data set, and is easy to scale to an arbitrary number of genres. We used PCA on our scaled data to determine the most significant features in our data set. We then used KMeans and Hierarchical clustering on several different sets of genres to analyze the effectiveness of clustering for classifying genres. Both Kmeans and Hierarchical clustering performed well with classifying chicago house and canto-pop genres, with results shown below:

```
KMeans Accuracy: 0.9208416833667334
KMeans Error Rate: 0.07915831663326656
KMeans Silhouette Score: 0.36934642389667216

Hierarchical Accuracy: 0.16182364729458917
Hierarchical Error Rate: 0.8381763527054108
Hierarchical Silhouette Score: 0.34069147956129936
```

The results for both clustering algorithms performed significantly worse than the machine learning models. This is likely because the clustering algorithms are unsupervised and do not have the same level of information about the data as the supervised machine learning models. However, the clustering algorithms are still useful for visualizing the data and for understanding the relationships between the genres in the dataset. Additionally, the clustering algorithms are easily scalable to an arbitrary number of genres, which is useful for future work.

## How to Use
If you would like to run through our entire project, check out our `final_code.ipynb` file. If you would like to look at some more modularized versions of our process, check out the files in the `Data` directory.

### Set-Up (for local development on VSCode)
1. Install VSCode from [here](https://code.visualstudio.com/).
2. Open VSCode and create a project directory by clicking on the "Open Folder" button on the welcome screen.
3. From the directory you created, open the terminal by pressing Ctrl+` (or by going to 'View > Terminal') and clone the repository by running the following command:
```bash
git clone https://github.com/atan9611/M148_Project.git
```
4. Create a virtual environment
    * Make sure you have Python installed on your system. If not, download it from [here](https://www.python.org/downloads/).
    * The `requirements.txt` file can be found in the utils directory in this repository.
    * On Mac:
    ```bash
    python -m virtualenv env
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    * On Windows:
    ```bash
    python -m virtualenv env
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
5. Now you are free to make and run .ipynb files in the project directory!
    * Note: when running cells in a .ipynb file, select the virtual environment you created earlier when prompted by VSCode to select a kernel.
6. To run the entire project, select the `final_code.ipynb` file and run all cells. 
    * You can also go to each individual section and run the cells one by one to see the output of each step.
    * The code is designed to be modular, so you can run each section independently of the others. It is also designed to be able to easily change the genres you are classifying, the features you are using, and the models you are using. Feel free to experiment with different combinations!
