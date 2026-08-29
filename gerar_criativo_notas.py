import os
from PIL import Image, ImageDraw, ImageFont

def create_iphone_notes():
    # 1080 x 1080 square for feed/ads
    width, height = 1080, 1080
    
    # iOS Notes background (clean light warm white)
    bg_color = (255, 255, 255)
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Fonts
    font_dir = "C:/Windows/Fonts"
    f_large_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 48)
    f_date = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 26)
    f_body = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 34)
    f_body_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 34)
    f_header = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 32)
    f_pill = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 32)
    
    # iOS Header Bar
    yellow_notes = (212, 160, 23)
    gray_text = (142, 142, 147)
    dark_text = (28, 28, 30)
    
    # "< Pastas" on top left
    draw.text((60, 60), "‹  Notas", fill=yellow_notes, font=f_header)
    
    # Share and more icons on top right
    draw.text((950, 60), "•••", fill=yellow_notes, font=f_header)
    draw.text((860, 58), "⎋", fill=yellow_notes, font=f_header)
    
    # Thin separator line
    draw.line([(50, 120), (1030, 120)], fill=(235, 235, 238), width=2)
    
    # Date timestamp
    draw.text((60, 150), "28 de agosto • 21:42", fill=gray_text, font=f_date)
    
    # Title
    title = "Aviso para quem nasceu entre 1980 e 2005:"
    draw.text((60, 210), title, fill=dark_text, font=f_large_title)
    
    # Body lines
    body_y = 300
    paragraphs = [
        ("Se você sente que a sua vida financeira ou amorosa deu uma travada bizarra nos últimos meses, o problema não é falta de esforço.", False),
        ("A astrologia tradicional explica isso com clareza: a maioria das pessoas só conhece o signo solar, mas é a sua LUA e a sua Casa 12 que governam o que você atrai.", False),
        ("O alinhamento planetário do seu nascimento revela:", True),
        ("• O padrão oculto que faz você atrair pessoas desgastantes\n• O bloqueio kármico que drena seu dinheiro e energia\n• O ritual simples do seu elemento para destravar seus caminhos", False),
        ("Fiz a leitura guiada completa hoje e fez mais sentido do que anos de terapia. Leva 2 minutos para calcular.", False),
        ("Toque no botão abaixo para fazer o seu teste:", True)
    ]
    
    current_y = body_y
    for text, is_bold in paragraphs:
        f = f_body_bold if is_bold else f_body
        color = (180, 40, 40) if "Toque no botão" in text else dark_text
        
        # Word wrap
        words = text.split('\n')
        for sub in words:
            # simple line breaking
            tokens = sub.split(' ')
            line = ""
            for token in tokens:
                test_line = line + token + " "
                bbox = draw.textbbox((0, 0), test_line, font=f)
                if bbox[2] - bbox[0] > 960:
                    draw.text((60, current_y), line, fill=color, font=f)
                    current_y += 48
                    line = token + " "
                else:
                    line = test_line
            if line:
                draw.text((60, current_y), line, fill=color, font=f)
                current_y += 48
        current_y += 24
        
    # Simulated iOS yellow button at bottom
    btn_y = 960
    draw.rounded_rectangle([(60, btn_y), (1020, btn_y + 75)], radius=18, fill=(245, 195, 35))
    draw.text((360, btn_y + 16), "CALCULAR MEU MAPA AGORA →", fill=(20, 20, 20), font=f_pill)
    
    out_path = "C:/Users/natan/.gemini/antigravity/scratch/funil_work/assets/img/criativo_1_bloco_de_notas.jpg"
    img.save(out_path, quality=95)
    print("Salvo:", out_path)

create_iphone_notes()
