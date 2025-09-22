import String
import secrets
from .models import coupon

def generate_coupon_code(length=10):
    characters=string.ascii_uppercase +string.digits

    while True:
        code =''.join(secrets.choice(characters) for _in range(lenght))

        if not Coupon.objects.filter(code=code).exists():
            return code;