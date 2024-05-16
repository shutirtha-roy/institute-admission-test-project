# Running the Frontend Application

To run the frontend application, follow these steps:

1. **Install Node.js:**  
   Download and install Node.js from [here](https://nodejs.org/en/download).

2. **Install Angular CLI:**  
   Open the Command Prompt and run the command to install the Angular CLI: 
npm install -g @angular/cli


3. **Navigate to the Frontend Angular App Directory:**  
   Go to the folder InstatuteApp which is the Frontend Angular App, then open the command prompt and locate the folder.
Example: If the Frontend Angular App is in the in the location: 
If the location is in the D drive, then type “D:” in the terminal then press Enter and then paste the absolute path like for example “cd D:\Development\Repo\Frontend\tip-project-instatute\src\frontend\InstatuteApp” then press Enter. 

4. **Install Dependencies:**  
 Then type the command “npm install -f” to install the packages from the “package.json” file.

5. **Start the Angular Application:**  
After its install, type the command “ng serve” to start the Angular application with the URL “http://localhost:4200/”.


### Steps on Running the Backend Application

1. **Install Python 3.10**: 
   - Download Python 3.10 from [here](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe).
   - Follow the installation instructions.

2. **Install MongoDB Community Server**: 
   - Download MongoDB Community Server from [here](https://www.mongodb.com/try/download/community).
   - Follow the installation instructions.

3. **Navigate to Backend Folder**: 
   - Open the command prompt.
   - Navigate to the backend folder where the application is located. 
   - Example:
     ```
     D:
     cd D:\Development\Repo\Backend\tip-project-instatute\src\backend
     ```

4. **Install Required Packages**: 
   - Once inside the backend folder, install all the required Python packages listed in the "requirements.txt" file.
   - Run:
     ```
     pip install -r requirements.txt
     ```

5. **Start the Python Application**: 
   - After installing the required packages, start the Python application.
   - Run:
     ```
     python run.py
     ```
   - Access the backend server via [http://localhost:8000/](http://localhost:8000/).

6. **Database Connection**: 
   - The application should automatically connect to the MongoDB server using the database named "instatuteDB". 
   - Ensure that MongoDB is running and accessible on the default port (27017) for this connection to succeed.
