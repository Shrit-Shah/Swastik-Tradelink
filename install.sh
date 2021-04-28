#!/bin/bash

sudo yum install python3 python3-pip -y

pip3 install virtualenv

virtualenv ve
source ve/bin/activate

pip3 install django django.db Pillow whitenoise