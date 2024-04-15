## Hidden Flag
root robots.txt show us two new root to explore, here we are looking to ```.hidden```.    

When we was on ```http://x.x.x.x/.hidden``` we observe lot of root some README that containe text.   
The goal here is to explore all root and catch all README in order to catch the Flag.   
To do so, we have use the program ```recursiv_scropt.ps1``` for windows.   
This programme go through all Page and right all README in ```ret_readme.txt```   
With a quick search in the file we catch the like to the Flag's URL :    
``` URL:
 http://192.168.56.101/.hidden//whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
 ```

## Patch 
Do not use ```robots.txt``` to store sensibles information