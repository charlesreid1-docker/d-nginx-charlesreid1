import glob
import os

"""
Clean d-nginx-charlesreid1 conf.d directory


This script cleans out the conf.d directory
in the d-nginx-charlesreid1 submodule of this
repository. 

This script should be run before you generate a new set
of config files from the nginx config file templates in
d-nginx-charlesreid1/conf.d_templates/

This script cleans out all the config files in the folder
d-nginx-charlesreid1/conf.d/

That way there are no old config files to clash with the
new ones.
"""

HERE = os.path.abspath(os.path.dirname(__file__))
CONF = os.path.abspath(os.path.join(HERE,'..','conf.d'))

for f in glob.glob(os.path.join(CONF,"*.conf")):
    if os.path.basename(f)!="_.conf":
        cmd = ['rm','-fr',f]
        subprocess.call(cmd)

