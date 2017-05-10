#!/bin/bash

#this file is used for launching instances on nectar and 
#deploying instances  with necassary packages
# version 2.0 by hongzhenx-773383


echo "Enter the name of new instance you want to lanuch:"
# get new instance name and its type from command line 
read newInsName 

echo "Choose the role of this instance: 1. harverstserver 2. couchdb node 3. both "
read instype

echo "Give the path of host file."
read host_path

echo "Give the path of key file."
read KeyPath


echo $newInsName
echo $instype
echo $host_path

#config openstack file, defines the servers information 
. nectarConf.sh 

#create a new instance from iso image 
IP_ADDR=`openstack server create --flavor 1 --image '866431b3-fcf4-474c-b678-18ad67894cc9' \
    --key-name 'yc' --security-group  'dou' --availability-zone 'melbourne-qh2' \
    --wait --column 'accessIPv4' $newInsName | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}'`

echo $IP_ADDR


#create a volume for the new instace
openstack volume create --availability-zone 'melbourne-qh2' --size 30 --bootable $newInsName


#add the new volume to this new instance
openstack server add volume $newInsName $newInsName --device /dev/vda

#list the volume 
openstack volume list


#base one the instype, make different deployment
case "$instype" in
"1")
    #create host file based on role
    filecontent="[harverstServer]"
    echo $filecontent > hosts

    filecontent=$IP_ADDR" ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file="$KeyPath
    echo $filecontent >> hosts

    #using ansible to make deployment of a harverstserver
    echo "start deployment for a harverstserver"
    ANSIBLE_NO_LOG=False ansible-playbook serSetup.yaml -i $host_path -vvv
    ;;
"2")

    filecontent="[database]"
    echo $filecontent > hosts

    filecontent=$IP_ADDR" ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file="$KeyPath
    echo $filecontent >> hosts

    #make deployment of a database
    echo "start deployment for a database"
    ANSIBLE_NO_LOG=False ansible-playbook dbSetup.yaml -i $host_path -vvv
    ;;
*)  
    filecontent="[harverstServer]"
    echo $filecontent > hosts

    filecontent=$IP_ADDR" ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file="$KeyPath
    echo $filecontent >> hosts

    filecontent="[database]"
    echo $filecontent >> hosts

    filecontent=$IP_ADDR" ansible_connection=ssh ansible_user=ubuntu ansible_ssh_private_key_file="$KeyPath
    echo $filecontent >> hosts

    echo "start deployment for a harverstserver"
    ANSIBLE_NO_LOG=False ansible-playbook serSetup.yaml -i $host_path -vvv


    echo "start deployment for a database"
    ANSIBLE_NO_LOG=False ansible-playbook dbSetup.yaml -i $host_path -vvv
    ;;
esac

