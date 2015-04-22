#!/usr/bin/env python

# import requirements
import os
import requests
from datetime import datetime
from boto.s3.key import Key
from boto.s3.connection import S3Connection


# setup solr replication for backup
# Ref URL : https://cwiki.apache.org/confluence/display/solr/Index+Replication

###################################
#
#<requestHandler name="/replication" class="solr.ReplicationHandler" >
#    <lst name="master">
#        <str name="replicateAfter">optimize</str>
#        <str name="backupAfter">optimize</str>
#        <str name="confFiles">schema.xml,stopwords.txt,elevate.xml</str>
#    </lst>
#</requestHandler>
#
###################################


# setup variables
solr_url = "" 			# solr url "http://localhost:8983/solr/"
backup_dir = ""			# solr backup directory "/home/solr/backup"
bucket_name = ""		# s3 bucket name to store backup files 
AWS_ACCESS_KEY = ""		# aws access key
AWS_SECRET = ""			# aws secret key


def solr_backup():
	# set backup name
	backup_name = "solr-backup-" + datetime.now().strftime("%Y-%M-%d-%H-%M")
	
	# solr url to call backup api
	url = solr_url + "replication?command=backup&location="+backup_dir+"&name="+backup_name+"&wt=json"
	res = requests.get(url)
	
	# tar file name to upload
	tar_file_name = backup_dir + backup_name + ".tar.bz2 "
	cmd = "tar -jcvf " + tar_file_name + "-C " + backup_dir + backup_name + " " + backup_name
	os.system(cmd)

	# create s3 connection and upload tar file
	conn = S3Connection(AWS_ACCESS_KEY, AWS_SECRET)
	bucket = conn.get_bucket(bucket_name)
	s3_bckup_file = Key(bucket)
	s3_backup_file.key = backup_name + ".tar.bz2"
	s3_backup_file.set_contents_from_file = (tar_file_name, {'Content-Type':'application/x-tar'})
	
	# status of last backup
	status_url = solr_url = "replication?command=details&wt=json"
	res = requests.get(status_url)
	output = res.json()
	try:
		print "Start Time: ", output['details']['backup'][1]
		print "End Time: ", output['details']['backup'][7]
		print "Backup Status: ", output['details']['backup'][5]
		print "Backup File Count: ", output['details']['backup'][3]
		print "Backup Name: ", output['details']['backup'][9]
	except:
		pass

if __name__ == '__main__':
	solr_backup()