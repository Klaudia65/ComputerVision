from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='./Break-bone-3/data.yaml', epochs=50, imgsz=640, device='cpu', batch=8)