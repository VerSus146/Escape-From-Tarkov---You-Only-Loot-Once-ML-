import os

from ultralytics import YOLO
from trame.app import get_server
from trame.widgets import vuetify
from trame_vuetify.ui.vuetify import SinglePageWithDrawerLayout
from trame.assets.local import to_url


class Detection:
	def __init__(self, port, model):
		self.server = get_server(client_type="vue2", name="EFTYoloApp")
		self.model = YOLO("D:\\PycharmProjects\\Escape-From-Tarkov---You-Only-Loot-Once-ML-\\EFT-YOLO-V1.pt")
		self.predict_items()
		self.prepare_view()

		self.server.start(port=port)

	def prepare_view(self):

		with SinglePageWithDrawerLayout(self.server) as layout:
			layout.title.set_text("EFT You Only Loot Once")
			layout.icon.hide()
			layout.footer.hide()

			with layout.toolbar:
				pass

			with layout.footer:
				pass

			with layout.content:
				vuetify.VImg(src=to_url(os.path.abspath(os.curdir) + "\\Code\\Detection\\Predicted.jpg"))

	def predict_items(self):
		result = self.model(os.path.abspath(os.curdir) + "\\Code\\Detection\\Current.jpg")

		save_path = os.path.abspath(os.curdir) + "\\Code\\Detection\\Predicted.jpg"

		result[0].save(save_path)
		#TODO: Collect bounding boxes and display them on an image in custom way, so the user can hover and check the
		#price on the market
