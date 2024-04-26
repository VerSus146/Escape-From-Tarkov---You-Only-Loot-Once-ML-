from Code.training import Train
from Code.argparser import Parser

if __name__ == '__main__':

	Parser = Parser()

	mode = Parser.Parse_arguments()

	if "training" in mode["mode"]:
		print("Training Mode")

		if mode["dataset"] is None:
			Train = Train(model_name=mode["name"])
		else:
			Train = Train(model_name=mode["name"], dataset=mode["dataset"])
			Train.train()

	if "detection" in mode["mode"]:
		print("Detection Mode")
