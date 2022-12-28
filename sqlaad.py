import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=tcp:silicondb.database.windows.net,1433;'
                      'Database=silicondb;'
                      'Uid=spuser@sid24desaioutlook.onmicrosoft.com;'
                      'Pwd=Watermelon@123;'
                      'Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Authentication=ActiveDirectoryPassword;')


cursor = conn.cursor()
cursor.execute('Select * FROM OnlineCourses')
for i in cursor:
    print(i)

cursor.close()
conn.close()

#server=Server;
# database=Database;
# UID=UserName;
# PWD=Password;
# Authentication=ActiveDirectoryPassword;
# # Encrypt=yes;

# Driver={ODBC Driver 13 for SQL Server};
# Server=tcp:silicondb.database.windows.net,1433;
# Database=silicondb;Uid=spuser@sid24desaioutlook.onmicrosoft.com;
# Pwd={your_password_here};
# Encrypt=yes;
# TrustServerCertificate=no;
# Connection Timeout=30;
# Authentication=ActiveDirectoryPassword