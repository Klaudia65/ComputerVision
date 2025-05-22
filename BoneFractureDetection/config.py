from roboflow import Roboflow

rf = Roboflow(api_key="j4nlaq31Emxo9hm16bV7")  # récupère ta clé sur Roboflow
project = rf.workspace("ahmedali-aqmwq").project("break-bone")
dataset = project.version(3).download("yolov8")
