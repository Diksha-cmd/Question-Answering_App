# About Web App </br>

This web applicatoon has been designed to hep users fetch answers to questions using numnerous NLP models . Users willl be able to view the list ov aviailbale models , add new models , delete existing models , ask a question and upload a CSV with bulk questions </br></br>

# Web App URL </br>
https://webapp-sueoei3pla-uc.a.run.app

# How to use this web app </br>

To use this app : Click on the above URL

# System Architecture</br>
![image](https://user-images.githubusercontent.com/69768815/120727045-867f3c00-c4a7-11eb-8feb-d2e7020f76a8.png)

## You should be able to see below layout :

## Get Models </br>
Returns the list of existing models in the system </br>
![image](https://user-images.githubusercontent.com/84538282/120740360-12519200-c4c1-11eb-8294-bae031c545fc.png)

## Put models </br>
Let's you add a new model and will return a list of existing models </br>
![image](https://user-images.githubusercontent.com/84538282/120740555-69576700-c4c1-11eb-8587-53283db154c0.png)

## Delete models</br>
Let's you delete an existing model and will return the list of remaining models </br>
![image](https://user-images.githubusercontent.com/84538282/120740617-8429db80-c4c1-11eb-9f3b-54237b508d64.png)

## Question/Answer</br>
Use this to post your questions along with context . You may select a model as well </br>

## Upload Questions</br>
Use this to bulk upload your questions using a CSV </br>
![image](https://user-images.githubusercontent.com/84538282/120740677-ab80a880-c4c1-11eb-8e18-a4becfc22efe.png)

Sample CSV</br>
![image](https://user-images.githubusercontent.com/84538282/120740754-d10db200-c4c1-11eb-867f-dace69bd32cf.png)

# Prerequisites and Installation </br>
To run this web application, you'll need the following pre-requisites installed on your machine

| Library | Version | Installation |
| ----------- | ----------- | --------- |
| Python | 3.9.1 or above | <a href="https://www.python.org/downloads/"> Python </a> |
| Streamlit | 0.82.0 | `pip install streamlit`|
| Docker Engine | NA | <a href="https://docs.docker.com/engine/"> Docker </a>|

You need to install all the dependencies available in requirements.txt

# Steps to build and run the app locally via Docker</br>

There are two ways to deploy the Web App on your local machine:
</br>
<b> 1. Deployment with Streamlit: </b>
</br>
</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. To deploy the app on your local machine through Streamlit, we just need to run the python file

```
>>> streamlit run webapp.py
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. This will deploy your webapp on your local machine. Post successful deployment of the code
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://10.0.0.244:8501

```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. You can access the web app through chrome, edge or any web browser and start sending requests to the REST API through the portal.

<b> 2. Deployment through Docker: </b>

- To deploy the app on your local machine through docker, we need a docker file ,given we already have the application file created, that would be the recipe for docker to build the application
- In the dockerfile, we will add the required dependency of python:3.7-slim
- Once the dockerfile is created, we'll execute the deployment of the docker container which would be published and deployed
- We'll copy the webapp.py in the app folder and the application would run once the docker image was deployed

*Sample Dockerfile*
````
FROM python:3.7-slim

EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install requests streamlit

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "webapp.py"]
````
*Building the Docker Image in the Active Directory/Folder*
```
sudo docker build -t <image-name> .
```

*Running the Docker Image - with ports defined for communication between local machine and docker image*
```
sudo docker run -it -p 8501:8501 <image-name> /app/<aap-name>.py
