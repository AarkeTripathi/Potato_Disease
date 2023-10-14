from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
# import matplotlib as mpl
# mpl.use('QtAgg')

app=FastAPI()

model=tf.keras.models.load_model(r'/home/aarke/Coding/potato_proj/saved_models/1')
class_names=['Early_Blight','Healthy','Late_Blight']

@app.get('/status')
async def status():
    return 'Server alive'

def read_file_as_image(data) -> np.ndarray:
    img=np.array(Image.open(BytesIO(data)))
    return img

@app.post('/predict')
async def predict(file: UploadFile=File(...)):
    img=read_file_as_image(await file.read())
    img_batch=np.expand_dims(img,0)
    # img_batch=np.array([img])
    prediction=model.predict(img_batch)
    prediction_class=class_names[np.argmax(prediction[0])]
    confidence=np.max(prediction[0])
    return {'class': prediction_class,'confidence': float(confidence)}

if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8000)