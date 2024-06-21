**PyFormExpress**

**Description**

PyFormExpress is a Windows Desktop Application that replicates the functionality of Google Forms. It allows users to create new form submissions and view existing submissions. The application includes features for creating, viewing, editing, and deleting submissions, with keyboard shortcuts for improved usability.

**Features**


![Screenshot (998)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/b6683ae0-bf93-470a-a69b-e0f3e3fef7fa)


**Create New Submission:**

-Fields for Name, Email, Phone Number, and GitHub repo link.

-A button to start/pause a stopwatch.

-Submit button to save the form details.

-Keyboard Shortcuts:

    Start/Pause Stopwatch: Ctrl+T
    
    Submit: Ctrl+S


![Screenshot (999)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/9648a913-aba6-4659-b8bf-2408332ca93c)


**View Submissions:**

  -Buttons to navigate through submissions (Previous, Next).
  
  -Buttons to edit or delete submissions.
  
  -Keyboard Shortcuts:
  
      View Previous Submission: Ctrl+P
      
      View Next Submission: Ctrl+N
      
      Edit Submission: Ctrl+E
      
      Delete Submission: Delete
      
      Update Submission: Ctrl+S (in Edit mode)
      
Submissions with stopwatch time 00:00:00 are saved but not displayed in the view submissions window.


![Screenshot (1000)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/217ea6b3-bf28-46de-a9f2-462707d75203)




![Screenshot (1001)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/122fccfa-0cdf-4a88-9a80-c4f552eea3e8)


**FrontEnd Setup**

1)Clone the repository:

 git clone <your-frontend-repo-url>

2)Install dependencies and reuiremnt.txt:

pip install tkinter

3)crete python environment

4)Run the application:

python main.py


![Screenshot (1002)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/83452fae-f6a3-4faa-883b-c000b08d0ac6)


**Backend Setup**

1)Clone the repository:

git clone <your-backend-repo-url>

cd backend

2)Install dependencies:

npm install

3)Run the server:

npm start


![Screenshot (997)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/557ce7a2-1d91-4dc9-9852-e22e9e78d885)


**Backend Endpoints**

***/ping:***

Method: GET

URL: http://localhost:3000/ping

Response: { "success": true }


![Screenshot (1004)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/2ed9115a-fa6c-4de8-91c1-b45f2ec9ac03)


***/submit:***

Method: POST

URL: http://localhost:3000/submit

Body: JSON

{
    "name": "John Doe",
    
    "email": "john.doe@example.com",
    
    "phone": "1234567890",
    
    "github_link": "https://github.com/johndoe",
    
    "stopwatch_time": "00:05:23"
}


![Screenshot (1006)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/7d2a1afa-fe64-4e96-ac66-7843613ab7c3)


***/read_all:***

Method: GET

URL: http://localhost:3000/read_all

Response:


![Screenshot (1005)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/82321e61-5c72-488a-8ac8-09761a7c5e9f)


***/submit (Update):***

Method: PUT

URL: http://localhost:3000/submit

Body: JSON

{
    "id": 1,
    
    "name": "John Doe",
    
    "email": "john.doe@example.com",
    
    "phone": "1234567890",
    
    "github_link": "https://github.com/johndoe",
    
    "stopwatch_time": "00:05:23"
}


![Screenshot (1007)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/9b9ffa69-ed71-4971-b64e-8249b67f32d7)




![Screenshot (1008)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/46faf111-6030-4724-8690-47fba785a2b6)


***/delete:***

Method: DELETE

URL: http://localhost:3000/delete?id=1

Response: Submission deleted successfully


![Screenshot (1009)](https://github.com/Samrudhi00/PyFormExpress/assets/89694069/2dcc1e0c-d522-4bbb-a5a8-9321770b43ef)


**Notes**

The db.json file is used as a database to store submissions.

Ensure the backend server is running before starting the frontend application.









