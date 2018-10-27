## Unsupervised Speaker Cue Usage Detection in Public Speaking Videos

#### Code for paper:
#### Gupta, A. & Jayagopi, D. (2018). "Unsupervised Speaker Cue Usage Detection in Public Speaking Videos." *Proceedings of the 29th British Machine Vision Conference Workshop, Vision for Interaction and Behaviour undErstanding.* http://anshul-gupta24.github.io/files/paper1.pdf
# </br>

####
### Datasets
#### Download the files 'ted_main.csv' and 'transcripts.csv' from https://www.kaggle.com/rounakbanik/ted-talks.
#### Also download the file 'ted_en-20160408.zip' from https://github.com/mleue/oxford-deep-nlp-2017-solutions/tree/master/practical-2.
#### Download the TED videos from the links provided in the xml file in 'ted_en-20160408.zip'.
#### </br>


### Preprocessing
#### Extract the last 1 minute of every video in the dataset.
#### Run Openpose (https://github.com/CMU-Perceptual-Computing-Lab/openpose) on every clip and store the csv files in TED/cuts_csv.
#### Run PysceneDetect (https://github.com/Breakthrough/PySceneDetect) on every clip and store the csv files in TED/shots. </br> </br>
#### NOTE: Maintain naming scheme as in the sample files in the folders. </br></br>
#### Remove videos with tags such as 'Performance' and 'live music'. To see a list of all tags sorted by frequency of occurence run:
#### >>python get_tags.py
#### To modify the tags whose videos you want to remove, edit the \<keywords\> list in 'get_performance.py'. Then run:
#### >>python get_performance.py </br> >>python remove_performance.py
#### This moves the csv files of the unwanted videos from 'TED/cuts_csv' to 'TED/removed_csv'. 
#### </br>

### Running the Code
#### __To get quantise the amount of walking, run:__
#### >>python /walk/cluster.py
#### This creates three files labels1.txt, labels2.txt and labels3.txt, containing the video names corresponding to the amount of cue usage.
#### To sample videos from any of the clusters, run:
#### >>python sample_videos \<labelX.txt\>
#### Modify the number of samples to be drawn with the 'num_samples' variable.
#### </br>

#### __To get quantise the amount of lateral head movement, run:__
#### >>python /head/cluster.py
#### This creates three files labels1.txt, labels2.txt and labels3.txt, containing the video names corresponding to the amount of cue usage.
#### To sample videos from any of the clusters, run:
#### >>python sample_videos \<labelX.txt\>
#### Modify the number of samples to be drawn with the 'num_samples' variable.
