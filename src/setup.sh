#bash script to add env variables

set -a
source config.env
set +a

#printing env variables for user to verify
python3 import_env.py

echo ''
echo 'please check the token and URL'
echo ''
echo 'cli application starting in 3 sec'
sleep .5
clear

#running the main python file TBD
python3 ticketviewer/ticketviewer.py