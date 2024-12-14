# Finding the Web Root in Apache

## ***1. Check Configuration Files***
* CentOS/RHEL:
   * /etc/httpd/conf/httpd.conf

* Debian/Ubuntu:
  * /etc/apache2/apache2.conf
 
> **Search for the DocumentRoot directive, which specifies the document root of the web server.**
```bash
DocumentRoot "/var/www/html"
```

* If you do not find DocumentRoot in the httpd.conf or apache2.conf file, look for this line:
```bash
IncludeOptional sites-enabled/
```

***This tells you that Apache is using virtual host configurations, typically stored in /etc/apache2/sites-enabled/ (for Debian/Ubuntu) or /etc/httpd/sites-enabled/ (for CentOS/RHEL).***

## ***2. Check Virtual Host Configuration Files***
* Virtual host configurations are typically located in the following directories:
   * /etc/apache2/sites-available/
   * /etc/apache2/sites-enabled/ (Debian/Ubuntu)
   * /etc/httpd/sites-enabled/ (CentOS/RHEL)

* The default config file is typically named:
   * 000-default.conf (for Debian/Ubuntu)
   * default.conf or 000-default.conf (for CentOS/RHEL)
    ```bash
    /etc/apache2/sites-enabled/000-default.conf
    /etc/httpd/sites-enabled/000-default.conf
    ```
