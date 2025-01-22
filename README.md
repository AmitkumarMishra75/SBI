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

# **IMAGES**

![Image](https://github.com/user-attachments/assets/64793e95-d0a9-410b-a062-8cbee94b687d)
![Image](https://github.com/user-attachments/assets/2590df3c-833b-458b-8393-1bed6ee89e39)
![Image](https://github.com/user-attachments/assets/2014a76e-8832-4ff0-a13a-fd4702adbc90)
![Image](https://github.com/user-attachments/assets/e49a1c91-e804-4d6b-af4b-964e0c44906a)
![Image](https://github.com/user-attachments/assets/205eb07c-108e-4f61-aa22-592fdda23222)
![Image](https://github.com/user-attachments/assets/b0ec1c60-8a51-439e-8ff3-25dade284698)
![Image](https://github.com/user-attachments/assets/3e86f830-a0bc-42d9-9937-2009c13210b4)
![Image](https://github.com/user-attachments/assets/f1c2cd40-732a-4748-bbf2-633ddd65295f)
![Image](https://github.com/user-attachments/assets/7d1742ea-5f60-4936-b3fb-e5ec9d6d94c1)
