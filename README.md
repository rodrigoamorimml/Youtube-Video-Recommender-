<h1 align="center">Youtube Video Recommender</h1>
 
#### The project consist of a video recommender from youtube where using a certain number of key words the model search for this videos and ranks the 30 most high score videos using an ensemble of two machine learning models.

The final result can be see it at: [Youtube Video Recommender](https://powerful-plains-65681.herokuapp.com/)




The project can be divided in four steps:
- [ ] *Scrapping the Data*
- [ ] *Processing the Data.*
- [ ] *Modeling and tuning the model.*
- [ ] *Deploying the model.*



### *Scrapping the Data*

For this task it was used a library to scrape the data from the youtube site: [Youtube-DLC](https://github.com/blackjack4494/yt-dlc), where this library can be used to download videos from youtube and other plataforms. For the project, we use the library only to get the metadata informations about the videos, there wasn't need to download. To train the model, it was used 3 queries (key-words) and a  300 videos search for each query, totalizing 900 videos. This was the size of the dataset used to produce the project. The notebook with the code can be see at: [Data Collect](https://github.com/rodrigoamorimml/Youtube-Video-Recommender-/blob/main/Data%20Collect.ipynb)


### *Processing the Data*

The processing step consist on cleaning the data and analysing the features. After looking for the columns in the dataset was set only 3 of this columns to build the model: the title of the video, the quantity of views on those videos and the date that was upload the video. The dataset label was set by me, looking for each video title and putting one on the video that i like and zero if i don't, as a classification task.

To Analyse the data was used the pandas library. In this stage was created a new feature to count the number of views per day, besides that, was ploted a graph about the time each video was upload to see the distribution of the video by the time. With this plot was abled to split the data into training set and validation set, where the proportion was approximaly 64% to training set and 36% to validation set. With only this informations was build the baseline for the model using a simple decision tree model. A baseline is a simple model where we have this model's metrics as our start point, where we need to upgrade this metrics using other models, tunning the hyperparameters or adding/dropping features. The metrics used are the Roc Auc Score where this metric compute the area under the curve , and the average precision score.

To upgrade the model was used the title was a features using a bag-of-words model (BoW). The BoW is a way of extracting features from texts. It's a representantion of text that describes the occurence of words within a document. Also was choose the TF-IDF (Term Frequency Inverse Document Frequency)  measure, it measure the occurencie of words in the vocabulary penalizing the words with high frequencies. The notebook with the code can be see at: [Data Processing](https://github.com/rodrigoamorimml/Youtube-Video-Recommender-/blob/main/Data%20Processing.ipynb)


### *Modeling and tuning the model.*


The next step  consist in modeling the model, in other words,  try some differents machine learning algorithms and feature extraction to upgrade the metrics. After testing some machine learning models and some hyperparameters, using a random search for the hyperparameters to improve the metrics, the final project was set as: an ensemble of two types of models, a Random Forest Classifier and a LGBM(Light Gradient Boosting Machine) Classifier, with this two models was used a 50% participation for each model in the ensemble, this configuration scored best than any of this two models solo. The notebook with the code can be see at: [Data Modeling](https://github.com/rodrigoamorimml/Youtube-Video-Recommender-/blob/main/Data%20Modeling.ipynb)



### *Deploying the model.*


In this section, it takes the model already trained and deploy to the internet, for this task it was used two things, the *Heroku* that is a cloud plataform as a service (PaaS) where we can upload the project to the internet and the *Docker*, docker is  a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers, in other words, we use the container to create a image with the specifics configurations where can be upload to the web via the heroku. All the files need it'ss on the folder called Deploy.


