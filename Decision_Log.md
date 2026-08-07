Decision Log
Skylark Drones Dashboard – Decision Log
1. Project Overview
The objective of this project was to develop a Business Intelligence Dashboard that connects with the Monday.com platform using its GraphQL API. The dashboard retrieves live data from the Deals Board and Work Orders Board and displays it in a clean and user-friendly web interface. The application helps users monitor business information from Monday.com in real time.
________________________________________
2. Technology Decisions
Backend
Technology: Flask (Python)
Reason:
•	Flask is lightweight and easy to configure. 
•	It integrates well with REST and GraphQL APIs. 
•	It supports server-side rendering using Jinja2 templates. 
•	It is suitable for small to medium-sized dashboard applications. 
________________________________________
Frontend
Technology: HTML, CSS and Jinja2 Templates
Reason:
•	HTML and CSS provide a simple and responsive interface. 
•	Jinja2 allows dynamic rendering of data received from the backend. 
•	No JavaScript framework was required for the current project scope. 
________________________________________
API Integration
Technology: Monday.com GraphQL API
Reason:
•	GraphQL allows requesting only the required fields. 
•	It reduces unnecessary network traffic. 
•	It provides flexible querying for board items and column values. 
________________________________________
Environment Variables
Technology: .env file with python-dotenv
Reason:
•	Keeps API credentials secure. 
•	Prevents sensitive information from being uploaded to GitHub. 
•	Makes deployment easier by using environment variables on Render. 
________________________________________
3. Assumptions
The following assumptions were made during development:
•	Monday.com boards contain valid business data. 
•	API authentication token remains valid. 
•	Board IDs do not change. 
•	Missing values are displayed as blank or "None". 
•	Internet connectivity is available while using the application. 
________________________________________
4. Trade-offs
Due to the project timeline, the following decisions were made:
•	Used server-side rendering instead of React. 
•	Focused on displaying business information rather than advanced analytics. 
•	Implemented a clean dashboard without complex charts. 
•	Prioritized stability and API integration over additional features. 
________________________________________
5. Challenges Faced
The following issues were encountered and resolved:
•	Python installation and PATH configuration. 
•	Git installation and GitHub authentication. 
•	Monday.com API authentication. 
•	Parsing nested GraphQL responses. 
•	Deploying the Flask application on Render. 
•	Managing environment variables securely. 
________________________________________
6. Leadership Dashboard Interpretation
The dashboard provides leadership with a centralized view of business operations by displaying:
•	Current Deals 
•	Work Orders 
•	Status 
•	Priority 
•	Assigned Owners 
•	Company Information 
•	Cost and Due Dates 
This enables quick monitoring of business activities and operational progress.
________________________________________
7. Future Improvements
The application can be enhanced by adding:
•	AI-powered chatbot for business queries 
•	Interactive charts and graphs 
•	Search and filtering options 
•	Export to Excel and PDF 
•	User authentication and role-based access 
•	Real-time updates using WebSockets 
•	Advanced analytics and KPI dashboards 
________________________________________
8. Conclusion
The Skylark Drones Dashboard successfully integrates with Monday.com using GraphQL APIs to retrieve live business data and present it through a responsive Flask web application. The project demonstrates API integration, backend development, frontend rendering, secure deployment practices, and cloud hosting using Render.

Project Title: Skylark Drones Dashboard
Student Name: Akanksha H A
Date: 07-08-2026

