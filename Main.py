import torch
from ultralytics import YOLO

if __name__ == '__main__':
	# Load a model
	model = YOLO('yolov8n.pt') # load a pretrained model (recommended for training)

	results = model.train(data="Data/Dataset/data.yaml", epochs=100, imgsz=640, device="cuda", workers=4)

	model.save("EFT-YOLO-V1.pt")