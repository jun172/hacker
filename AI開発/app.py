from flask import Flask, render_template, Response
import cv2 
import torch
from torchvision import models, transforms

app = Flask(__name__)

#モデル読み込み
model = models.resnet18(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224,224)),
    transforms.ToTensor(),
])

cap = cv2.VideoCapture(0)

def genetare_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        #AI処理
        img = transform(frame).unsqueeze(0)
        with torch.no_grad():
            outputs = model(img)
        _, pred = torch.max(outputs,1)
        
        #結果描画
        cv2.putText(frame, f"ID:{pred.item()}",(10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        
        #JPEG変換
        ret, buffer = cv2.imencode(',jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(genetare_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)