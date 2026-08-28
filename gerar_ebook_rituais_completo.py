import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle
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
            return  # Não desenha header/footer na capa

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
        self.drawString(45, 32, "Conteúdo de Proteção Espiritual e Autoconhecimento • Todos os direitos reservados")
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
    fontName='Helvetica-Bold', fontSize=25, leading=31,
    textColor=C_PRIMARY, alignment=1
)
cover_sub = ParagraphStyle(
    'CoverSub', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=12, leading=17,
    textColor=C_GOLD, alignment=1
)
author_style = ParagraphStyle(
    'CoverAuthor', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=11, leading=15,
    textColor=C_ROSE, alignment=1
)
h1_style = ParagraphStyle(
    'H1', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=16, leading=21,
    textColor=C_PRIMARY, spaceBefore=12, spaceAfter=8
)
h2_style = ParagraphStyle(
    'H2', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=12, leading=16,
    textColor=C_GOLD, spaceBefore=8, spaceAfter=4
)
body = ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontName='Helvetica', fontSize=9.5, leading=14.5,
    textColor=C_TEXT, spaceAfter=7
)
card_body = ParagraphStyle(
    'CardBody', parent=styles['Normal'],
    fontName='Helvetica', fontSize=9, leading=13.5,
    textColor=C_PRIMARY
)

story = []

# =========================================================================
# CAPA
# =========================================================================
story.append(Spacer(1, 35))
story.append(Paragraph("✦ ✦ ✦", cover_sub))
story.append(Spacer(1, 15))
story.append(Paragraph("O GUIA SAGRADO DOS<br/>RITUAIS LUNARES", cover_title))
story.append(Spacer(1, 10))
story.append(Paragraph("Manual Prático de Magia das 4 Fases, Banhos de Ervas, Cristais & Blindagem Energética", cover_sub))
story.append(Spacer(1, 20))
story.append(HRFlowable(width="50%", thickness=1.5, color=C_GOLD, spaceBefore=8, spaceAfter=22))

cover_card = [[
    Paragraph(
        "<b>MANUAL PRÁTICO DE PROTEÇÃO & PROSPERIDADE</b><br/><br/>"
        "A Lua é o corpo celeste mais veloz do zodíaco, governando as marés, os fluidos biológicos e as correntes invisíveis da sua mente subconsciente.<br/><br/>"
        "Quando você aprende a sincronizar seus banhos, simpatias ancestrais, limpezas com ervas e consagração de cristais com as fases lunares exatas, você para de remar contra a correnteza e passa a usar a gravidade cósmica a seu favor.<br/><br/>"
        "<i>Este e-book é o seu oráculo prático de consulta rápida para o dia a dia. Guarde no seu celular e pratique sempre que sentir sua energia pesada ou precisar de um impulso urgente de prosperidade.</i>",
        ParagraphStyle('CoverBox', parent=body, alignment=1, fontSize=9.5, leading=15, textColor=C_PRIMARY)
    )
]]
t_cover = Table(cover_card, colWidths=[430])
t_cover.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_GOLD),
    ('ROUNDEDCORNERS', [12, 12, 12, 12]),
    ('TOPPADDING', (0,0), (-1,-1), 20),
    ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ('LEFTPADDING', (0,0), (-1,-1), 22),
    ('RIGHTPADDING', (0,0), (-1,-1), 22),
]))
story.append(t_cover)

story.append(Spacer(1, 60))
story.append(Paragraph("Canalizado e Organizado por <b>Mahila Luz</b>", author_style))
story.append(Spacer(1, 4))
story.append(Paragraph("Material Exclusivo para Compradores • Versão Digital Registrada", ParagraphStyle('SubSub', parent=body, alignment=1, fontSize=8.5, textColor=C_MUTED)))

story.append(PageBreak())

# =========================================================================
# ÍNDICE & APRESENTAÇÃO
# =========================================================================
story.append(Paragraph("Como Usar Este Manual Sagrado", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=C_GOLD, spaceBefore=4, spaceAfter=12))

