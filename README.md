# Youtube Video Recommender 
 
#### The project consist of a video recommender from youtube where using a certain number of key words the model search for this videos and ranks the 30 most high score videos using an ensemble of two machine learning models.

The final result can be see it at: [Youtube Video Recommender](https://powerful-plains-65681.herokuapp.com/)


The project can be divided in four steps:
- [ ] *Scrapping the Data.*
- [ ] *Processing the Data.*
- [ ] *Modeling and tuning the model.*
- [ ] *Deploy the model.*



### *Scrapping the Data*

For this task it was used a library to scrape the data from the youtube site: [Youtube-DLC](https://github.com/blackjack4494/yt-dlc), where this library can be used to download videos from youtube and other plataforms. For the project, we use the library only to get the metadata informations about the videos, there wasn't need to download. To train the model, it was used 3 queries (key-words) and a  300 videos search for each query, totalizing 900 videos. This was the size of the dataset used to produce the project. The notebook with the code can be see at: [Data Collect](https://github.com/rodrigoamorimml/Youtube-Video-Recommender-/blob/main/Data%20Collect.ipynb)


### *Processing the Data*

In the second step,  processing step consist on cleaning the data and analysing the features. After looking for the columns in the dataset was set only 3 of this columns to build the model. the title of the video, the quantity of views on this videos and the date that was upload the video. The dataset label was set by me, looking for each video title and putting one on the video that i like and zero if not, as a classification task.

To Analyse the data was used the pandas library. In this stage was created a new feature to count the number of views per day. Besides that was ploted a graph about the time each video was upload to see the distribution of the video by the time. With this plot was abled to split the data into training set and validation set, where the proportion was approximaly 64% to training set and 36% to validation set.

