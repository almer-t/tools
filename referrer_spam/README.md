Referrer Spam
=============

The joy of every website: referrer spam *sigh*. The scripts here help you combat referrer spam both at the server-level and the level of analytics tracking.

nginx-refspam-config-gen.py
---------------------------
This script can create an configuration file for nginx based on an external
file with referrer spam urls. To use this:

     ./nginx-refspam-config-gen.py --help

will show you the arguments.

You can execute this directly (with root rights) on a server running nginx, by default it will pull the spamlist from https://github.com/piwik/referrer-spam-blacklist. However, you can use any text file with a url one each line as input.
The output will be written to /etc/nginx/conf.d/referrer-blacklist.conf, which on many configurations is the default for custom nginx files (you made need to change this depending on your server configuration). For regular updates, put this under a cron job.

The file written provides nginx with a simple binary map that it can use to determine if someone is a bad_referrer. You will still need to instruct nginx to use than information, which you can do as follows.

You will need to add this inside your nginx 'server' section to actually block the referrer spam.

     if ($bad_referrer) { 
          return 403; 
     }

Restarting your nginx server will be enough. As a simple test you can try something like this:

     curl -k --referer http://4webmasters.org http://<yoursite>

This should give you a 403 error and not return any content.

regex-refspam-gen.py
--------------------
This script generates a regular expression that you can paste in an analytics console. One application of this is to create a separate segment in something like Google Analytics. You can run the script as regular user (this uses the default list of referrer spam urls, see previous section):

    ./regex-refspam-gen.py

This will output some statistics and a long regular expression at the end. To use this in a Google Analytics segment:

   1. Go to your analytics console and enter the Admin section.
   2. Onder Personal Tools & Assets find "Segments"
   3. Create a new Segment with a descriptive name (e.g. "Excluding Referrer Spam")
   4. As filter add "Sessions" with condition "Exclude"
   5. To the filter add a "Source" condition, set it to "matches regex" and then paste the output of this script in th field.
   6. Save
   
NOTE: Google Analytics does't seem to handle domain names with unicode characters well (and Python escapes such characters)
so I suggest leaving those out for now.

You can now select the Segment in analytics. This will show statistics (in fact: all your past statistics as well) excluding
referrer spam.
