<<<<<<< HEAD
# Health-Metrics
=======
Project Description: Health Metrics and Medical Data Management

This project aims to provide a comprehensive solution for managing health metrics and medical data using FastAPI, SQLite, and SQLAlchemy. The system consists of two main components: Health Metrics and Medical Data.

Health Metrics Component

The Health Metrics component allows users to track and visualize various health metrics over time. It includes the following features:

Dashboard Visualization:

The main dashboard displays trends for weight, blood pressure, and heart rate over time.

Each metric is presented in a separate plot for easy analysis.

Data Entry:

Users can enter their health metrics, including weight, blood pressure, and heart rate.

The entered data is stored in an SQLite database for historical tracking.

Data Deletion:

Users have the option to delete specific health records, providing flexibility in managing their data.

Medical Data Component

The Medical Data component focuses on managing comprehensive medical records for individuals. Key features include:

Data CRUD Operations:

●	Create, Read, Update, and Delete operations are supported for individual medical records.
●	Users can add, view, update, and delete detailed medical information, including name, age, address, national ID, diagnosis, treatment, allergies, immunizations, and family history.

Interactive Web Interface:

●	The system provides an interactive web interface for users to view and manage medical records.
●	The interface allows users to easily navigate and perform actions such as adding new records or deleting existing ones.

Cross-Origin Resource Sharing (CORS):
 
●	CORS middleware is implemented to enable communication between the FastAPI backend and potential frontend applications.

Technologies Used:

●	FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
●	SQLite: A lightweight, file-based relational database for storing health metrics and medical data.
●	SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library for interacting with the SQLite database.

Project Structure:

The project is organized into two main parts, each addressing specific health-related data management needs. The code includes the definition of database models, API routes for CRUD operations, and web templates for rendering the user interface.

How to Run:

1.	Ensure you have the necessary dependencies installed.

2.	Run the FastAPI application.

3.	Access the web interface through the specified URL (e.g., http://localhost:8000).



This project provides a foundation for a versatile health data management system, allowing users to monitor and maintain their health metrics and comprehensive medical records. Future enhancements may include additional features, improved visualizations, and integration with external systems.
>>>>>>> 1ecf4728 (Transferring to git)
