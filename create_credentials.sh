#!/usr/bin/env bash
if [ ! -f ~/.credentials.json ]
then echo '{"atlas_login": "atlas_login", "atlas_password": "atlas_password"}' > ~/.credentials.json
fi
