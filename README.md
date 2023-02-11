# Prepaid-Recharge-API
Using Python/Django Framework
Prepaid-Recharge-API

Admin user :- admin12 , Admin password :- 2211

At first clone this project- Install this module :- pip install virtualenv Then create virtualenv in which directory your project is cloned usig this command :- virtualenv env_name Then activate your virtual env after your dir :- .\env_name\Scripts\activate. Then go to project folder and run this command :- pip install -r requirements.txt.

Then run this command to run the project :- python manage.py runserver

Then....

GET http://127.0.0.1:8000/api/get-plans/ responsible for get the all available palns with get method with a valid token because this is protected endpoint. 
POST http://127.0.0.1:8000/api/do-recharge/ responsible for do recharge as your given mobile number,valid operator, valid area/circle, valid plan with valid user token.

mobile -> valid 10 digit of mobile no.

valid operator -> Airtel Prepaid,Jio Prepaid, BSNL Prepaid, VI Prepaid, MTNL Prepaid same as it is formate.

valid area/circle -> Andhra Pradesh ,Assam ,Bihar Jharkhand ,Chennai ,Delhi NCR, Goa, Gujrat ,Haryana ,Himanchal Pradesh , Jammu Kashmir ,Karnataka ,Kerala ,Kolkata ,Madhya Pradesh Chhattisgarh ,Maharashtra ,Mumbai ,North East ,Orissa ,Punjab , Rajasthan ,Tamilnadu ,Telangana ,UP East ,UP West & Uttarakhand ,West Bengal mention in model.

valid plan -> 359, 719, 299, 479, 2999, 181, 301, 75, 152, 122, 86, 182, 26, 62, 555, 241, 19 plans are indicate what is the price of your paln.

Thanks................
