# Picha Gallery

## Description

This Application that allows Admin to post photos for users to see. The Admin can aslo provide details of the photo,delete,save and allows users to copy link to view image source. Users can search photos by category and location. 


## Author

Sandra Dindi

You can view the site at:[]()

## User Stories
As a user I would like to:
* See various photos  
* Copy link and directed to image source 
* Allowed to search by category
* Allowed to search by location
* Allowed to see image details


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display  photos | **On page load** | List of various photos from Admin is displayed on a page|
| Search for photo by category| **On search bar click submit** | see photos in a particular category|
| Search photo by location | **On search bar click submit** | see photos from a location|
| As Admin log in | **On Admin panel** | Upload photos by user by title,description,username,category,location|
| As Admin | **On log in** |  save,delete and update photos|
|Users can click on photo | **on click** | expand and see details of photo


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pipenv


### Cloning
* In your terminal:

        $ git clone git@github.com:Dindihub/my_gallery.git
        $ cd my-gallery

## Running the Application
* Creating the virtual environment

        $ pip3 install pipenv 
        $ pipenv shell
        
       


* To run the application, in your terminal:

        $ python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        $ python3.8  manage.py tests 

## Technologies Used
* Python3.8
* Django 4.0.4
* Heroku

## Known Bugs
No known bugs

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/my_gallery.git)**