story.append(Paragraph(
    "Bem-vindo(a) ao seu círculo íntimo de práticas lunares. Você não precisa de anos de estudo em ocultismo nem de ingredientes caros e inacessíveis para manifestar proteção e fartura. Os maiores mistérios da natureza funcionam pela simplicidade, pelo respeito às leis planetárias e pela sua <b>intenção focada</b>.",
    body
))
story.append(Paragraph(
    "Neste manual, cada ritual foi estruturado em passos claros: o momento lunar ideal, a lista exata de elementos fáceis de encontrar em qualquer feira ou mercado, o modo de preparo e a oração de ativação cósmica.",
    body
))

story.append(Spacer(1, 8))
story.append(Paragraph("<b>SUMÁRIO DE RITUAIS:</b>", h2_style))

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
    story.append(Spacer(1, 2))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_BORDER, spaceBefore=6, spaceAfter=14))

# =========================================================================
# CAPÍTULO 1: AS 4 FASES
# =========================================================================
story.append(Paragraph("Capítulo 1 • A Roda das 4 Fases Lunares", h1_style))
story.append(Paragraph(
    "A maior causa de feitiços e simpatias não funcionarem é realizar o pedido na fase lunar contrária. A natureza segue um ritmo de expiração e inspiração que você deve sempre respeitar:",
    body
))

fases_data = [
    [Paragraph("<b>Fase Lunar</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY)),
     Paragraph("<b>Direção Energética</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY)),
     Paragraph("<b>Melhor Tipo de Ritual</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY))],
    [Paragraph("<b>🌑 Lua Nova</b>", body), Paragraph("Início, plantio, quietude", body), Paragraph("Novos projetos, lançamentos, desapego do passado, decretos no papel.", body)],
    [Paragraph("<b>🌓 Lua Crescente</b>", body), Paragraph("Expansão, ganho, força", body), Paragraph("Dinheiro rápido, fechar contratos, atrair novos clientes, fortalecer a saúde.", body)],
    [Paragraph("<b>🌕 Lua Cheia</b>", body), Paragraph("Clímax, abundância, iluminação", body), Paragraph("Magnetismo amoroso, visibilidade pública, consagração de talismãs, intuição.", body)],
    [Paragraph("<b>🌗 Lua Minguante</b>", body), Paragraph("Eliminação, corte, banimento", body), Paragraph("Quebrar demandas, curar mágoas, cortar relações tóxicas, limpeza da casa.", body)]
]
t_fases = Table(fases_data, colWidths=[100, 140, 190])
t_fases.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#ede3f7")),
    ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_fases)

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 2: BANHO DA LUA CRESCENTE (PROSPERIDADE)
# =========================================================================
story.append(Paragraph("Capítulo 2 • Banho da Lua Crescente: Magnetismo do Dinheiro & Fartura", h1_style))
story.append(Paragraph(
    "A Lua Crescente atua como uma lente de aumento para a matéria. Este banho ancestral utiliza três ervas solares e condutoras para abrir seus caminhos financeiros e atrair oportunidades de ganho rápido:",
    body
))

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
t_crescente = Table(card_crescente, colWidths=[430])
t_crescente.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_GOLD),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_crescente)

story.append(Spacer(1, 14))

# =========================================================================
# CAPÍTULO 3: BANHO DA LUA MINGUANTE (LIMPEZA & QUEBRA DE INVEJA)
# =========================================================================
story.append(Paragraph("Capítulo 3 • Banho da Lua Minguante: Descarrego e Quebra de Olho Gordo", h1_style))
story.append(Paragraph(
    "Quando você sente o corpo pesado, sono excessivo sem motivo médico, dores na nuca ou sensação de bloqueio onde nada avança, o seu campo áurico acumulou miasmas e inveja alheia. Este é o banho de faxina pesada mais eficaz da tradição:",
    body
))

card_minguante = [[
    Paragraph(
        "<b>BANHO DE CORTE DAS 3 CHAVES SAGRADAS:</b><br/><br/>"
        "• <b>Ingredientes:</b> 1 punhado de sal grosso (3 colheres de sopa), 7 folhas de arruda e 1 ramo de manjericão.<br/>"
        "• <b>Fase:</b> Exclusivamente durante a Lua Minguante, no final da tarde ou à noite antes de dormir.<br/><br/>"
        "<b>Passo a Passo da Limpeza:</b><br/>"
        "1. Ferva 1,5L de água, desligue o fogo e misture o sal grosso até dissolver completamente.<br/>"
        "2. Adicione a arruda e o manjericão. Macere levemente as folhas com as próprias mãos na água para soltar o sumo verde.<br/>"
        "3. Deixe amornar. Tome seu banho comum e, em seguida, jogue o banho de ervas <b>rigorosamente do pescoço para baixo</b> (nunca jogue sal grosso no topo da cabeça).<br/>"
        "4. Mentalize uma fumaça cinzenta saindo dos seus ombros e sendo dissolvida pelo ralo da água, afirmando:<br/><br/>"
        "<i>'Toda energia densa, todo olhar de inveja, todo pensamento de inveja ou demanda direcionado a mim e à minha família minguam agora com a força desta Lua. Minha aura se fecha para o mal e se abre para a luz divina.'</i>",
        card_body
    )
]]
t_minguante = Table(card_minguante, colWidths=[430])
t_minguante.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f4f6fa")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#4b5563")),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_minguante)

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 4: RITUAL DA LUA CHEIA (MAGNETISMO & AMOR)
# =========================================================================
story.append(Paragraph("Capítulo 4 • O Ritual de Encantamento & Amor da Lua Cheia", h1_style))
story.append(Paragraph(
    "A Lua Cheia é o pico absoluto da energia eletromagnética. Ela ilumina os desejos ocultos e potencializa o magnetismo do Chakra Cardíaco. Este ritual é destinado a quem busca atrair um novo amor sincero ou reacender a paixão em uma relação existente:",
    body
))

