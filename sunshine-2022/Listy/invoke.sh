#!/bin/bash

# Ansible-Vault unlock the gcloud credential
CRED=$(ansible-vault decrypt vault.txt --output /tmp/key.json) 

gcloud auth activate-service-account listy-developer@sunshine-2022-challenges.iam.gserviceaccount.com '--key-file=/tmp/key.json'

rm /tmp/key.json

curl -H "Authorization: bearer $(gcloud auth print-identity-token)" https://us-central1-sunshine-2022-challenges.cloudfunctions.net/listy\?bucket\=ssctf22-listy-leaderboard-prod
