# About Web App </br>

This web applicatoon has been designed to hep users fetch answers to questions using numnerous NLP models . Users willl be able to view the list ov aviailbale models , add new models , delete existing models , ask a question and upload a CSV with bulk questions </br></br>

# Web App URL </br>
https://mgmt-qna-portal-yu4izdrwlq-uc.a.run.app

# How to use this web app </br>

To use this app : Click on the above URL

# System Architecture</br>

## You should be able to see below layout :

## Home Page:</br>
This is the landing page of the web app and you will be able to read the instructions on how to navigate through various features </br>

![image](https://user-images.githubusercontent.com/74998715/120737738-9ead8600-c4bc-11eb-8067-6dcffcac707e.png)

## List Models </br>
Returns the list of existing models in the system </br>

![image](https://user-images.githubusercontent.com/74998715/120737783-b71da080-c4bc-11eb-8505-19d9646a0578.png)

## Add a model </br>
Let's you add a new model and will return a list of existing models </br>

![image](https://user-images.githubusercontent.com/74998715/120737826-c4d32600-c4bc-11eb-8575-e91a7f4c9ea9.png)

## Delete a model</br>
Let's you delete an existing model and will return the list of remaining models </br>

![image](https://user-images.githubusercontent.com/74998715/120737847-d3b9d880-c4bc-11eb-96a3-1300d8b45579.png)

## Ask a question</br>
Use this to post your questions along with context . You may select a model as well </br>

![image](https://user-images.githubusercontent.com/74998715/120737882-e2a08b00-c4bc-11eb-8360-38aa8b05a68d.png)

## Upload Questions</br>
Use this to bulk upload your questions using a CSV </br>

![image](https://user-images.githubusercontent.com/74998715/120737916-ef24e380-c4bc-11eb-9db8-e5cec26705e2.png)

Sample CSV</br>

![image](https://user-images.githubusercontent.com/74998715/120737973-08c62b00-c4bd-11eb-9af0-d7dd0bff9bfc.png)

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
