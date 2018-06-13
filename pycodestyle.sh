#!/bin/bash
XARGS="xargs -0 -t pycodestyle"
for pyfile in `ls ./det/*.py`; do python dev/stripspace.py $pyfile; done
find ./det/ -name '*.py' -print0 | ${XARGS} --ignore=E501
