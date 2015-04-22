Solr backup and upload on aws s3 bucket

* Install required dependencies

  pip install requirements.txt

* Setup Variables
  
  sesese3solr_url = "" 		# solr url "http://localhost:8983/solr/"


  backup_dir = ""		# solr backup directory "/home/solr/backup"
  
  
  s3_upload = False		# set to "True" if you want to upload to s3 bucket, default is "False"
  
  
  bucket_name = ""		# s3 bucket name to store backup files
  
  
  AWS_ACCESS_KEY = ""		# aws access key
  
  
  AWS_SECRET = ""		# aws secret key
  
 
* Setup cron job

  * * * 12 05 /path/to/script/solr-backup.py >> /path/to/log/file/solr-backup.log

or 

* Run script

  python solr-backup.py
