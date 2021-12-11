from fastapi import FastAPI, File, UploadFile
import os


app = FastAPI()



@app.post("/uploadFile")
async def upload_file(file: UploadFile = File(...)):
    ext = file.filename.split(".")[1]
    name = file.filename
    
    if(ext =="evtx"): 

        path = os.path.join("Logs", name)          
        file_to_save = open(path, "wb")
        content = await file.read()
        file_to_save.write(content)
        file_to_save.close()
    elif(ext =="pcapng"): 
        path = os.path.join("Captures", name)          
        file_to_save = open(path, "wb")
        content = await file.read()
        file_to_save.write(content)
        file_to_save.close()
    return {f"file {file.filename} uploaded successfully"}