from passlib.hash import sha256_crypt
password="agent@123"
testpassword = sha256_crypt.hash(password)
print(testpassword)
#$5$rounds=535000$fC0hzjRQhp6.LqFR$hmsIbboqNjV0IblCh9fIcs6P3jZOBUGfn5P3jQNzze1
#$5$rounds=535000$9cVBuyaLbVxmY7D.$56SYe2JVIBA.uAFVMWw.IFCgA7c45UWJeFZMUqtOhJ4
val_password = sha256_crypt.verify(password,'$5$rounds=535000$fC0hzjRQhp6.LqFR$hmsIbboqNjV0IblCh9fIcs6P3jZOBUGfn5P3jQNzze1' )
print(val_password)