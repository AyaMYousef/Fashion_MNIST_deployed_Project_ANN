import tensorflow as tf
from dotenv import load_dotenv
import os


load_dotenv(override=True)

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY= os.getenv("API_SECRET_KEY")


#Source Folder

SRC_PATH_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Load Model

MODEL = tf.keras.models.load_model(os.path.join(SRC_PATH_FOLDER,"artifacts", "model.keras"))

#Class_Names


CLASS_NAMES = ['T_Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle_Boot']