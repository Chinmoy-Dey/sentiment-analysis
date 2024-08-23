# sentiment-analysis
This model can be used for topic classification. Example finding out the sentiment of a text whther it is posivive or negative

# how to set up 
```
    1. create Docker hub A/c
    2. Create Secret
    3. Add secret to guthum project setting DOCKER_USERNAME, DOCKER_PASSWD
```

# How to build
```
$ cd sentiment_analysis_project/
$ pip install --upgrade build
$ python3 -m build

```

# How to build Docker image 
```
$ sudo apt install docker.io
$ sudo dockerd &
 
$ docker build -t <yourImageName> -f <yourDockerfileName> .
 or 
$ docker build .
 or 
$ docker build ./sentiment_analysis_project/ --file ./sentiment_analysis_project/Dockerfile --tag my-image-name:$(date +%s) 

```

# How to run 
```
 $ cd sentiment_analysis_project/sentiment_analysis_model_api/app/
 $ uvicorn main:app --reload

 http://127.0.0.1:8000

 http://127.0.0.1:8000/docs#/default/analyze_sentiment_api_v1_analyze_sentiment__post

```