card_cheia = [[
    Paragraph(
        "<b>RITUAL DA TAÇA DE AFRODITE:</b><br/><br/>"
        "• <b>Elementos:</b> 1 taça ou copo de vidro transparente com água, 1 cristal de Quartzo Rosa e pétalas de 1 rosa cor-de-rosa ou vermelha.<br/>"
        "• <b>Horário:</b> À noite, preferencialmente sob a luz visível da Lua Cheia (pode ser na janela).<br/><br/>"
        "<b>Procedimento:</b><br/>"
        "1. Coloque o quartzo rosa no fundo da taça com água e cubra com as pétalas de rosa fresca.<br/>"
        "2. Deixe a taça no parapeito da janela ou varanda recebendo o brilho da Lua Cheia por pelo menos 3 horas (ou durante a noite inteira).<br/>"
        "3. Pela manhã, retire o quartzo rosa (ele agora é o seu amuleto de bolso para levar na bolsa).<br/>"
        "4. Lave o rosto com a água energizada e passe algumas gotas nos pulsos e atrás das orelhas.<br/>"
        "5. O aroma sutil e a carga de Vênus aumentam o seu brilho pessoal, fazendo com que as pessoas notem sua presença com carinho e admiração instantânea.",
        card_body
    )
]]
t_cheia = Table(card_cheia, colWidths=[430])
t_cheia.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fcf4f6")),
    ('BOX', (0,0), (-1,-1), 1, C_ROSE),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_cheia)

story.append(Spacer(1, 14))

# =========================================================================
# CAPÍTULO 5: O ESCUDO PSÍQUICO DA CASA
# =========================================================================
story.append(Paragraph("Capítulo 5 • O Escudo Psíquico: Protegendo Sua Casa de Pessoas Pesadas", h1_style))
story.append(Paragraph(
    "Muitas vezes você está bem, mas ao receber uma visita negativa em casa ou morar com pessoas que reclamam sem parar, a atmosfera do seu lar adoece. Aqui está o segredo das antigas parteiras e benzedeiras:",
    body
))

