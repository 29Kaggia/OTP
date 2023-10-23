import random
import string

# Generating a random OTP
def generate_otp(length=6):
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for i in range(length))
    return otp

# Verify the OTP
def verify_otp(otp, input_otp):
    return otp == input_otp

# Example of a simple model to manage OTPs
class OTPModel:
    def __init__(self):
        self.otp = None

    def generate_otp(self, length=6):
        self.otp = generate_otp(length)
        return self.otp

    def verify_otp(self, input_otp):
        if self.otp:
            result = verify_otp(self.otp, input_otp)
            if result:
                self.otp = None
            return result
        return False

# Example usage
otp_model = OTPModel()
generated_otp = otp_model.generate_otp()
print(f"Generated OTP: {generated_otp}")

# Simulating OTP input
user_input = input("Enter the OTP: ")

if otp_model.verify_otp(user_input):
    print("OTP verification successful.")
else:
    print("OTP verification failed.")

