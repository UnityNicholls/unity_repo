import base64
from seleniumbase import SB

# Ask the user for base64 input
b_input = 'aHR0cHM6Ly9raWNrLmNvbS9icnV0YWxsZXM='
desd_b = base64.b64decode(b_input)
ssax = desd_b.decode('utf-8')
with SB(uc=True, test=True) as unity:
    url = ssax
    unity.uc_open_with_reconnect(url, 5)
    unity.uc_gui_click_captcha()
    unity.sleep(2)
    unity.uc_gui_handle_captcha()
    
    unity2 = unity.get_new_driver(undetectable=True)
    unity.uc_open_with_reconnect(url, 5)
    unity.uc_gui_click_captcha()
    unity.sleep(2)
    unity.uc_gui_handle_captcha()

    while(unity.is_element_present('video#video-player')):
        unity.sleep(10)
