# Finding the Web Root in Nginx

## ***1. Check Configuration Files***
* CentOS/RHEL:
   * /etc/nginx/nginx.conf

* Debian/Ubuntu:
  * /etc/nginx/nginx.conf
 
> **Search for the server block, which typically defines the virtual hosts, including document root details.**
```bash
server {
    listen 80;
    server_name example.com;
    root /var/www/html;
    index index.html index.htm;
}
```

* If you do not find the root directive in the nginx.conf file, you should look for include directives which load configurations from additional files
```bash
include /etc/nginx/sites-enabled/*;
```

***This tells you that Nginx is likely using server block configuration files (virtual hosts), usually located in /etc/nginx/sites-enabled/ or /etc/nginx/conf.d/***

## ***2. Check Virtual Host Configuration Files***
* Virtual host configurations are typically located in the following directories:
   * /etc/nginx/sites-available/ (Debian/Ubuntu)
   * /etc/nginx/sites-enabled/ (Debian/Ubuntu)
   * /etc/nginx/conf.d/ (sometimes used in CentOS/RHEL)

* The default config file is typically named:
   * default (for Debian/Ubuntu)
   * default.conf (for CentOS/RHEL)
    ```bash
    /etc/nginx/sites-enabled/default
    /etc/nginx/conf.d/default.conf
    ```
