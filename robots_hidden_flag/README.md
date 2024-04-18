## Hidden Flag
root robots.txt show us two new root to explore, here we are looking to ```.hidden```.    

When we was on ```http://x.x.x.x/.hidden``` we observe lot of root some README that containe text.   
The goal here is to explore all root and catch all README in order to catch the Flag.   
To do so, we have use the program ```recursiv_scropt.ps1``` for windows.   
This program go through all Page and right all README in ```ret_readme.txt```   
With a quick search in the file we catch the like to the Flag's URL :    
``` URL:
 http://192.168.56.101/.hidden//whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
 ```

OR we can be smart and see that "wil" name appears is the survey... it works !

## Patch 
Do not use ```robots.txt``` to store sensitive information
Do not use familiar patterns to store and hide information.