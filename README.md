# Package a Python Script into a Command-Line Tool

![CI](https://github.com/nogibjj/ids706-mini-project-7/actions/workflows/main.yml/badge.svg)

This is a Python command-line tool that connects to a MySQL database, creates tables, and inserts sample data. 

## Prerequisites

Before running this project, make sure you have the following:

* A MySQL database instance accessible from your Python environment.
* Python (versions 3.7, 3.8, 3.9) installed on your machine.

## Getting Started

Follow these steps to set up and run the project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nogibjj/ids706-mini-project-7.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ids706-mini-project-7
   ```
   
3. Configure environment variables by creating a .env file in the project directory with the following content:

   ```bash
   DB_HOST='your_host'
   DB_NAME='your_db_name'
   DB_USER='your_username'
   DB_PASSWORD='your_password'
   ```

Note: These environment variables are crucial for the application to connect to the right MySQL instance. Make sure they match your database configurations.

4. Install the Tool - With the project directory as your current directory, run:

   ```bash
   pip install .
   ```

6. Once installed, you can use the tool by running:

   ```bash
   my_tool
   ```

## Testing

To run the tests for this project, first ensure you have pytest installed:


   ```bash
   pip install pytest
   ```

Then, in the project directory, simply run:

   ```bash
   pytest
   ```

## Contributing

If you find any bugs or have suggestions for improvements, please create an issue or a pull request in the repository.



