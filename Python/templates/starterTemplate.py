# Borrowed from https://github.com/traderres
# Displays the name of the script along with the date/time of when the script starts and finishes.

#######################################################################
# Filename:  sample.py
# Author:    <your name>
#######################################################################
# Purpose:
#   To be used as a standard template for python scripts
#
# Usage
#   DOS> python sample.py
#
# Assumptions
#   A) python is in the PATH
#######################################################################
import os
import sys
import time


gsScriptName = os.path.basename(__file__)

# Print the date/time when this script started
print("%s has started as of %s." % (gsScriptName, time.strftime("%c")))


# Python Script does something here



# Print the date/time when this script finished
print("%s has finished as of %s." % (gsScriptName, time.strftime("%c")))

# Python script ends here
sys.exit(0)