"""
@ Author - Krishnabhashkar jha
@ Creation date - 25/03/2020
@ Description - Declares all the xpaths, username and password .
"""
# All URL's
TogglURL = 'https://toggl.com/login/'


# Credentials
Username = "scroy@spscommerce.com"
Password = "Doremon@2019"

# Xpaths
Login_Username_Xpath_Click = "//input[@type='email' and @name = 'email-address' and @id ='login-email']"
Login_Password_Xpath_Click = "//input[@type='password' and @name = 'password' and @id ='login-password']"
Login_Click = "//button[contains(@type,'submit') and contains(@id,'login-button')]"
Reports_Click = ".//*[contains(@id,'navigation-menu')]/div[2]//*[contains(text(),'Analyze')]/following::*[contains(text(),'Reports')][1]"
Team_Click = ".//*[contains(text(),'Filter by:')]/following::*[contains(text(),'Team')][1]"
Find_Name = ".//input[@type='text' and @placeholder='Find members or groups...']"
Summary_Click = ".//*[contains(text(),'Summary')]"
Duration_Click = "//*[contains(text(),'Filter by:')]/following::button[@type='button'][2]"
Today_Click = "//button[contains(text(),'Today')]"
Yesterday_Click = "//button[contains(text(),'Yesterday')]"
Thisweek_Click = "//button[contains(text(),'This week')]"
Lastweek_Click = "//button[contains(text(),'Last week')]"
Thismonth_Click = "//button[contains(text(),'This month')]"
Lastmonth_Click = "//button[contains(text(),'Last month')]"
Thisyear_Click = "//button[contains(text(),'This year')]"
Lastyear_Click = "//button[contains(text(),'Last year')]"
None_Click = ".//*[contains(text(),'Filter by:')]/following::*[contains(text(),'Team')][1]/following::*[contains(text(),'None')][1]"
Clock_Click = '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span/span[1]'
Sc_Click = ".//*[contains(text(),'IMP Time Tracking')]/following::*[contains(text(),'Sc')][2]"
LogOut_Click = ".//*[contains(text(),'Log Out')]"