# Resize image 

## 1. Cloning the repository
```
git clone https://github.com/fabianMM04/resize_image_backend.git
```
## 2. go to the project and build with docker-compose
```
cd resize_image_backend/images_resize/
docker-compose build
```
## 4. Run project with docker-compose
```
docker-compose up -d
```
## 4. API resize images
```
* POST: ec2-3-84-252-199.compute-1.amazonaws.com:8000/savefile
  Query Params: files
  Body (form data): 
  files : path/to/file/image1.jpg
Response:{
    "message": [{"name": file_name, "orientation": image_orientation}]
}
```
