# BenefitShield

BenefitShield is a Flask-based financial benefit discovery and scam awareness web application. It helps users find relevant government benefits and financial support schemes based on their basic details, understand eligibility requirements, prepare required documents, and identify common signs of financial scams.

## Features

- Home page for the BenefitShield platform overview
- User profile section for entering basic details
- Financial benefit and government scheme discovery
- Eligibility matching based on user information
- Scheme details including benefits and eligibility requirements
- Required document checklist for selected schemes
- Information about application requirements and deadlines
- Official source information for schemes
- Scam Shield for checking suspicious financial messages
- Warning signs for OTP, PIN, password, suspicious links, and fake offers
- Reminder and guidance section for important actions
- SQLite database support through Flask-SQLAlchemy
- Simple and user-friendly web interface

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite

## Project Structure

```text
BenefitShield/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── schemes.html
│   ├── checklist.html
│   ├── document.html
│   ├── fraud.html
│   └── tracker.html
│
└── uploads/
````

## Main Modules

### 1. User Profile

Users can provide basic information such as:

* Location
* Education
* Income range
* Area of interest

This information is used to identify potentially suitable benefits and schemes.

### 2. Benefit Discovery

BenefitShield helps users discover relevant government benefits and financial support schemes.

The system provides information such as:

* Scheme name
* Eligibility
* Benefits
* Required documents
* Application details
* Deadline
* Official source

### 3. Eligibility Matching

The system compares the user's basic details with the eligibility requirements of available schemes and displays potentially relevant opportunities.

### 4. Scam Shield

The Scam Shield module helps users identify possible financial scams.

It checks for common warning signs such as:

* Requests for OTP or PIN
* Requests for passwords or bank details
* Suspicious links
* Urgent payment requests
* Fake scholarship or loan offers
* Unknown sender information
* Requests for advance fees

The feature provides safety guidance and encourages users to verify information through official sources.

### 5. Document Checklist

Users can view the documents that may be required for applying to a selected scheme.

This helps users prepare the required documents before starting the application process.

### 6. Reminder and Guidance

The platform provides guidance related to:

* Application deadlines
* Required documents
* Important actions
* Official verification
* Scheme application steps

## Database

BenefitShield uses SQLite for storing application-related information.

Flask-SQLAlchemy is used to connect the Flask application with the database.

The database can store information related to:

* User details
* Government schemes
* Eligibility information
* Required documents
* Scam reports
* Application tracking information

## Setup

1. Clone the repository.

2. Open the project folder in VS Code.

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment.

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python app.py
```

7. Open the local URL shown in the terminal.

For example:

```text
http://127.0.0.1:5000/
```

## Notes

* The application is developed as a prototype for financial benefit discovery and scam awareness.
* Users should verify scheme information through the respective official government source before applying.
* The system does not guarantee eligibility or approval for any financial benefit.
* Sensitive information such as OTPs, PINs, passwords, and bank credentials should not be entered into the application.
* SQLite is used as the database for the prototype.
* Uploaded files, if used, are stored locally in the project environment.

## Git Commands

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/BenefitShield.git
git push -u origin main
```

## Purpose

BenefitShield is designed to make financial benefit information easier to discover and understand while helping users recognize common digital financial scams.

The project focuses on:

* Benefit discovery
* Eligibility matching
* Document guidance
* Application reminders
* Financial scam awareness
* Simple and accessible information

```

### Your GitHub README will look like the sample

The order is:

**BenefitShield → Description → Features → Tech Stack → Project Structure → Main Modules → Database → Setup → Notes → Git Commands → Purpose**

This matches the structure of the **VipherAid README** you showed, but the content is specific to **BenefitShield**.
```
