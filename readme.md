# Beer advisor

This is a sourse for my pet project. Telegram bot that can recognize ±199 different beers and reply with based information.
Model Yolov5 was taken form *[Ultralytics](https://github.com/ultralytics/yolov5/)* and fine-tuned on 4k images

## Installation
Clone this repo and install dependencies and yolo dependencies.

```sh
git clone
pip install -r requirements.txt 
cd yolov5
pip install -r requirements.txt 
```
Create config.py in project root and add your bot token
```sh
echo "TOKEN = 'your token here'" > config.py
```
## Run bot

```sh
python bot.py
```


