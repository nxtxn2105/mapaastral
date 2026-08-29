import os
from PIL import Image, ImageDraw, ImageFont

def create_lockscreen_notification():
    width, height = 1080, 1080
    
    # Elegant dark celestial wallpaper (subtle dark night sky)
    img = Image.new("RGB", (width, height), (15, 12, 28))
    draw = ImageDraw.Draw(img)
    
    font_dir = "C:/Windows/Fonts"
    f_time = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 140)
    f_date = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 36)
    f_app = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 30)
    f_time_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 26)
    f_notif_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 34)
    f_notif_body = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 32)
    f_btn = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 32)
    
    # Lockscreen Clock & Date
    draw.text((370, 160), "21:42", fill=(255, 255, 255), font=f_time)
    draw.text((380, 320), "Sexta-feira, 28 de agosto", fill=(210, 205, 225), font=f_date)
    
    # iOS Notification Card (Frosted glass effect)
    card_x = 80
    card_y = 440
    card_w = 920
    card_h = 320
    
    # Card Background (Semi-translucent dark glass)
    draw.rounded_rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], radius=32, fill=(35, 30, 52), outline=(75, 65, 105), width=2)
    
    # App Header inside card
    # Green WhatsApp dot / icon
    draw.ellipse([card_x + 35, card_y + 35, card_x + 75, card_y + 75], fill=(37, 211, 102))
    draw.text((card_x + 47, card_y + 38), "💬", fill=(255, 255, 255), font=ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 22))
    
    draw.text((card_x + 95, card_y + 40), "MENSAGEM ASTRAL", fill=(195, 185, 220), font=f_app)
    draw.text((card_x + card_w - 150, card_y + 42), "agora mesmo", fill=(140, 130, 165), font=f_time_sub)
    
    # Notification Title
    draw.text((card_x + 35, card_y + 105), "Astróloga Mahila Luz ✦", fill=(242, 202, 115), font=f_notif_title)
    
    # Notification Message Body
    msg_lines = [
        "Calculei o alinhamento da sua data de nascimento:",
        "o motivo de você sentir que seus caminhos travaram",
        "está na sua Casa 12. Sua leitura completa foi liberada..."
    ]
    ny = card_y + 160
    for ml in msg_lines:
        draw.text((card_x + 35, ny), ml, fill=(240, 235, 255), font=f_notif_body)
        ny += 42
        
    # Tap to open hint
    hint_y = 860
    draw.rounded_rectangle([(180, hint_y), (900, hint_y + 80)], radius=24, fill=(242, 202, 115))
    draw.text((250, hint_y + 20), "TOQUE PARA OUVIR SUA LEITURA ➔", fill=(20, 12, 38), font=f_btn)
    
    # Swipe bar at bottom
    draw.rounded_rectangle([(390, 1020), (690, 1028)], radius=4, fill=(200, 200, 200))
    
    out_path = "C:/Users/natan/.gemini/antigravity/scratch/funil_work/assets/img/criativo_3_notificacao_celular.jpg"
    img.save(out_path, quality=95)
    print("Salvo:", out_path)

create_lockscreen_notification()
