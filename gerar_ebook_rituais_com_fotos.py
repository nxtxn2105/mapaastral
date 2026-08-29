import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle, Image
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        if self._pageNumber == 1:
            return  # Não desenha header/footer na capa visual

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#7a6f91"))

        # Cabeçalho
        self.drawString(45, 800, "✦ MAHILA LUZ • O GUIA DOS RITUAIS LUNARES & BLINDAGEM ENERGÉTICA")
        self.setStrokeColor(colors.HexColor("#e2d9ec"))
        self.setLineWidth(0.5)
        self.line(45, 792, 550, 792)

        # Rodapé
        self.line(45, 45, 550, 45)
        self.drawString(45, 32, "Conteúdo de Proteção Espiritual e Autoconhecimento • Edição Ilustrada de Luxo")
        page_str = f"Página {self._pageNumber} de {total_pages}"
        self.drawRightString(550, 32, page_str)

        self.restoreState()

pdf_filename = "O_Guia_dos_Rituais_Lunares_Mahila_Luz.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=45,
    rightMargin=45,
    topMargin=55,
    bottomMargin=55
)

# Paleta Mística
C_PRIMARY = colors.HexColor("#1b0f38")
C_GOLD = colors.HexColor("#c59b27")
C_ROSE = colors.HexColor("#9b3c5a")
C_EMERALD = colors.HexColor("#1b6348")
C_TEXT = colors.HexColor("#2a2436")
C_MUTED = colors.HexColor("#6b6080")
C_CARD_BG = colors.HexColor("#f8f4fc")
C_BORDER = colors.HexColor("#decfe8")

styles = getSampleStyleSheet()

cover_title = ParagraphStyle(
    'CoverTitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=24, leading=30,
    textColor=C_PRIMARY, alignment=1
)
cover_sub = ParagraphStyle(
    'CoverSub', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=11, leading=16,
    textColor=C_GOLD, alignment=1
)
author_style = ParagraphStyle(
    'CoverAuthor', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=11, leading=15,
    textColor=C_ROSE, alignment=1
)
h1_style = ParagraphStyle(
    'H1', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=15, leading=20,
    textColor=C_PRIMARY, spaceBefore=12, spaceAfter=8
)
h2_style = ParagraphStyle(
    'H2', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=11.5, leading=15,
    textColor=C_GOLD, spaceBefore=8, spaceAfter=4
)
body = ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontName='Helvetica', fontSize=9.5, leading=14,
    textColor=C_TEXT, spaceAfter=6
)
card_body = ParagraphStyle(
    'CardBody', parent=styles['Normal'],
    fontName='Helvetica', fontSize=9, leading=13.5,
    textColor=C_PRIMARY
)
caption_style = ParagraphStyle(
    'Caption', parent=styles['Normal'],
    fontName='Helvetica-Oblique', fontSize=8, leading=11,
    textColor=C_MUTED, alignment=1, spaceAfter=8
)

story = []

# =========================================================================
# PÁGINA 1: CAPA VISUAL DE ALTO LUXO
# =========================================================================
capa_path = os.path.join("assets", "img", "ebook_capa_rituais.jpg")
if os.path.exists(capa_path):
    story.append(Image(capa_path, width=470, height=627))
    story.append(Spacer(1, 15))
    story.append(Paragraph("<font size=10 color='#c59b27'><b>MAHILA LUZ • EDIÇÃO ILUSTRADA DE COLECIONADOR</b></font>", ParagraphStyle('CoverSubTop', parent=cover_sub, alignment=1)))
    story.append(PageBreak())

# =========================================================================
# PÁGINA 2: INTRODUÇÃO & SUMÁRIO EXECUTIVO
# =========================================================================
story.append(Spacer(1, 10))
story.append(Paragraph("✦ ✦ ✦", cover_sub))
story.append(Spacer(1, 10))
story.append(Paragraph("O GUIA SAGRADO DOS<br/>RITUAIS LUNARES", cover_title))
story.append(Spacer(1, 6))
story.append(Paragraph("Manual Prático de Magia das 4 Fases, Banhos de Ervas, Cristais & Blindagem Energética", cover_sub))
story.append(Spacer(1, 12))
story.append(HRFlowable(width="60%", thickness=1.5, color=C_GOLD, spaceBefore=4, spaceAfter=16))

