# CID

### Abstract:

This project will implement OAuth/OpenID -like functionality so that a user can register for one account that can log in to multiple websites.

### Description:

This app/website (CID) will allow an administrator of an external website to offload user authentication to CID. When a user needs authentication for a certain website, they will be presented with a login page or a registration page from CID. Upon successful completion authentication, the user will be redirected to their desired website as an authenticated user. In the backend side of things, the 3rd party server will request a token from CID after user authentication, which is then written to a cookie for the user. This cookie will be used to keep the user logged in from this point on. CID will keep track of which websites the user is registered for.
