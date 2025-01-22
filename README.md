# **🏦 Bank Management System**

A **Bank Management System** built using **Django** that enables users to open accounts, generate PINs, and perform essential banking operations like credit, debit, balance checks, and fund transfers.

---

## **🌟 Features**

- **Account Management**:  
  - Open a new bank account with default balance of ₹5000.  
  - Generate and set a secure PIN for transactions.  
  - View and manage account details securely.  

- **Banking Operations**:  
  - **Credit Money**: Deposit funds into your account.  
  - **Debit Money**: Withdraw funds securely with a valid PIN.  
  - **Transfer Money**: Seamlessly transfer funds:  
    - By Account Number.  
    - By Email Address.  
    - By Mobile Number.  
  - **Check Balance**: Retrieve current account balance details.  

- **Security Features**:  
  - Secure PIN generation and encryption.  
  - OTP-based PIN setup for enhanced security.  
  - Email notifications for account updates and transactions.  

---

## **💻 Tech Stack**
### **Frontend**
- HTML5  
- CSS3  

### **Backend**
- Python  
- Django Framework  

### **Database**
- SQLite (Default database with Django)  

---

## **📂 Project Structure**

|── bank_management/ # Main Django project │ <br>
├── settings.py # Project settings │ <br>
├── urls.py # URL routing <br>
│ └── wsgi.py # WSGI application <br>
├── app/ # Banking app │ <br>
├── migrations/ # Database migrations │ <br>
├── templates/ # HTML templates │ <br>
├── static/ # Static CSS and JS files │ <br>
├── models.py # Models for accounts and data │ <br>
├── views.py # Application logic (CRUD, transactions, etc.) │ <br>
└── urls.py # Application-specific routes <br>
└── manage.py # Django management script <br>

## **🚦 Application Flow**

### **Key Operations** (`views.py`):
1. **Home (`home`)**  
   Displays the homepage with navigation links.  

2. **Open Account (`open`)**  
   Create a new account with default balance and encrypted PIN storage.  

3. **Generate PIN (`pin`)**  
   Generate a one-time OTP to securely set your PIN.  

4. **Credit (`credit`)**  
   Deposit money into the account.  

5. **Debit (`debit`)**  
   Withdraw money with balance validation and PIN verification.  

6. **Transfer (`transfer`)**  
   Transfer funds to accounts using account numbers, emails, or mobile numbers.  

7. **Check Balance (`balance`)**  
   Retrieve the current balance of the account.  

8. **Account Details (`display`)**  
   View masked personal details securely.
