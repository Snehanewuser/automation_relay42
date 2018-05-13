# relay_42_automation: Create an engagement, Create an engagement, Emulate a visit to the product page and Check that the user has entered the audience
****************************The code is developed is python selenium for relay42*********************************
The following document is a helper to set up the automation ENVIRONMENT on the containers for the test execution

1.The host machine is a ubuntu linux

2.Install docker and VNC veiwer on the host machine 

3.To install docker refer : https://docs.docker.com/install/linux/docker-ce/ubuntu/#os-requirements

4.To install vnc-viewer refer : https://www.realvnc.com/en/connect/download/viewer/linux/

5.on the host do "mkdir /tmp/relay42_results"

6.on the host do a  "git clone https://github.com/Snehanewuser/automation_relay42.git"
 
7. on the host do cd ~/automation_relay42/relay42_automation/

8.The Dockerfile at ~/automation_relay42/relay42_automation/ contains the details about how to build a docker image from the repo  and install the required installables and copies the automation code to the image at ~/automation_relay42/relay42

9.Use the following command to build the image : 

docker build . -t relay42_automation:0.0.1

10. use docker run to launch an instance and also mount the results folder, set the web-APP port and the vnc port with instance name

11. use the following cmd to trigger docker run for SINGLE INSTANCE :
docker run --rm -p 6080:80 -p 5900:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1

12. use the following cmd for multiple instance :
docker run --rm -p 6080:80 -p 5900:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1 

and 

docker run --rm -p 6081:80 -p 5901:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1 

13. The python automation code is designed in a modular manner to make debugging easy and can be executed independently when in need of trouble shooting.

14. The automation suite also contains a.js file support the html5 function to over python-selenium limitations.

15. THE AUTOMATION CODE at ~/automation_relay42/relay42_automation/relay_42 contains the automation suite.

16.Brief description about the modules is as follows:

relay42_main.py creates dynamic engagement identity that can used in all the modules and the relay_main.py also contains the function call for all the def functions (create engagement, create audience and audience validation)

relay42_usermodules.py contains all the def functions 

relay42_libmodules.py contains the reporting module used for logging results and info

in order to execute the script locally on the host machine use the following

cd ~/automation_relay42/relay42_automation/relay_42

python relay42_main.py
