# captcha
Captcha service in a docker with python and pillow

## To run: 

docker build -t captcha-service .
docker run -d -p 5000:5000 --name captcha-service captcha-service



## To test 


Just use the `example.html` file for testing purposes. You can adapt this quickly into any web page.


## Endpoints:

http://localhost:5000/generate_captcha

http://localhost:5000/statis/captcha_1.png
