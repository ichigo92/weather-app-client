docker build . --tag=weather_client_image:v1

docker run -p 8080:8081 weather_client_image:v1