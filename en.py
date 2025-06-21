from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key.decode())
#K0fc3LdOBFprIeGy1iueOVzCspkRruzdGviL_QyeY7k=