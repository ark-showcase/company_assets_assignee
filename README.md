# company_assets_assignee

API list

#  For company registration

http://127.0.0.1:8000/user/module/signup/

type: post

body:
{
    "username": "username_value",
    "password": "password_value",
    "email": "email_value",
    "company_name": "company_name_value"
}



#  For company login

http://127.0.0.1:8000/user/module/login/

type: post

body:
{
    "username": "username_value",
    "password": "password_value"
}



#  For company logout

http://127.0.0.1:8000/user/module/logout/

type: get



#  For add company employee

http://127.0.0.1:8000/operation/module/assign_employee/

type: post

body:
{
    "employee_name": "employee_name_value",
    "employee_department": "employee_department_value",
    "employee_cell_no": "employee_cell_no_value",
    "employee_email": "employee_email_value"
}



#  For add company asset

http://127.0.0.1:8000/operation/module/assign_asset/

type: post

body:
{
    "asset_category": "asset_category_value",
    "asset_name": "asset_name_value",
    "asset_brand": "asset_brand_value",
    "asset_model": "asset_model_value"
}



#  For assign an asset to an employee

http://127.0.0.1:8000/operation/module/assign_employee_asset/

type: post

body:
{
    "company_employee_id": "company_employee_id_value",
    "company_asset_id": "company_asset_id_value",
    "assigned_date": "asset_brand_value"
}

here assigned_date is optional, if you dont give the assigned_date then it will be set to todays date.



#  For return an asset from an employee

http://127.0.0.1:8000/operation/module/assign_employee_asset/return/{company_asset_id}/

eg: http://127.0.0.1:8000/operation/module/assign_employee_asset/return/AMIPROLIM3-3/

type: get



#  For view assets

http://127.0.0.1:8000/operation/module/view_asset/

type: get