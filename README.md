# macserver

Python modules needed:
  Flask
  pyopenssl

macServer.py 
  Is the server which is implemented in Python and uses the Flask WebApplication framework. It implementes a local simple data dictionary of mac address and company names. It looks up this dict to get the info for the input mac address. The server entertains only SSL requests. share the cert.pem with the client applications. (key.pem is not to be shared)


How to start this server by typing the command:
 startServer.sh


###### REST API CLIENT ##############
now,from another command prompt use the "curl" to access and get info.
ensure that the cert.pem is available and in the current folder or specify the path of the file

Example:

curl -k ./cert.pem -i https://127.0.0.1:5000/macServer/D7:A3:E7:FD:58:F5

response: ABC Company


#Building Dockerfile

docker build -t macServer:lateat .

# starting the image

docker run -d -p 5000:5000 macserver:latest

# now check if running

docker ps

The docker image build is in: https://hub.docker.com/repository/docker/ravnatar/macserver

