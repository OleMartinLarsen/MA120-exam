# MA120 Big Data Exam
In the exam we have used Hadoop to analyze a dataset from Bitcoin Stack Exchange (www.stackexchange.com). Bitcoin Stack Exchange is a question and answer site for Bitcoin crypto-currency enthusiasts.

The dataset is an anonymized dump of all user-contributed content on the Bitcoin stack exchange network.  The dataset is available from: 
archive.org/download/stackexchange/bitcoin.stackexchange.com.7z

The dataset is formatted as a separate archive consisting of XML files. The archive includes:

	● Badges.xml
	● Comments.xml
	● PostHistory.xml
	● PostLinks.xml
	● Posts.xml
	● Tags.xml
	● Users.xml
	● Votes.xml

# Setup
This is how you setup the environment to run this project.

## Download
Download the project manually:

![enter image description here](https://lh3.googleusercontent.com/6BfFd_oH6d-G8_mKxdPdregNR3JsToxve12zEjim3RsY_o2BFvqChdObF7V6p7gbPfa2QUBuO8SV)

Download the project with git clone:

    git clone https://github.com/OleMartinLarsen/MA120-exam.git


## Docker
For this project you need to have docker installed.
### Installation
1. Install docker (if you don't have it, requires docker id): https://hub.docker.com/?overlay=onboarding
2. Run this command inside project folder to start hadoop: 
``docker run -it -v "\`pwd`"/:/hadoop kristiania/hadoop /start``
3. You can then find the project files inside `hadoop/`
## pip
pip is the package installer for Python. We use this to install the packages needed for this project.
### Installation

    apt-get install python3-pip
   If the error "E: Unable to fetch some archives", run:

    apt-get update

## lxml
lxml is a Python library we use which allows for easy handling of XML. This is what we use to parse the xml files in the dataset.
### Installation

    pip3 install lxml
## NLTK

NLTK, or the Natural Language Toolkit, is a library for text preprocessing. We use NLTK to get stopwords, tokenize text and make n-grams.
### Installation
1. `pip3 install -U nltk` 
2. Run python: `python3` 
3. `import nltk`
4. `nltk.download('stopwords')`
5. `nltk.download('punkt')`
6. Then you can run `exit()` to exit python
## HDFS
You need to upload the dataset to HDFS (Hadoop Distributed File System) before you can run the MapReduce jobs. You also need to upload the data the pig script is going to use.

1. You need to navigate inside the hadoop folder: `cd hadoop`
2. To upload the dataset: `hadoop fs -copyFromLocal Dataset`
3. To upload the data for pig script: `hadoop fs -copyFromLocal 1e_PigTop10/data`

You can use `hadoop fs -ls` to see the data in the HDFS.
## Encoding
You need to specify what encoding python is going to use. Your termianl can typically handle UTF8 characters just fine. The issue is actually that Python is just getting confused about what encoding the terminal accepts. However, you can explicitly set this value. 

Run this command: `export PYTHONIOENCODING=utf8` 

# Usage
Here we will go trough examples of how you can use the project.
## How to run a MapReduce job
This is how you run a MapReduce job.
1. You navigate inside the folder of the MapReduce job you want to execute. For example:`cd 1a_WordCount`
2. Then you run: `bash run.sh`.

Inside the `run.sh` file is a Hadoop streaming command which starts the MapReduce job. This command generates a folder for the output inside the HDFS. The folder has the same name as the MapReduce job, so in this example the name is `1a_WordCount`. Inside the folder 2 files are generated, `_SUCCESS` and `part-00000`. Inside the `part-00000` is the data.

### Commands for displaying the data the MapReduce jobs produces.
#### All the data

    hadoop fs -cat '1a_WordCount/part-00000' | more
#### The first 10 lines

    
    hadoop fs -cat '1a_WordCount/part-00000' | head -10

#### The last 10 lines

    
    hadoop fs -cat '1a_WordCount/part-00000' | tail -10
## How to run a Pig script
Inside the folder `1e_PigTop10` we have a Pig script which makes a top 10 list of words from the data file we uploaded to the HDFS. This data file is a file which is produced by the MapReduce job inside the `1d_Stopwords` folder, were all the stopwords gets removed from the titles of questions.

This is how you run the Pig script.
1. Navigate inside the folder were the pig script is: `1e_PigTop10`
2. Then you run this command to execute the Pig script: `pig top10.pig`