cover_card = [[
    Paragraph(
        "<b>MANUAL PRÁTICO DE PROTEÇÃO & PROSPERIDADE</b><br/><br/>"
        "A Lua é o corpo celeste mais veloz do zodíaco, governando as marés, os fluidos biológicos e as correntes invisíveis da sua mente subconsciente.<br/><br/>"
        "Quando você aprende a sincronizar seus banhos, simpatias ancestrais, limpezas com ervas e consagração de cristais com as fases lunares exatas, você para de remar contra a correnteza e passa a usar a gravidade cósmica a seu favor.<br/><br/>"
        "<i>Este e-book é o seu oráculo prático de consulta rápida para o dia a dia. Guarde no seu celular e pratique sempre que sentir sua energia pesada ou precisar de um impulso urgente de prosperidade.</i>",
        ParagraphStyle('CoverBox', parent=body, alignment=1, fontSize=9, leading=14.5, textColor=C_PRIMARY)
    )
]]
t_cover = Table(cover_card, colWidths=[450])
t_cover.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_GOLD),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 18),
    ('RIGHTPADDING', (0,0), (-1,-1), 18),
]))
story.append(t_cover)

story.append(Spacer(1, 12))
story.append(Paragraph("<b>SUMÁRIO DE RITUAIS & BANHOS:</b>", h2_style))

sumario = [
    "<b>Capítulo 1:</b> A Roda das 4 Fases Lunares e a Janela Temporal de Cada Intenção",
    "<b>Capítulo 2:</b> Banho da Lua Crescente: Magnetismo do Dinheiro, Vendas e Atração",
    "<b>Capítulo 3:</b> Banho da Lua Minguante: Quebra de Inveja, Descarrego e Limpeza Áurica",
    "<b>Capítulo 4:</b> Ritual da Lua Cheia: Consagração do Quartzo Rosa e Encantamento Afetivo",
    "<b>Capítulo 5:</b> O Caderno dos Novos Começos da Lua Nova: Decretos de Manifestação",
    "<b>Capítulo 6:</b> O Escudo Psíquico: Como Proteger Sua Casa e Seu Quarto de Energias Drenantes",
    "<b>Capítulo 7:</b> Guia de Emergência: 3 Rituais Rápidos de 2 Minutos para Dias Pesados",
    "<b>Capítulo 8:</b> As 7 Afirmações Sagradas Diárias de Blindagem Cósmica"
]
for item in sumario:
    story.append(Paragraph(f"✦  {item}", body))
    story.append(Spacer(1, 1.5))

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 1: AS 4 FASES (COM ILUSTRAÇÃO FOTOGRÁFICA)
# =========================================================================
story.append(Paragraph("Capítulo 1 • A Roda das 4 Fases Lunares", h1_style))
story.append(Paragraph(
    "A maior causa de simpatias não funcionarem é realizar o pedido na fase lunar contrária. A natureza segue um ritmo cósmico de expansão e recolhimento que deve ser honrado:",
    body
))

fases_img_path = os.path.join("assets", "img", "ebook_fases_lua.jpg")
if os.path.exists(fases_img_path):
    story.append(Spacer(1, 4))
    story.append(Image(fases_img_path, width=470, height=264))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Figura 1: A Dança Sagrada das Fases Lunares — Nova, Crescente, Cheia e Minguante.", caption_style))

