# CID

### Abstract:

This project will implement OAuth/OpenID -like functionality so that a user can register for one account that can log in to multiple websites.

### Description:

This app/website (CID) will allow an administrator of an external website to offload user authentication to CID. When a user needs authentication for a certain website, they will be presented with a login page or a registration page from CID. Upon successful completion authentication, the user will be redirected to their desired website as an authenticated user. In the backend side of things, the 3rd party server will request a token from CID after user authentication, which is then written to a cookie for the user. This cookie will be used to keep the user logged in from this point on. CID will keep track of which websites the user is registered for.
Note: For the sake of having 3rd party websites, very basic websites will be created to communicate to CID and check for cookies.

### Page details:
- Login/Registration for User
  - Email cannot be duplicated
  - Email should be validated for format
  - Minimum password length of 8 characters
  - Registration password and confirmation must match
  - Bcrypt used for storing passwords and authentication
  - No fields may be empty

### Stretch Goals:
- Login/Registration for Admin
  - Email cannot be duplicated
  - Email should be validated for format
  - Minimum password length of 8 characters
  - Registration password and confirmation must match
  - Bcrypt used for storing passwords and authentication
  - No fields may be empty
- Admin Dashboard
  - Displays all the websites with their name, callback url, and API key
  - Each website is clickable to edit
  - Add website
  - No fields may be empty
  - Callback url should be validated for format
  - new API key generated upon successful submission
  - Edit website (not shown, but will look similar to Add Website with an extra button to request for a new API key)
  - No fields may be empty
  - Callback url should be validated for format
  - Only accessible by administrators
  - Be able to see a list of their users for each website and be able to deny access
  - Be able to grant different authorization levels/categories
  - Has button to request a new API key and also invalidates the old one
  - Old API key is not deleted, but it is marked as invalid
- Add more user information on registration. Each user can see this info on registration to a 3rd party site and be able to grant what access that site has to this info
