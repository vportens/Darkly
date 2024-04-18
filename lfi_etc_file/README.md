## Local File Inclusion (LFI) / Remote File Inclusion (RFI)



On linux /etc/passwd is use to store information on system's user.

![image](./Ressources/etc_passwd.png)
Page parameter can be exploited to access sensitive file here. 
To reduce the posibility of RFI we can unable some PHP configuration and add a whitelist. 
Here ```../../../../../../../etc/passwd``` gives us the flag


## Patch 
- Disable ```allow_url_fopen``` and ```allow_url_include``` using PHP

- Use a list of allowed page like
```php
$allowed_pages = ['home.php', 'contact.php'];

if (in_array($_GET['page'], $allowed_pages)) {
    include($_GET['page']);
} else {
    echo "Access Deny"
}
```