fases_data = [
    [Paragraph("<b>Fase Lunar</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY)),
     Paragraph("<b>Direção Energética</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY)),
     Paragraph("<b>Melhor Tipo de Ritual</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY))],
    [Paragraph("<b>🌑 Lua Nova</b>", body), Paragraph("Início, plantio, quietude", body), Paragraph("Novos projetos, lançamentos, desapego do passado, decretos no papel.", body)],
    [Paragraph("<b>🌓 Lua Crescente</b>", body), Paragraph("Expansão, ganho, força", body), Paragraph("Dinheiro rápido, fechar contratos, atrair novos clientes, fortalecer a saúde.", body)],
    [Paragraph("<b>🌕 Lua Cheia</b>", body), Paragraph("Clímax, abundância, iluminação", body), Paragraph("Magnetismo amoroso, visibilidade pública, consagração de talismãs, intuição.", body)],
    [Paragraph("<b>🌗 Lua Minguante</b>", body), Paragraph("Eliminação, corte, banimento", body), Paragraph("Quebrar demandas, curar mágoas, cortar relações tóxicas, limpeza da casa.", body)]
]
t_fases = Table(fases_data, colWidths=[105, 145, 200])
t_fases.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#ede3f7")),
    ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_fases)

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 2: BANHO DA LUA CRESCENTE (COM ILUSTRAÇÃO DAS ERVAS)
# =========================================================================
story.append(Paragraph("Capítulo 2 • Banho da Lua Crescente: Magnetismo do Dinheiro & Fartura", h1_style))
story.append(Paragraph(
    "A Lua Crescente atua como uma lente de aumento para o mundo material. Este banho ancestral utiliza ervas nobres e solares para abrir seus caminhos financeiros:",
    body
))

altar_img_path = os.path.join("assets", "img", "ebook_altar_ervas.jpg")
if os.path.exists(altar_img_path):
    story.append(Spacer(1, 4))
    story.append(Image(altar_img_path, width=470, height=264))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Figura 2: Altar de Ativação — Canela, Louro, Alecrim, Cristais de Quartzo e Sal Rosa Ancestral.", caption_style))

card_crescente = [[
    Paragraph(
        "<b>RECEITA DO BANHO DE OURO & EXPANSÃO:</b><br/><br/>"
        "• <b>Ingredientes:</b> 3 paus de canela, 7 folhas de louro secas e 1 ramo de alecrim fresco (ou 1 colher de sopa seco).<br/>"
        "• <b>Água:</b> 1,5 litro de água mineral ou filtrada.<br/><br/>"
        "<b>Modo de Preparo:</b><br/>"
        "1. Ferva a água. Ao levantar fervura, desligue o fogo imediatamente.<br/>"
        "2. Adicione o louro, a canela e o alecrim. Tampe com um prato e deixe abafado por 20 minutos.<br/>"
        "3. Coe as ervas (pode devolver à natureza em um jardim ou vaso).<br/>"
        "4. Tome seu banho de higiene normal. Em seguida, despeje a infusão morna <b>do pescoço para baixo</b>.<br/>"
        "5. Enquanto a água escorre, mentalize com vivacidade o dinheiro entrando na sua conta bancária e pronuncie a oração:<br/><br/>"
        "<i>'Pela força da Lua Crescente e pelo calor da canela e do louro, eu abro todos os portais da fartura. A riqueza me procura, o dinheiro permanece comigo e a prosperidade transborda na minha vida. Que assim seja.'</i><br/><br/>"
        "<i>Dica de Ouro:</i> Deixe o corpo secar naturalmente, sem esfregar a toalha com força.",
        card_body
    )
]]
t_crescente = Table(card_crescente, colWidths=[450])
t_crescente.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fffdf5")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#e5c368")),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_crescente)

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 3: BANHO DA LUA MINGUANTE (DESCARREGO)
# =========================================================================
story.append(Paragraph("Capítulo 3 • Banho da Lua Minguante: Quebra de Demandas & Olho Gordo", h1_style))
story.append(Paragraph(
    "Quando você sente cansaço inexplicável, peso nos ombros ou bocejos frequentes após conversar com certas pessoas, seu campo áurico foi sobrecarregado por miasmas e inveja. A Lua Minguante é o período cirúrgico para extirpar essas cargas:",
    body
))

card_minguante = [[
    Paragraph(
        "<b>RECEITA DO BANHO DE DESCARREGO & CORTE:</b><br/><br/>"
        "• <b>Ingredientes:</b> 1 punhado de sal grosso (ou sal marinho), 1 punhado de folhas de guiné (ou arruda) e casca de 1 alho.<br/>"
        "• <b>Água:</b> 2 litros de água morna.<br/><br/>"
        "<b>Como Fazer:</b><br/>"
        "1. Ferva a água com as ervas e o sal por 3 minutos. Desligue e deixe amornar até uma temperatura agradável.<br/>"
        "2. Tome seu banho comum de chuveiro para limpar as impurezas físicas.<br/>"
        "3. Despeje o banho de descarrego <b>SEMPRE do pescoço para baixo</b> (nunca jogue sal grosso no topo da cabeça, onde fica o Chakra Coronário).<br/>"
        "4. Mentalize uma fumaça cinzenta sendo arrancada dos seus ombros, do seu peito e das suas costas, sendo sugada pelo ralo.<br/>"
        "5. Diga em voz firme: <i>'Toda inveja, mau-olhado, feitiço, palavra maldita e pensamento denso são desfeitos agora pela força da Lua Minguante. Meu corpo é templo fechado.'</i><br/><br/>"
        "<b>Importante (O Reequilíbrio):</b> Como o sal grosso limpa tanto a energia ruim quanto a boa, tome uma xícara de chá de camomila logo após o banho para selar sua aura com serenidade.",
        card_body
    )
]]
t_minguante = Table(card_minguante, colWidths=[450])
t_minguante.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f6f3fa")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#9b8bb5")),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_minguante)

