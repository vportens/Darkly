## Weak cookie

We see in all pages the I_am_admin cookie, 
if we take the cookie and put it on internet, the first site is a convertor md5.
The cookies translate to 'false'
So we try to convert 'true' in md5 and past it as the new cookie.  
Refresh the page, and tada you got the Flag

![image](./Ressources/cookie_result.png)

## Patch 

MD5 is not safe and cookie is publicly available.
Always randomise cookie value, and if you really want to use MD5, salt it.