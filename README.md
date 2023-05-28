# CSV-Data-Import
This is a Django project that provides an API to upload a CSV file with employee data and populate the database with the contents of the file.

This feature allows users to save valuable time by uploading CSV files to populate the database. Instead of manually entering records one by one, users can now conveniently upload a CSV file containing library management or employee data. This not only expedites the data input process but also minimizes the chances of errors that may occur during manual entry. By ensuring proper formatting and validation of the CSV file, including column headers, data formatting, and necessary transformations, the system ensures accurate and efficient population of the database. With CSV uploads, you can streamline your data entry process and enhance overall productivity

API Endpoints

Upload Employee Data

 ```
http://127.0.0.1:8000/employee/api/upload/
 ```
Method: POST

Description: Upload a CSV file with employee data to populate the database.

Request Body: The request body should include a file field containing the CSV file.

Get Employee List
 ```
 http://127.0.0.1:8000/employee/data/
 ```

Method: GET
