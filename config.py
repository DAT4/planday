'''
allday_days are days where you are avalible all day
early_days are days where you are avalible from BASTARD_OPEN to EARLY_END
late_days are days where you are avalible from LATE_START to BASTARD_CLOSE
free_days are days where you are not avalible
'''

# Slow internet requires longer SLEEP_TIME
SLEEP_TIME = 3

USERNAME = 'your@email.com'
PASSWORD = 'yourp4s5w0rd'

BASTARD_OPEN    = '10:30'
BASTARD_CLOSE   = '02:00'
EARLY_END       = '20:00'
LATE_START      = '18:00'

#days has to be in danish
allday_days = ['lørdag','onsdag']
early_days  = ['søndag']
late_days   = ['fredag']
free_days   = ['mandag','tirsdag','torsdag']
