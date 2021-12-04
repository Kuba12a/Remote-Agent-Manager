from fastapi import FastAPI, File, UploadFile


app = FastAPI()



@app.post("/uploadFile")
async def upload_file(file: UploadFile = File(...)):
    print(file.filename)
    file_to_save = open(file.filename, "wb")
    file_to_save.write(await file.read())
    file_to_save.close()
    return {f"file {file.filename} uploaded successfully"}