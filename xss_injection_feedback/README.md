## XSS Injection 

Here we are invited to leave a feedback on the comment section.  
We can try to pass HTML balise on the comment section like 
```<img src="javascript:alert('XSS')">``` to put image insted of word

Here we need a specifiq injection : 
``` <svg/onload=alert('XSS')>a```
to access the flag

![image](./Ressources/xss_injection.png)

## Patch
- controle user input 
- use security framework
