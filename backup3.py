#!/usr/bin/python3

# import modules

import sys
from backupcfg import jobs, usage_msg, job_msg

# global variables

errors = 0
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
        pass #do_backup(job)
    
    # if there are errors, send error email
    if errors:
        
        pass #do_email(job)
        
    # output messages to logfile
    pass #do_logfile(job)

    # exit with zero to indicate normal program execution
    sys.exit(0)