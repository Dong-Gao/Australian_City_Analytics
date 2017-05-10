# COMP90024 Cluster and Cloud Computing Assignment2 - Australian City Analytics
#### Authors:
    HongZhen Xie:
    Dong Gao: 795622
    NanJiang Li:
    KaiLe Wei:
    Chuang Ying: 844566
## Scenarios Exploration
### Scenario 1: A series of sentiment scenarios
A series of sentiment scenarios are achieved by Dong Gao, including sentiment score analysis for each city, Time-Happiness scenario for cities, and Factors-Happiness Scenario for suburbs.
This part consists of five python files:
sentiment_analysis.py: Input is a tweet json file, and a sentiment tag is the output.
coordinate_tweets.py: Filter out tweets with corridinate attribute.
reverse_geocode.py: Input is a coordinate, and the corresponding suburb is the output.
suburb_analysis.py: Input is a tweet, and the output is the corresponding suburb and sentiment score.
result_plots.py: According to final results, drawing plots using matplotlib library.

### Scenario 2: Cultural Integration


### Scenario 3: Alcohol-Tobacco
The Alcohol-Tobacco Scenario is made by Nanjiang.
This document include one smoke_drink.py, and a text file smoke.txt.
The py file is the function of alcohol-tobacco scenario, and the txt file stores the keywords of the function.
There are two executable functions, smoke_Drink_per(tweet,result) for single tweet analysis, and smoke_Drink() for json file analysis.


### Main.py
The main.py is written by Chuang Ying.
This is a python file for tweets harvesting by REST API to find new users & their tweets before and Streaming API to get current relevant tweets, and saving the tweets into couchdb.

## Web
This folder contains the code used for building web interface
This web interface use a RESTFUL framework. Implementing by Python with Django, 
To run this web interface, 
A Django packages are required and also apache service should open for running this web interface.
Before running, the allow_host should add its IP address.  
To run this interface,  you should run :  python manage.py  run server
U can visit our interface through: 115.146.91.76:8000

## Deployment
There are several files in this folders for the launching and depolying process.
File setupbash.sh: a bash file to run the lanuching and deploying process. 
file dbSetup.yaml : a yaml file for ansible-playbook to deploying the database instances on nectar
File serSetup.yaml : a yaml file for ansible-playbook to deploying the processing server instances on nectar
File hosts: stort the instance's configuration information
nectarConf.sh : configuration of nectar project for ansible to connect to server.
Connect.key: the private key used for connecting the system
By running the setupbash.sh file, it can automatically launch a new instance of harverstserver or database and automatically deploy those required.
Besides, as to how to create a cluster of couchdb, some useful information can be got from:
https://medium.com/linagora-engineering/setting-up-a-couchdb-2-cluster-on-centos-7-8cbf32ae619f
Few things to pay attention:
1. Before running this script, make sure that ansible and openstack has been correctly installed.
2. Make sure that the environmental variable: ANSIBLE_HOST_KEY_CHECKING has been set false,  more information can be viewed: http://stackoverflow.com/questions/32297456/how-to-ignore-ansible-ssh-authenticity-checking
Otherwise, the ssh key connections may refuse.
3.  In this script, the availability zone of new instance has been pre-set as ‘Melbourne’ which guarantee that volume and instance are in the same zone
If there is not enough host in this zone, the launch process may fail.
  
 