story.append(Spacer(1, 10))

# =========================================================================
# CAPÍTULO 4: RITUAL DA LUA CHEIA (AMOR)
# =========================================================================
story.append(Paragraph("Capítulo 4 • Ritual da Lua Cheia: O Encanto de Vênus & Magnetismo Pessoal", h1_style))
story.append(Paragraph(
    "A Lua Cheia potencializa em dez vezes o poder do elemento Água e a irradiação de Vênus. Este ritual serve tanto para quem busca atrair um novo amor de alma quanto para quem deseja reacender o fogo e o carinho em um relacionamento já existente:",
    body
))

card_amor = [[
    Paragraph(
        "<b>CONSAGRAÇÃO DO CRISTAL DE QUARTZO ROSA:</b><br/><br/>"
        "• <b>Material:</b> 1 pedra de Quartzo Rosa bruta ou rolada, 1 taça de água mineral com 3 gotas de mel e pétalas de 1 rosa cor-de-rosa.<br/><br/>"
        "<b>O Passo a Passo sob a Luz da Lua:</b><br/>"
        "1. Na primeira noite de Lua Cheia, coloque a taça com água, o mel e as pétalas próximo à janela ou em local onde a luz lunar incida diretamente.<br/>"
        "2. Coloque o quartzo rosa imerso nessa taça e deixe pernoitar absorvendo os raios lunares.<br/>"
        "3. Na manhã seguinte, retire o cristal. Ele agora é um <b>ímã de doçura e afeto</b>.<br/>"
        "4. Carregue o quartzo rosa dentro da bolsa ou deixe na sua cabeceira da cama. A água com pétalas pode ser usada para borrifar nos lençóis.",
        card_body
    )
]]
t_amor = Table(card_amor, colWidths=[450])
t_amor.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fdf5f7")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#d88c9d")),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_amor)

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 5: O CADERNO DA LUA NOVA
# =========================================================================
story.append(Paragraph("Capítulo 5 • O Caderno da Lua Nova: Decretos de Manifestação", h1_style))
story.append(Paragraph(
    "A Lua Nova é o útero da criação. Nada se vê no céu, mas todas as sementes estão sob a terra se preparando para brotar. Este é o momento mais forte para lançar intenções materiais ao Universo:",
    body
))

card_nova = [[
    Paragraph(
        "<b>O MÉTODO DOS 7 DESEJOS ESCRITOS:</b><br/><br/>"
        "1. Separe um caderno exclusivo ou uma folha em branco (sem pautas). Use caneta azul ou preta.<br/>"
        "2. Escreva 7 decretos sempre no tempo <b>PRESENTE</b> e com gratidão antecipada, como se já fossem reais:<br/>"
        "   • <i>Exemplo errado:</i> 'Quero conseguir pagar minhas dívidas.'<br/>"
        "   • <i>Exemplo correto:</i> 'Eu sou imensamente grata pela multiplicação dos meus ganhos e pela tranquilidade financeira que desfruto agora.'<br/>"
        "3. Dobre o papel três vezes em sua direção (trazendo a energia para si).<br/>"
        "4. Guarde o papel embaixo de uma pedra de Pirita ou dentro de um livro sagrado até a próxima Lua Cheia.",
        card_body
    )
]]
t_nova = Table(card_nova, colWidths=[450])
t_nova.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_BORDER),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_nova)

story.append(Spacer(1, 10))

# =========================================================================
# CAPÍTULO 6: O ESCUDO PSÍQUICO DA CASA
# =========================================================================
story.append(Paragraph("Capítulo 6 • O Escudo Psíquico: Proteção do Lar e do Quarto", h1_style))
story.append(Paragraph(
    "Sua casa é o seu templo de recarga. Se a sua casa absorver miasmas de visitas pesadas, brigas ou vizinhança tóxica, você nunca acordará com disposição:",
    body
))

