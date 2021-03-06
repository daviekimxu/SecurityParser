# SecurityParser

This script will parse through an unencrypted Artifactory security.xml to look for usernames, passwords and user properties that start with AM6J.
Unencrypted values that start with "AM6J" can interfere with encryption and subsequent export/import functions.

After running this tool, review the findings in log.txt and address the violation in Artifactory.
*****************************

Instructions:
1. Download the files to a local directory
2. run POST /api/system/decrypt against your artifactory server
3. run GET /api/system/security to get security.xml
4. run POST /api/system/encrypt to restore encryption
5. move security.xml to the same directory as the security parser
6. Run python securityParser.py
7. Violations will appear in log.txt with the username and/or offending entries containing "AM6J"
