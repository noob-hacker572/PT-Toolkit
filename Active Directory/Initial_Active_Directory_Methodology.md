# **Initial Enumeration is not limited to the instruction provided in this Document**

## **--> Ports to Know <--**

  - **135/139/445**: SMB/NB
  - **88**: Kerberos
  - **3269**: Global Catalog
  - **389**: LDAP

## **Steps to Follow**

### **1. Run Nmap**
   - Execute the following commands:
     ```bash
     nmap -sC -sV -v -oA nmap $IP
     ```
   - After waiting, run:
     ```bash
     nmap -sC -p- -sV -oA all-ports $IP
     ```

### **2. Check for Web Server**
   - You do not have to wait for Nmap; check the server directly for the following ports:
     - **80**, **443**, **8080**, **8090**, **65535**

### **3. Enumerate SMB (Ports 135, 139, 445)**
   - Use tools such as:
     - `smbclient`
     - `rpcclient`
     - `netexec`
     ```bash
      netexec smb <target-ip>-u 'guest' -p '' --rid-brute
     ```
     - `Nmap Scripts`
     ```bash
     nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse $IP
     ```
     - `enum4linux`
     - `smbmap`
     - Refer to the tools in your documentation

### **4. Enumerate DNS (Port 53)**
   - Run the following command in the terminal:
     ```bash
     nslookup
     > server <dc-ip>
     > dc-ip
     ```
   - Other tools:
     - `dig`
     - `dnsenum` (refer to your documentation)

### **5. Enumerate LDAP (Port 389)**
   - To get the schema, run:
     ```bash
     ldapsearch -H ldap://<dc-ip> -x -s base namingcontext
     ```
     (This will give you results like this `DC=domain,DC=local`)
   - Now run:
     ```bash
     ldapsearch -H ldap://<dc-ip> -x -b "DC=domain,DC=local"
     ```
     ```bash
     ldapsearch -H ldap://<dc-ip> -x -b "DC=domain,DC=LOCAL" '(objectClass=user)' sAMAccountName | grep sAMAccountName
     ```
   - Get the password policy using tools like:
     - `crackmapexec`
     - `enum4linux`
     - `enu4linux-ng.py`
   - If you find the usernames above, then move to step 7.
   - Run Kerbrute from your documentation.

### **6. Do Kerberoasting Attack**
   - Refer to the documentation for:
     - Active Directory > Enumeration to FootHold > Kerberos SPN Service Accounts
     - Active Directory > Post Enumeration > Kerberoasting

### **7. Creating a WordList**
   - Check your documentation under:
     - HTB ALL Tools > Password Attacks > WordList Creation > ForLoop
   - By now, you should know the password policy:
     ```bash
     cat passwd.txt | awk 'length($0) >= 8'
     ```
     ```bash
     cat passwd.txt | awk 'length($0) > 8'
     ```

### **8. Password Spraying or Brute Force**
   - If you have a valid password, then proceed with password spraying; otherwise, do brute force.
   - Make sure you know the password policy before this step, as it can be catastrophic and lock out accounts.
   - Refer to the documentation for:
     - Active Directory > Enumeration to FootHold > Password-Spraying