story.append(Paragraph(
    "<b>1. O Filtro do Copo de Sal Grosso atrás da Porta:</b><br/>"
    "Coloque um copo americano com 2 dedos de sal grosso e água até a metade logo atrás da porta de entrada principal da casa. O sal funciona como um polo de atração que absorve a estática energética de quem pisa na soleira. Troque a água e o sal a cada 15 dias jogando no vaso sanitário.",
    body
))
story.append(Paragraph(
    "<b>2. Defumação Instantânea de Alecrim e Louro no Fogão:</b><br/>"
    "Não precisa de incensário complicado. Em uma frigideira velha ou panela de ferro, coloque 3 folhas de louro seco e 1 colher de alecrim. Ligue o fogo baixo até começar a soltar uma fumaça aromática branca. Caminhe com a frigideira pelos cômodos da casa, do fundo para a porta de entrada, com as janelas abertas. A sensação de alívio e leveza no ar é imediata.",
    body
))

story.append(PageBreak())

# =========================================================================
# CAPÍTULO 6: AS 7 AFIRMAÇÕES DE PODER DIÁRIO
# =========================================================================
story.append(Paragraph("Capítulo 6 • As 7 Afirmações Sagradas de Blindagem Cósmica", h1_style))
story.append(Paragraph(
    "A palavra falada com convicção emocional é a ferramenta mágica mais potente do ser humano. Pronuncie estas 7 afirmações ao acordar ou antes de sair de casa para criar um manto de invisibilidade contra a inveja e o azar:",
    body
))

afirmacoes = [
    "<b>1. Escudo da Manhã:</b> 'Meu corpo é templo da luz. Nenhuma energia intrusa, olho gordo ou feitiço tem permissão de tocar a minha aura hoje.'",
    "<b>2. Ouro & Abundância:</b> 'Eu honro o trabalho e a criação. O dinheiro chega até mim por múltiplos canais lícitos, pacíficos e abundantes.'",
    "<b>3. Paz Mental:</b> 'Eu não absorvo a ansiedade, a pressa e os julgamentos dos outros. Eu permaneço soberano(a) no meu centro.'",
    "<b>4. Discernimento de Pessoas:</b> 'Meus olhos espirituais enxergam a verdade por trás das máscaras. Eu me afasto do que é falso e me aproximo do que é sagrado.'",
    "<b>5. Cura Cardíaca:</b> 'Eu perdoo o passado e retiro todas as minhas expectativas dos ombros de quem não soube me valorizar.'",
    "<b>6. Atração Nobre:</b> 'A minha vibração é magnética e pura. Eu atraio pessoas leais, de caráter elevado e com intenções honestas.'",
    "<b>7. Decreto Final de Fechamento:</b> 'O que Deus uniu e os astros abençoaram em mim, nada e ninguém tem poder de desestabilizar. Está selado, blindado e consagrado.'"
]

for af in afirmacoes:
    card_af = [[Paragraph(af, ParagraphStyle('AfText', parent=body, fontSize=9.5, leading=14, textColor=C_PRIMARY))]]
    t_af = Table(card_af, colWidths=[430])
    t_af.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_af)
    story.append(Spacer(1, 6))

story.append(Spacer(1, 20))
story.append(HRFlowable(width="100%", thickness=1, color=C_GOLD, spaceBefore=10, spaceAfter=14))
story.append(Paragraph(
    "<b>✦ Benção Final de Mahila Luz:</b><br/>"
    "Que a sabedoria das estrelas ilumine seus passos nos dias de escuridão e que a força da Lua renove sua fé a cada novo ciclo. Guarde este livro e compartilhe sua luz apenas com quem sabe honrar a sua presença.",
    ParagraphStyle('FinalBless', parent=body, alignment=1, fontSize=9.5, leading=15, textColor=C_PRIMARY)
))

doc.build(story, canvasmaker=NumberedCanvas)
print(f"E-book completo gerado: {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.1f} KB)")
