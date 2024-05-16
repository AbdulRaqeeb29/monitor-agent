# monitor-agent
This project aims to address this need by developing a monitor agent that collects CPU and memory usage data from Docker containers and stores it in a MySQL database.  


The development of the monitor agent application has provided a valuable solution for monitoring CPU and memory resource usage within Docker containers. Using DockerPy and MySQL Connector Python, we have successfully created a lightweight and efficient tool that interfaces with the Docker daemon to collect real-time container statistics and store them in a MySQL database.

Two different python files 'monitor_containers' used for the deployment of image that monitors container resources inside the container in docker environment. 'monitor_agent' used for monitoring the resources of the containers and also retrieve the info into the database every 2 minutes.






