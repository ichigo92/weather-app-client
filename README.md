# Weather App

Weather app is a cloud based application, the application performs CRUD operations on weather data for different cities.

When a user adds a new city, the application retrieves the current weather from an external api openweathermap.org, and stores the city in Cassandra.

The CRUD operations are performed on the data in the database

# Docker

Commands for docker

`docker build . --tag=weather_client_image:v1`

`docker run -p 8080:8081 weather_client_image:v1`