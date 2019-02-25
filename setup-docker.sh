docker pull mysql:5.7

docker build -t assignment1 .

docker network create assignment1-cloud

docker run -p 3307:3306 -d --name db --net assignment1-cloud -v /data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=adminuser -e MYSQL_DATABASE=BOOKSINFO -d mysql:5.7

docker run --name assignment1-connector --net assignment1-cloud --link db:mysql -d assignment1

docker  run -d --net assignment1-cloud -p 5001:5000 --name assignment1-cloudcomputing assignment1
