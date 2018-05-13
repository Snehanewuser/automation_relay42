# relay_42_automation
****************************The code is developed is python selenium for relay42*********************************
The following document is a helper to set up the automation ENVIRONMENT on the containers for the test execution
1. The host machine is a ubuntu linux
2. Install docker and VNC veiwer on the host machine 
3. To install docker refer : https://docs.docker.com/install/linux/docker-ce/ubuntu/#os-requirements
4. To install vnc-viewer refer : https://www.realvnc.com/en/connect/download/viewer/linux/
5. on the host do "mkdir /tmp/relay42_results"
6. on the host do a  "git clone https://github.com/Snehanewuser/automation_relay42.git"
 
7. on the host do cd ~/automation_relay42/relay42_automation/

8.The Dockerfile at ~/automation_relay42/relay42_automation/ contains the from image repo for the image to be created and the required installables and copies the automation code to the image at /relay42

9.Use the command to build the image : 

10. docker build . -t relay42_automation:0.0.1

11. use docker run to launch an instance and also mount the results folder, set the web-APP port and the vnc port with instance name

12. use the following cmd trigger docker run for SINGLE INSTANCE :

13.docker run --rm -p 6080:80 -p 5900:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1

14. use the following for multiple instance :

docker run --rm -p 6080:80 -p 5900:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1 

and 

docker run --rm -p 6081:80 -p 5901:5900 -v /tmp/relay42_results:/tmp/relay42_results relay42_automation:0.0.1 

15. The python automation code is designed in a modular manner to make debugging easy and can be executed independently when in need of trouble shooting.

16. The automation also the suite contains an.js file support the html5 function where the python-selenium couldn't handle.

17. THE AUTOMATION CODE at ~/automation_relay42/relay42_automation/relay_42 contains the automation suite.

18.Brief description about the modules is as follows:

relay42_main.py creates dynamic engagement identity that can used in all the modules and the relay_main.py also contains the function call for all the def functions (create engagement, create audience and audience validation)

relay42_usermodules.py contains all the def functions 

relay42_libmodules.py contains the reporting module used for logging results and info

in order to execute the script locally on the host machine use the following

cd ~/automation_relay42/relay42_automation/relay_42

python relay42_main.py
