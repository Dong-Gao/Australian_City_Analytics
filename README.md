# COMP90024 Cluster and Cloud Computing Assignment2 - Australian City Analytics
#### Authors:
    HongZhen Xie: 773383
    Dong Gao: 795622
    NanJiang Li: 741524
    KaiLe Wei: 812381
    Chuang Ying: 844566
## Scenarios Exploration
### Scenario 1: A series of sentiment scenarios
A series of sentiment scenarios are achieved by Dong Gao, including sentiment score analysis for each city, Time-Happiness scenario for cities, and Factors-Happiness Scenario for suburbs. <br>
This part consists of five python files:<br>
sentiment_analysis.py: Input is a tweet json file, and a sentiment tag is the output.<br>
coordinate_tweets.py: Filter out tweets with corridinate attribute.<br>
reverse_geocode.py: Input is a coordinate, and the corresponding suburb is the output.<br>
suburb_analysis.py: Input is a tweet, and the output is the corresponding suburb and sentiment score.<br>
result_plots.py: According to final results, drawing plots using matplotlib library.<br>

### Scenario 2: Cultural Integration
The Cultural Integration Scenario is made by KaiLe Wei.<br>
This document include one cultural.py, and a text file keywords.txt.<br>
The py file is the function of cultural integration  scenario, and the txt file stores the keywords of the function.<br>
There are two executable functions, culture_per(tweet,result) for single tweet analysis, and culture_file() for json file analysis.

### Scenario 3: Alcohol-Tobacco
The Alcohol-Tobacco Scenario is made by Nanjiang Li.<br>
This document include one smoke_drink.py, and a text file smoke.txt.<br>
The py file is the function of alcohol-tobacco scenario, and the txt file stores the keywords of the function.<br>
There are two executable functions, smoke_Drink_per(tweet,result) for single tweet analysis, and smoke_Drink() for json file analysis.


### Main.py
The main.py is written by Chuang Ying.<br>
This is a python file for tweets harvesting by REST API to find new users & their tweets before and Streaming API to get current relevant tweets, and saving the tweets into couchdb.

## Web
This folder contains the code used for building web interface.<br>
This web interface use a RESTFUL framework. Implementing by Python with Django.<br>
To run this web interface: <br>
A Django packages are required and also apache service should open for running this web interface.<br>
Before running, the allow_host should add its IP address.  <br>
To run this interface,  you should run :  python manage.py run server.<br>
You can visit our interface through: 115.146.91.76:8000

## Deployment
There are several files in this folders for the launching and depolying process.<br>
File setupbash.sh: a bash file to run the lanuching and deploying process. <br>
File dbSetup.yaml : a yaml file for ansible-playbook to deploying the database instances on nectar.<br>
File serSetup.yaml : a yaml file for ansible-playbook to deploying the processing server instances on nectar.<br>
File hosts: stort the instance's configuration information.<br>
nectarConf.sh : configuration of nectar project for ansible to connect to server.<br>
Connect.key: the private key used for connecting the system.<br>
By running the setupbash.sh file, it can automatically launch a new instance of harverstserver or database and automatically deploy those required.<br>
Besides, as to how to create a cluster of couchdb, some useful information can be got from:<br>
https://medium.com/linagora-engineering/setting-up-a-couchdb-2-cluster-on-centos-7-8cbf32ae619f<br>
Few things to pay attention:<br>
1.Before running this script, make sure that ansible and openstack has been correctly installed.<br>
2.Make sure that the environmental variable: ANSIBLE_HOST_KEY_CHECKING has been set false,  more information can be viewed: http://stackoverflow.com/questions/32297456/how-to-ignore-ansible-ssh-authenticity-checking
Otherwise, the ssh key connections may refuse.<br>
3.In this script, the availability zone of new instance has been pre-set as ‘Melbourne’ which guarantee that volume and instance are in the same zone.<br>
If there is not enough host in this zone, the launch process may fail.<br>
  
 





