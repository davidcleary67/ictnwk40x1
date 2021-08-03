jobs = {"job1": ['/home/ec2-user/environment/ictnwk40x1/file1','/home/ec2-user/environment/ictnwk40x1/backup'],
        "job2": ['/home/ec2-user/environment/ictnwk40x1/file2','/home/ec2-user/environment/ictnwk40x1/backup'],
        "job3": ['/home/ec2-user/environment/ictnwk40x1/file3','/home/ec2-user/environment/ictnwk40x1/backup'],
        "job4": ['/home/ec2-user/environment/ictnwk40x1/dir1','/home/ec2-user/environment/ictnwk40x1/backup'],
        "job5": ['/home/ec2-user/environment/ictnwk40x1/dir1','/home/ec2-user/environment/ictnwk40x1/backup1']}

usage_msg = "Usage: python backup.py <job name from backupcfg.py>"
job_msg = "Error: job '%s' not in jobs list"
logfile = "/home/ec2-user/environment/ictnwk40x1/backup.log"

email = {"recipient": "dcleary@sunitafe.edu.au",
         "user": "dcleary@sunitafe.edu.au",
         "pwd": "xxxxxx",
         "server": "mail.example.com",
         "port": 587}