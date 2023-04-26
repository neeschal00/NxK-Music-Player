# NxK Music Player

This is an attempted online **Music Streaming** platform written in Django. The web application supports the CRUD operations for playlists for normal users and the music is added by the admin with related information.

#HOSTED LINK
https://nxk-musicapp.herokuapp.com/

# Tools and Technologies:

NxK music player uses several tools to appropriately function in its current state which are mentioned below :

- Django
- Bootstrap
- HTML/CSS/Javascript
- Aplayer jquery library
- Ajax Form Submission

## SETUP
### Preferred Python version 3.7

Firstly clone create a virtualenv and

```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```
- Setup Spotify:
Register in https://developer.spotify.com/
Create an app and obtain the clientId and Client Secret.
Add the obtained ClientId and ClientSecret to "mainui.html" in the templates directory like below 
```
const clientId = 'Your Client Id ';
const clientSecret = 'Your Client Secret';
```


# User Interface ScreenShots
- Front Screen
![Alt text](/Screenshots/frontpage.png?raw=true "Front Screen")

- Explore Page
![Alt text](/Screenshots/explorepage.gif?raw=true "Explore Page")

- All Songs Page Panel
![Alt text](/Screenshots/homepanel.gif?raw=true "All Songs Pannel")

- Favourites and Playlist
![Alt text](/Screenshots/favplaylist.gif?raw=true "Favourites and Playlist Page")

- Admin Panel
![Alt text](/Screenshots/Admin-Dashboard.gif?raw=true "Admin Dashboard")

- Registration
![alt-text-2](/Screenshots/registration.png "Registration UI")


