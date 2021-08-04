#!/usr/bin/python3

# import modules

import sys
import os
import pathlib
import shutil
from datetime import datetime
from backupcfg import jobs, usage_msg, job_msg

# global variables

errors = 0
messages = []
date_string = datetime.now().strftime("%Y%m%d-%H%M%S")

# functions

# backup the file or directory described in job
def do_backup(job):

    global errors
    global messages
    global date_string
    
    # get the source and destination
    src = jobs[job][0]
    dst = jobs[job][1]

    # check the src exists
    if not os.path.exists(src):
        messages.append("Source '" + src + "' does not exist -> FAIL")
        errors += 1
        
    # check the destination exists
    if not os.path.exists(dst):
        messages.append("Destination '" + dst + "' does not exist -> FAIL")
        errors += 1
 
    # if both source and destination exist, continue
    if not errors:
        
        # determine if source is a file or directory
        is_a_dir = pathlib.Path(src).is_dir()
        is_a_file = pathlib.Path(src).is_file()
        
        # create destination path
        src_path = pathlib.PurePath(src)
        dst_path = dst + "/" + src_path.name + "-" + date_string

        # determine if source is a file or directory
        is_a_dir = pathlib.Path(src).is_dir()
        is_a_file = pathlib.Path(src).is_file()
        
        # backup file
        if is_a_file:
            
            try:
                shutil.copy2(src, dst_path)
                messages.append("Backup file job '" + job + "' -> SUCCEED")
            except:
                messages.append("Backup file job '" + job + "' -> FAIL")
                errors += 1
 
        # backup directory
        elif is_a_dir:
            
            try:
                shutil.copytree(src, dst_path)
                messages.append("Backup directory job '" + job + "' -> SUCCEED")
            except:
                messages.append("Backup directory job '" + job + "' -> FAIL")
                errors += 1


# main program

# check correct number of command line arguments
if len(sys.argv) != 2:
    
    print(usage_msg)
    
else:

    # get and check job name
    job = sys.argv[1]
    
    if job not in jobs:
        
        print(job_msg % (job))
        
    else:

        # perform backup as described in current job        
        do_backup(job)
    
    # if there are errors, send error email
    if errors:
        
        pass #do_email(job)
        
    # output messages to logfile
    pass #do_logfile(job)

    # exit with zero to indicate normal program execution
    sys.exit(0)