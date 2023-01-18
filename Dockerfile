FROM python:3.9.16-slim-bullseye

# Install linux packages
RUN apt update && apt install --no-install-recommends -y zip htop screen libgl1-mesa-glx
RUN apt -y install git
RUN apt -y install libglib2.0-0

# Install pip packages
RUN python -m pip install --upgrade pip
RUN pip uninstall -y torch torchvision torchtext Pillow
RUN pip install --no-cache -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt albumentations wandb gsutil notebook Pillow>=9.1.0 \
    torch torchvision

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN git clone https://github.com/ultralytics/yolov5/. /usr/src/app

# Add training model
RUN mkdir -p runs/train/exp/weights
COPY best.pt runs/train/exp/weights

# Set environment variables
ENV OMP_NUM_THREADS=8

ENTRYPOINT ["/bin/sh", "-c" , "python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.3 --source runs/detect"]
