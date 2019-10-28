# property_manager

Project was made using Database SQLlite, to save time.

New Owner can be added through admin page.

Property also could be added using admin page.

Application main page is http://localhost:8000/main (locahost might be different)

From main page, user can got to Properties List page or Add new property page.

On properties list page, user can click property price and it will take to edit page. On Edit page user can edit value,
user and property type. User also can delete on edit page.

Property owners has separate models, and One to Many relationship is set by ForeigKey.

Some HTML validation was used and messages about succesfull operations will be desplayed.

Property type and owner to be selected through drop down, so options are valid only from database.

Used class based views.

Before trying to add new property, user needs to be added through admin page.

http://localhost:8000/admin.
Login details: 
  username: xx
  password: xx
