import os
from PIL import Image, ImageDraw, ImageFont

def create_twitter_post():
    width, height = 1080, 1080
    bg_color = (0, 0, 0) # Pure Twitter dark mode
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    font_dir = "C:/Windows/Fonts"
    f_name = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 38)
    f_handle = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 30)
    f_body = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 38)
    f_body_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 38)
    f_meta = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 28)
    f_card_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 30)
    f_card_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 24)
    
    # Outer margin
    pad_x = 70
    top_y = 90
    
    # Profile Picture (Circle)
    pfp_radius = 45
    pfp_center = (pad_x + pfp_radius, top_y + pfp_radius)
    draw.ellipse([pad_x, top_y, pad_x + 90, top_y + 90], fill=(50, 30, 90), outline=(242, 202, 115), width=2)
    draw.text((pad_x + 28, top_y + 20), "✦", fill=(242, 202, 115), font=f_name)
    
    # Name & Handle
    draw.text((pad_x + 115, top_y + 4), "Mahila Luz ✦", fill=(255, 255, 255), font=f_name)
    # Verified badge (blue circle with check)
    v_x = pad_x + 360
    draw.ellipse([v_x, top_y + 12, v_x + 24, top_y + 36], fill=(29, 155, 240))
    draw.text((v_x + 5, top_y + 9), "✓", fill=(255, 255, 255), font=ImageFont.truetype(os.path.join(font_dir, "arial.ttf"), 16))
    
    draw.text((pad_x + 115, top_y + 50), "@mahilaluz • 3h", fill=(113, 118, 123), font=f_handle)
    
    # Tweet text
    tweet_y = top_y + 130
    lines = [
        "Se você nasceu entre as 06h e as 18h, o seu Sol governa a sua vitalidade. Mas se nasceu à NOITE, a sua Lua comanda 90% das suas decisões emocionais e financeiras.",
        "",
        "A maioria das pessoas passa a vida sofrendo porque tenta forçar resultados que vão contra o alinhamento kármico da sua Casa natal.",
        "",
        "Se você sente que sua energia travou nos últimos meses, faça o teste de 2 minutos do seu mapa:"
    ]
    
    curr_y = tweet_y
    for l in lines:
        if not l:
            curr_y += 18
            continue
        # Word wrap
        tokens = l.split(' ')
        line_str = ""
        for tok in tokens:
            test_str = line_str + tok + " "
            bbox = draw.textbbox((0, 0), test_str, font=f_body)
            if bbox[2] - bbox[0] > 940:
                draw.text((pad_x, curr_y), line_str, fill=(231, 233, 234), font=f_body)
                curr_y += 50
                line_str = tok + " "
            else:
                line_str = test_str
        if line_str:
            draw.text((pad_x, curr_y), line_str, fill=(231, 233, 234), font=f_body)
            curr_y += 50
            
    # Embedded Link Card Preview
    card_y = curr_y + 25
    draw.rounded_rectangle([(pad_x, card_y), (pad_x + 940, card_y + 190)], radius=16, fill=(22, 24, 28), outline=(47, 51, 54), width=1)
    
    draw.text((pad_x + 24, card_y + 22), "mapa-astral-oficial.vercel.app", fill=(113, 118, 123), font=f_card_sub)
    draw.text((pad_x + 24, card_y + 58), "Calculadora do Mapa Astral • Leitura Guiada em Áudio", fill=(255, 255, 255), font=f_card_title)
    draw.text((pad_x + 24, card_y + 105), "Descubra seu Ascendente, Signo Lunar e os 7 segredos do seu nascimento.", fill=(113, 118, 123), font=f_card_sub)
    draw.text((pad_x + 24, card_y + 145), "🔗 Toque para iniciar o cálculo gratuito", fill=(29, 155, 240), font=f_card_sub)
    
    # Twitter Metrics Bar
    bar_y = card_y + 225
    draw.line([(pad_x, bar_y), (pad_x + 940, bar_y)], fill=(47, 51, 54), width=1)
    
    metrics = "💬 842         🔁 2.190         ❤️ 24,6 mil         📊 412 mil"
    draw.text((pad_x + 20, bar_y + 25), metrics, fill=(113, 118, 123), font=f_meta)
    
    out_path = "C:/Users/natan/.gemini/antigravity/scratch/funil_work/assets/img/criativo_2_tweet_astrologico.jpg"
    img.save(out_path, quality=95)
    print("Salvo:", out_path)

create_twitter_post()