card_casa = [[
    Paragraph(
        "<b>AS DUAS ÂNCORAS DE PROTEÇÃO DA PORTA DE ENTRADA:</b><br/><br/>"
        "<b>1. O Copo Testemunha de Sal e Vinagre:</b><br/>"
        "Coloque atrás da porta de entrada principal um copo de vidro transparente com 2 dedos de sal grosso e cubra até a metade com vinagre de álcool. Se o sal começar a transbordar ou criar crostas bizarras para fora do copo, ele absorveu uma carga pesada direcionada ao seu lar. Despeje no vaso sanitário, dê descarga e refaça imediatamente.<br/><br/>"
        "<b>2. A Turmalina Negra na Entrada:</b><br/>"
        "Mantenha um cristal de Turmalina Negra próximo à soleira da porta. Ela atua como um para-raios etérico que neutraliza olhares invejosos antes que entrem no corredor.",
        card_body
    )
]]
t_casa = Table(card_casa, colWidths=[450])
t_casa.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fbf9fe")),
    ('BOX', (0,0), (-1,-1), 1, C_BORDER),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_casa)

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 7: RITUAIS DE EMERGÊNCIA
# =========================================================================
story.append(Paragraph("Capítulo 7 • Guia de Emergência: 3 Rituais de 2 Minutos", h1_style))
story.append(Paragraph(
    "Para aqueles dias em que você não tem tempo de ferver ervas e precisa de alívio instantâneo antes de uma reunião, prova ou encontro:",
    body
))

card_emergencia = [[
    Paragraph(
        "<b>1. A Lavagem dos Pulsos com Sal Fino:</b><br/>"
        "Vá até a pia do banheiro. Pegue uma pitada de sal fino, esfregue nos dois pulsos (onde pulsam as artérias e cruzam meridianos de energia) em movimentos circulares sob a torneira ligada. Mentalize que todo peso que você absorveu de outras pessoas no dia de hoje está indo pelo cano.<br/><br/>"
        "<b>2. O Selamento do Umbigo:</b><br/>"
        "Quando for a locais de energia sabidamente densa (hospitais, velórios, fóruns ou reuniões com pessoas invejosas), coloque um pedaço pequeno de fita adesiva (micropore) cobrindo seu umbigo. O Plexo Solar é o portal por onde mais 'engolimos' energias externas.<br/><br/>"
        "<b>3. A Defumação Expressa com Folha de Louro Seca:</b><br/>"
        "Acenda uma única folha de louro seca com um fósforo dentro de um prato. Deixe a fumaça perfumada espalhar pelo quarto. O aroma do louro queima larvas astrais e acalma a mente em menos de 60 segundos.",
        card_body
    )
]]
t_emergencia = Table(card_emergencia, colWidths=[450])
t_emergencia.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fffdf5")),
    ('BOX', (0,0), (-1,-1), 1, C_GOLD),
    ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_emergencia)

story.append(Spacer(1, 10))

# =========================================================================
# CAPÍTULO 8: AS 7 AFIRMAÇÕES SAGRADAS DIÁRIAS
# =========================================================================
story.append(Paragraph("Capítulo 8 • As 7 Afirmações Sagradas Diárias de Blindagem", h1_style))
story.append(Paragraph(
    "A palavra falada com convicção reorganiza a frequência da sua água interna. Repita estas afirmações ao acordar ou antes de dormir:",
    body
))

afirmacoes = [
    "<b>1.</b> 'Eu sou uma fortaleza impenetrável à inveja, à maldade e às baixas vibrações alheias.'",
    "<b>2.</b> 'A luz da Lua clareia meu discernimento e me afasta de ciladas visíveis e invisíveis.'",
    "<b>3.</b> 'Minha mente está ancorada na certeza de que o Universo conspira a meu favor a cada respiração.'",
    "<b>4.</b> 'Eu devolvo à terra tudo o que não me pertence, e recebo do céu toda bênção que me é de direito.'",
    "<b>5.</b> 'O dinheiro é uma corrente limpa e sagrada que flui até mim com naturalidade, facilidade e constância.'",
    "<b>6.</b> 'Minha energia pessoal é magnética, pura e blindada. Quem chega perto de mim sente paz.'",
    "<b>7.</b> 'Está feito, está selado, está protegido pelo poder cósmico que rege as estrelas.'"
]

afirm_card = []
for a in afirmacoes:
    afirm_card.append([Paragraph(f"✦  {a}", body)])

t_afirm = Table(afirm_card, colWidths=[450])
t_afirm.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_BORDER),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#f0e8f7")),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
]))
story.append(t_afirm)

story.append(Spacer(1, 15))
story.append(Paragraph("✦ <i>Que a sabedoria das estrelas e o manto de Mahila Luz iluminem cada passo da sua jornada.</i> ✦", ParagraphStyle('Final', parent=body, alignment=1, fontName='Helvetica-Oblique', textColor=C_GOLD)))

doc.build(story, canvasmaker=NumberedCanvas)
print(f"E-book ilustrado de luxo gerado com sucesso: {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.1f} KB)")
