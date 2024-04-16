## Dictionnary attack

Here we can try to connect by using a login/password, but there is no restriction about the number of try, no catpcha, or time limite access.
So we gonna use the 10millions most use password to try to login, 
Luckly, for us, not for the website, but there is someone using ```shadow``` password that is in the list.
And this password work with every username ...

## Patch

- Use a captcha
- Use a limit rate from an ip, to avoid massive call from a bot
- Use stronger password, salt, and hash with restriction like minimun 12 caractere
 