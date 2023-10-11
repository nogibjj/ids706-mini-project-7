# Package a Python Script into a Command-Line Tool

This is a Python command-line tool that connects to a MySQL database, creates tables, and inserts sample data.

## Prerequisites

Before running this project, make sure you have the following:

* A MySQL database instance accessible from your Python environment.
* Python installed on your machine.

## Getting Started

Follow these steps to set up and run the project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aghakishiyeva/ids706-mini-project-7.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ids706-mini-project-7
   ```
   
3. Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables by creating a .env file in the project directory with the following content:

   ```bash
   DB_HOST='your_host'
   DB_NAME='your_db_name'
   DB_USER='your_username'
   DB_PASSWORD='your_password'
   ```

5. Once installed, you can use the tool by running:

   ```bash
   my_tool
   ```
