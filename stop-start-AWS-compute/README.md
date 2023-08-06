# Stop or start instances based on tag: dev

To run the script, sys argv - '**stop**' or '**start**' on execution of script from cmdline should be specified 

        i.e. ./stop-start-AWS-compute.py start


The script will stop or start instances based on tag: dev

        Note: *tag: dev* will need to updated inside the script, however will look to make this a feature in the future as a sys.argv

Script should typically be run as a cronjob on a schedule, i.e. stop at 7pm every evening mon-fri, and start again at 7am

On sat/sun, the instances should remain off.

    
    * Crontab expression for starting instances Mon-Fri 7am:
        0 7 * * 1-5


    * Crontab expression for stopping instances Mon-Friday 7pm:
        0 19 * * 1-5