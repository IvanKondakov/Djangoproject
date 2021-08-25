# Djangoproject

1. Description
2. Libraries
3. App's
4. Updates after pre-release

## 1 Description

This project was created during my studies at the university, to defend one of the subjects. The project is a blog on Django with the ability to register, create and edit posts (including deleting), post likes, categorization, user subscription and category subscription. The main goal was to make a project that would include new technologies and techniques that I had not used before. Thus, in this project, I first met in Django and its template engine, the features of authorization on Django, authorization using telegrams, in general how to interact with a telegram, the features of interacting with the database in Django.

## 2 Libraries

All necessary dependencies are in **requrements.txt**
Short list:

- Django==3.2
- django-ckeditor==6.0.0
- django-quill==0.1.0
- gunicorn==20.0.4
- loguru==0.5.3
- oauthlib==3.1.0
- Pillow==8.2.0

## 3 App's

1. Aft - Registration application
2. Main - Basic urls
3. Blog - Blog application
4. fortysixth - Main application

### 3.1 Aft

Pages:

- logout
- login
- sign_up

There are two types of registration.

<img src="https://sun9-53.userapi.com/impg/PIOUX3p9aDfgNXvDkVp02hpyAOwp8AUVNgw70A/OWCz6TYM-dg.jpg?size=590x531&quality=96&sign=7eeeea8fe3c802d197fcfad432f5b30f&type=album" width=40% height=55%> </img>

The first is the usual one with entering parameters into the form and confirming. The user enters data into the form after which he is asked to confirm the registration by clicking on the link. The link is now coming to the telegram bot.

After confirm we create a profile user and redirect him to site.

The second via telegram. After all the user confirmations, we intercept his image and nickname, after which we enter it into the user database and create a profile for him. We get the hash of the user, I think it can be used as a password by re-encoding it for storage in the database.

### 3.2 Main

Pages:

- About
- Follow (only as POST)

On the about page, you can view information about yourself, this page also provides a view of information about other users.
On this page, if it belongs to the user, then he can edit information about himself, include the picture (name, surname, email - not yet possible).

<img src="https://sun9-29.userapi.com/impg/1D0xvv_54bSqFyaC2j44NqzVofH2piC_vDpcwg/mRZ-DknoUic.jpg?size=1280x642&quality=96&sign=6aec59f4d943235e732e182cffc8cb5d&type=album" width=65% height=65%> </img>

Information about another user is visible on the page of another user, as well as the ability to subscribe and unsubscribe.

<img src="https://sun9-31.userapi.com/impg/_18ofctXGpjIS3Q8s6zd7zRrjW-dllSn-n6TDQ/8xlZEJR_hbo.jpg?size=1280x642&quality=96&sign=01d1fe4008b4e757144ea4bf1318031b&type=album" width=65% height=65%> </img>

------

<img src="https://sun9-52.userapi.com/impg/REe1swQazktzxXJCEVTDUUVcXCWZppPQAALZfw/by_LZzHiwzM.jpg?size=159x62&quality=96&sign=c70b31794ed8f5ddd913b04a4c80ee34&type=album" width=10% height=10%> </img>

### 3.3 Blog

Pages:

- Blog - Own articles
- Blog detail - 
- Feed - Articles by other users
- Follow category (only as POST)
- Likes (only as POST)

The blog page shows blogs written by the user, that is, he is the author. Here you can create your own blog, as well as later edit and delete it. By clicking on the blog, you can simply read it.

<img src="https://sun9-40.userapi.com/impg/UIPoKai-_PrkadeOdaOjOK71ZtUcPAU5G-xY0A/O9xZxMoJKHM.jpg?size=1280x629&quality=96&sign=9f77c5449f623579d284f28783d6a222&type=album" width=50% height=50%> </img>

------

<img src="https://sun9-19.userapi.com/impg/wjAsU62T5k9tZRfvcvhrHs_HiIvpH-QbhpS4BA/7jgw5gnNrp4.jpg?size=1280x868&quality=96&sign=b36a6221065ce4d0656486340cf58441&type=album" width=50% height=50%> </img>

------

<img src="https://sun9-56.userapi.com/impg/o3E6_pVHhieCp-UID8uT_OXw8hvCtnemeQr98g/KHgDcxdu0Kc.jpg?size=1123x856&quality=96&sign=752c2437efdf0fb35c3d7d08164c652e&type=album" width=50% height=50%> </img>

On the post reading page, you can like the post, subscribe to the author or subscribe to a category.

<img src="https://sun9-72.userapi.com/impg/dqzG0aI7eho9YZwLs9bHb6pt12IqG0TD5G9bgQ/0meWjZI7daA.jpg?size=837x89&quality=96&sign=d390f858302f32dd40aefe082e2a4c7e&type=album" width=70% height=10%> </img>

On the Feed page, you can see articles written by users you follow, new articles that someone else has made, and articles whose category matches the ones you subscribed to. Also here you can go to the category pages, where all the articles of a specific category. You can of course go to these articles to read them. In the same place, subscribe to the author, category and like. By the way, the likes counter is visible both on the feed page and on the blog.

<img src="https://sun9-26.userapi.com/impg/QaeRux93oN2L2wdliI_H1tSkxs5c_6VZtFbtBA/xM6zUDrJZPA.jpg?size=838x795&quality=96&sign=7c02c64f051d07209c347be906355a24&type=album" width=50% height=55%> </img>

------

<img src="https://sun9-59.userapi.com/impg/02xNO9bkUsbIRUVfTvnJ5ZJkW8eOKUOXp0eCUg/GnGmFFHSOTM.jpg?size=485x842&quality=96&sign=e7af7f86ca58777a18615515f2342789&type=album" width=30% height=55%> </img>

------

<img src="https://sun9-7.userapi.com/impg/BgNRXK0jKriGPV_3bSESvBFi4WiVox_qyKRlWQ/swQfLvTm8FY.jpg?size=379x765&quality=96&sign=5613ceedc8be0c1de4b49f5a321d7126&type=album" width=25% height=40%> </img>

## 4 Updates after pre-release

What exactly will be done in the future:

- Password for telegram users
- Editing all information, i.e. name, surname and e-mail
- Comments under posts

> The site is available at the [link](http://djblog.me/)

