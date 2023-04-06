# Generating video subtitles: Unlocking the power of Openai-Whisper 

#### Language and Libraries

<p>
<a><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="python"/></a>
<a><img src="https://img.shields.io/badge/openai-181818?style=for-the-badge&logo=openai&logoColor=white" alt="numpy"/></a>
<a><img src="https://img.shields.io/badge/whisper-181818?style=for-the-badge&logo=openai&logoColor=green" alt="opencv"/></a>
<a><img src="https://img.shields.io/badge/Django-%23EE4C2C.svg?style=for-the-badge&logo=Django&logoColor=white" alt="pytorch"/></a>
</p>

## Problem statement
The goal of this project is to develop a web application that allows user to upload a video and automatically transcribe or translate any video to **English substitle SRT FILE** ,gives downloaded file Automatically to the user.The application is built using Django framework.The project aim to give user the srt file directly without any huddle to search the file on the internet

## Solution
The proposed solution for this project utilized `Openai-Whisper` model to transribe or translate audio of the video into subtitle file.The application is built using Django framework.

Create Environment
```
conda create --name subtitles python==3.9 -y

```


Activate Environment
```
conda activate subtitles

```

install requirements file

```
pip install -r requirements.txt

```


## To run the project and get the srt file automatically 
#### follow this command 
```
cd subtitle
python manage.py runserver

```

👨‍💻 Tech Stack Used
1. Python
2. Django


## Conclusion
This application could be used in a wide range of real-world scenarios, such as in the entertainment industry for **subtitle generation**. We often feel frustrated to find the subtitle file , this could help user to get the **Subtitle srt file** with no time . Accuracy of the model could be increased by switching on to different models.