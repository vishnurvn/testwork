from object_map import Element


class LoginPage:
    USERNAME_FIELD = Element("logintxt", "id")
    PASSWORD_FIELD = Element("passwordtxt", "id")
    LOGIN_BUTTON = Element("userlogin", "id")


class DisclaimerPage:
    ACCEPT_BUTTON = Element("//*[@id='pt1:r1:0:cb1']", "xpath")


class HomePage:
    RAVE_ICON = Element("//*[@id='pt1:cb24']", "xpath")
