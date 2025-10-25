**1.1	Introduction **
      In recent years, artificial intelligence (AI) has revolutionized the way humans interact with technology. Chatbots have become an integral part of communication systems in websites, applications, and business platforms. They assist users by providing instant responses, saving human effort, and improving accessibility.
This project, PersonalBot, is designed to serve as a personalized virtual assistant capable of real-time communication. It integrates FastAPI (Python) as the backend framework and React.js as the frontend interface. Using OpenAI’s GPT model, it provides intelligent, natural language conversations with users.



**1.2 Objective**
The main objectives of this project are:
•	To design and develop an interactive chatbot capable of understanding and responding to user queries.
•	To integrate a reliable backend (FastAPI) that handles API requests and manages communication with OpenAI’s API.
•	To create a modern, responsive user interface using React.js for real-time message exchange.
•	To demonstrate seamless integration between frontend and backend technologies.





**1.3 Project Description**
PersonalChat Bot is a full-stack web application that allows users to have natural conversations with an AI assistant.
The backend, built with FastAPI, processes user messages and interacts with OpenAI’s GPT model. The frontend, built in React.js, displays a chat interface similar to modern messaging apps. The project ensures efficient data flow between user and AI, providing a smooth, real-time chatting experience.




**Chapter 2:  Related Work**
2.1 Related Work
Recent developments in natural language processing (NLP) have introduced advanced AI chatbots like:
•	Google Assistant, Alexa, and ChatGPT, which use deep learning models for human-like responses.
PersonalBot builds upon these modern concepts using OpenAI’s GPT model while focusing on a lightweight, deployable web-based solution using FastAPI and React.js.








**Chapter 3: Requirement Analysis and System Specification**
3.1 Requirement Analysis
Hardware Requirements
•	Any Device Run After Deployment But 
•	For Instant Run We Need Of Laptop
•	Internet connection for API communication

**Software Requirements**
•	Backend: Python 3.10+, FastAPI
•	Frontend: React.js, Node.js
•	Tools: Visual Studio Code,  Uvicorn, npm
•	APIs: OpenAI GPT API 
•	Server Reload Need: uvicorn server:app --reload
3.2 System Specification
•	Operating System: Windows 10 / 11
•	Programming Languages: Python (backend), Javascript(frontend)
•	Frameworks: FastAPI, React.js







**Chapter 4: System Design**
4.1 System Architecture
The architecture consists of:
•	Frontend Layer: React.js handles the UI and communicates with the backend via REST API requests.
•	Backend Layer: FastAPI processes input messages, sends them to OpenAI, and returns the response.
•	External API Layer: OpenAI’s GPT model generates human-like responses.


**4.2 Workflow**
1.	User types a message in the React chat UI.
2.	The frontend sends the message to FastAPI via an HTTP POST request.
3.	FastAPI forwards the message to the OpenAI API.
4.	OpenAI generates a response and returns it to FastAPI.
5.	FastAPI sends the reply back to the React app, which displays it instantly.
6.	<img width="961" height="437" alt="image" src="https://github.com/user-attachments/assets/da5134a4-65be-48b7-86b6-3e6bfb657dd1" />

7.	

**4.3 Module Description**
•	Frontend Module: Displays chat messages, input box, and send button.
•	Backend Module: Handles message routing and OpenAI communication.
•	AI Module: Uses GPT-based reasoning to create responses.
•	Integration Module: Connects frontend and backend seamlessly using REST API calls.


**
Chapter 5: Implementation Modules**
**5.1 Introduction to Programming Languages**
•	Python: Used for backend development due to its simplicity and FastAPI support.
•	JavaScript (React.js): Used for frontend to create a dynamic, responsive user interface.
5.2 Tools and Technologies
•	FastAPI: Lightweight and high-performance web framework for Python.
•	React.js: Frontend library for building user interfaces.
•	Uvicorn: ASGI server used to run the FastAPI backend.
•	OpenAI API: Provides intelligent conversational responses.


**Step 1: Create a Python backend**
Install dependencies: 
Run In Terminal;-     

                   python -m pip install fastapi uvicorn openai

Then Run For Server Load In the Terminal-:
                                                        uvicorn server:app --reload


Step 2: Create a React frontend
        create a React app:
     Run Terminal :-                
                      
                      1.  npx create-react-app frontend
                                                     2.  cd frontend
                                                     3.    npm start


**ScreenShot Of The Output: **
<img width="635" height="823" alt="image" src="https://github.com/user-attachments/assets/266f31f8-4846-4999-a73a-0e803f588fe5" />
<img width="561" height="777" alt="image" src="https://github.com/user-attachments/assets/da956ebc-a341-422d-9b6e-312b126f55c5" />
<img width="751" height="772" alt="image" src="https://github.com/user-attachments/assets/6bbe5145-c4c3-4e57-b971-f951deee960b" />




                   
