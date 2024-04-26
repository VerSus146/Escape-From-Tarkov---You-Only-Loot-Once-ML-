from ultralytics import YOLO


class Train:

	def __init__(self, model_name, dataset="Data/Dataset/data.yaml"):
		self.model_name = model_name
		self.dataset = dataset

	def train(self):
		# Load a model
		model = YOLO('yolov8n.pt')

		model.train(data=self.dataset, epochs=100, imgsz=640, device="cuda", workers=4)

		model.save(self.model_name)
