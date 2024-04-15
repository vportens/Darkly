
## Hidden Password

root robots.txt show us two new root to explore, here we are looking to ```whatever```   
When we go to ```http://x.x.x.x/whatever``` we observe a page named htpasswd that contained :   
```root:437394baff5aa33daa618be47b75cb49```
using MD5 to decrypte the code give us : ```qwerty123@```
Now we can go to the ```http://x.x.x.x/admin``` page and try to log as  ```root```
with ```qwerty123@``` as password.   
