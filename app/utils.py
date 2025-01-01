from captcha.image import ImageCaptcha
import random
import string

def generate_captcha():
    image = ImageCaptcha()
    # captcha_text = "1234"  # Replace with randomized text generation logic
    # random 6 alphanumeric chars
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    captcha_image = image.generate_image(captcha_text)
    return captcha_text, captcha_image

def verify_captcha(correct_text, user_input):
    return correct_text == user_input

