"""
Note: This program doesn't working if u run it from Pycharm run terminal or from Powershell.
"""

import wexpect

print("Spawn a command prompt")
# Start the command prompt
child = wexpect.spawn(r"C:\Windows\system32\cmd.exe")
child.expect('>')
child.sendline('gh auth login')

print("Login to GitHub")
# Run 'gh auth login'
child.sendline('gh auth login')
child.expect('.*')
print("Stream text after 'gh auth login':")
print(child.after)

print("Choose the first option [Step 1]")
# Step 1: Choose the first option (e.g., GitHub CLI)
child.sendline('\r1')
child.expect('.*')
print("Stream text after choosing the first option [Step 1]:")
print(child.after)

print("Choose the first option [Step 2]")
# Step 2: Choose the first option again (e.g., HTTPS)
child.sendline('\r1')
child.expect('.*')
print("Stream text after choosing the first option [Step 2]:")
print(child.after)

print("Confirm with 'y' [Step 3]")
# Step 3: Confirm with 'y'
child.sendline('\ry')
child.expect('.*')
print("Stream text after confirming with 'y' [Step 3]:")
print(child.after)

print("Choose the first option [Step 4]")
# Step 4: Choose the first option again (e.g., login with a web browser)
child.sendline('\r1')
child.expect('.*')
print("Stream text after choosing the first option [Step 4]:")
print(child.after)

print("Press enter [Step 5]")
# Step 5: Press enter
child.sendline('\r\n')
child.expect('.*')
print("Stream text after pressing enter [Step 5]:")
print(child.after)

print("Close the process")
# Close the process
child.close()
print("Process closed")
