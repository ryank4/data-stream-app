# data-stream-app
Microservices based data streaming application 
The project consists of 4 microservices:
  1. Data stream server
  2. Analytics client
  3. Redis data store
  4. Flask web server

Dataset: https://www.kaggle.com/shubamsumbria/traffic-violations-dataset.
The data is streamed from the server to the analytics client via gRPC.
The client performs real time data analysis and stores the results in Redis.
The web server retrieves the results from Redis and displays them on a web page. The results are updated when the page is refreshed.

Enter `docker-compose up` to start up the application.
The web page can be viewed on port 5000. 

Note: if the following error is encountered when running docker-compose up:
 ![image](https://user-images.githubusercontent.com/93801531/165293305-43113a6a-4903-46f6-b819-a289dacadd24.png)
 
Removing this command from the docker-compose file should fix it.
command: ["./wait-for-it.sh", "data_stream:50051", "--timeout=3", "--", "python3", "client.py"]


