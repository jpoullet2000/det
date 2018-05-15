#!/usr/bin/env bash
if [ ! -f ~/.credentials.json ]
then echo '{"ATLAS_LOGIN": "atlas_login", "ATLAS_PASSWORD": "atlas_password", "AMBARI_LOGIN": "ambari_login", "AMBARI_PASSWORD": "ambari_password", "DET_API_TOKEN": "mytoken", "DET_API_ADMIN_TOKEN": "admintoken", "TEST_FLAG": true}' > ~/.credentials.json
chmod 600 ~/.credentials.json
fi
