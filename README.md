# relay_42_automation
****************************The code is developed is python selenium for relay42*********************************
The following document is a helper to set up the automation ENVIRONMENT on the containers for the text executio
1. The host machine is a ubuntu linux
2. Install docker and VNC veiwer on the host machine 
3. To install docker refer : https://docs.docker.com/install/linux/docker-ce/ubuntu/#os-requirements
4. To install vnc-viewer refer : https://www.realvnc.com/en/connect/download/viewer/linux/
5. on the host do "mkdir /tmp/relay42_results"
6. do a git clone https://github.com/Snehanewuser/relay_42_automation.git
7. Dockerfil contains the  from image repo for the image to be created and the required installables and copies the automation code to the image at /relay42
Use the command to build the image : docker build . -t relay42_automation:0.0.1
Once the image is succesfully built as follows:
docker build . -t relay42_automation:0.0.1
Sending build context to Docker daemon  254.5kB
Step 1/8 : FROM dorowu/ubuntu-desktop-lxde-vnc
 ---> 5d5344948b64
Step 2/8 : RUN sudo apt-get update -y &&     sudo apt-get install python-pip wget curl -y &&     sudo pip install --upgrade pip &&     pip install selenium
 ---> Using cache
 ---> a64cc6ec035d
Step 3/8 : ADD https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz ./
Downloading [==================================================>]  2.688MB/2.688MB
 ---> Using cache
 ---> df62e6b0cb58
Step 4/8 : RUN tar -zxvf ./geckodriver-v0.20.1-linux64.tar.gz -C /usr/local/bin
 ---> Using cache
 ---> a03780a2cf72
Step 5/8 : RUN mkdir /relay42
 ---> Using cache
 ---> 8e8497def28a
Step 6/8 : COPY ./relay_42 /relay42/
 ---> Using cache
 ---> 4e7db927fa39
Step 7/8 : WORKDIR /sneha
 ---> Using cache
 ---> 27e3bc2390f6
Step 8/8 : CMD ["python","relay42_main.py"]
 ---> Using cache
 ---> 077b2ad8065e
Successfully built 077b2ad8065e
Successfully tagged relay42_automation:0.0.1

use docker to launch an instance and also mount the results folder set the web-APP port and the vnc port with instance name

use the following cmd trigger docker run for SINGLE INSTANCE for SINGLE INSTANCE
docker run --rm -p 6080:80 -p 5900:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1
use the following for multiple instance :
docker run --rm -p 6080:80 -p 5900:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1 
and 
docker run --rm -p 6081:80 -p 5901:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1 

The python automation code is designed in a modular manner to make debugging easy and can be executed indepently when in need of trouble shooting.
also the suite contains an.js file support the html5 function where the python-selenium couldn't handle.


the module 
relay42_main.py creates dynamic engagement identity that can used in all the modules and the relay_main.py also contains the function call for all the def functions (create engagement, create audience and audience validation)
relay42_usermodules.py contains all the def functions 
relay42_libmodules.py contains the reporting module used for logging results and info
in order to execute the script locally on the host machine use the following
cd ~/relay_42
python relay42_main.py


