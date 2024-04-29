import argparse
import os
from pathlib import Path


class Parser:

	def __init__(self):
		self.parser = argparse.ArgumentParser(prog='EFT YOLO')
		self.parser.add_argument('--train', help='Train Mode', type=str, default="False")
		self.parser.add_argument('--model_name', help="Name of the trained model", type=str)
		self.parser.add_argument('--dataset', help='Dataset for TrainMode', type=str)

	def Parse_arguments(self):
		args = self.parser.parse_args()
		if "False" in args.train:
			return {"mode": "detection"}

		if args.dataset is None:
			print("Training enabled, but dataset not provided. Closing.")
			exit(1)

		if args.model_name is None:
			print("Using default name: EFT-YOLO")
			args.model_name = "EFTYOLO.pt"

		if os.path.isfile(Path(args.dataset)):
			return {"mode": "training", "dataset": args.dataset, "name": args.model_name}
		else:
			print("Wrong path to Dataset provided. Closing")
			exit(1)
