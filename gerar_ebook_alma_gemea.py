import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle
from reportlab.pdfgen import canvas

pdf_filename = "O_Mapa_da_Alma_Gemea_Mahila_Luz.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=45,
    rightMargin=45,
    topMargin=50,
    bottomMargin=50
)

# Paleta de Cores Místicas & Sofisticadas
C_PRIMARY = colors.HexColor("#1b1038")
C_GOLD = colors.HexColor("#c59b27")
C_ROSE = colors.HexColor("#9b3c5a")
C_TEXT = colors.HexColor("#2d2738")
C_MUTED = colors.HexColor("#645979")
C_BG_CARD = colors.HexColor("#f8f5fa")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CoverTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=26,
    leading=32,
    textColor=C_PRIMARY,
    alignment=1
)

subtitle_style = ParagraphStyle(
    'CoverSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=13,
    leading=18,
    textColor=C_GOLD,
    alignment=1
)

author_style = ParagraphStyle(
    'CoverAuthor',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=C_ROSE,
    alignment=1
)

h1_style = ParagraphStyle(
    'ChapterH1',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=17,
    leading=22,
    textColor=C_PRIMARY,
    spaceBefore=14,
    spaceAfter=8
)

h2_style = ParagraphStyle(
    'SectionH2',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=C_GOLD,
    spaceBefore=10,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'BodyDark',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=15,
    textColor=C_TEXT,
    spaceAfter=8
)

box_style = ParagraphStyle(
    'BoxText',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9.5,
    leading=14,
    textColor=C_PRIMARY
)

story = []

# --- CAPA ---
story.append(Spacer(1, 40))
story.append(Paragraph("✦ ✦ ✦", subtitle_style))
story.append(Spacer(1, 15))
story.append(Paragraph("O MAPA DA ALMA GÊMEA", title_style))
story.append(Spacer(1, 10))
story.append(Paragraph("O Guia Definitivo de Vênus, Casa 7 & Sinastria Cósmica", subtitle_style))
story.append(Spacer(1, 25))
story.append(HRFlowable(width="60%", thickness=1.5, color=C_GOLD, spaceBefore=10, spaceAfter=25))

cover_card_data = [[
    Paragraph(
        "<b>LEITURA EXCLUSIVA DE MAGNETISMO AFETIVO</b><br/><br/>"
        "Este guia sagrado foi codificado para revelar as forças cósmicas invisíveis que regem os seus encontros amorosos. "
        "Aqui você descobrirá o arquétipo do seu parceiro destinado, como desativar os nós cármicos de dor e o momento astrológico propício para a união de almas.",
        ParagraphStyle('CoverBox', parent=body_style, alignment=1, fontSize=10.5, leading=16, textColor=C_PRIMARY)
    )
]]
cover_table = Table(cover_card_data, colWidths=[420])
cover_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_BG_CARD),
    ('BOX', (0,0), (-1,-1), 1, C_GOLD),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 22),
    ('BOTTOMPADDING', (0,0), (-1,-1), 22),
    ('LEFTPADDING', (0,0), (-1,-1), 24),
    ('RIGHTPADDING', (0,0), (-1,-1), 24),
]))
story.append(cover_table)

story.append(Spacer(1, 80))
story.append(Paragraph("Por Mahila Luz", author_style))
story.append(Spacer(1, 4))
story.append(Paragraph("Canalização Astrológica e Terapêutica Integrada", ParagraphStyle('SubAut', parent=body_style, alignment=1, fontSize=9, textColor=C_MUTED)))

story.append(PageBreak())

# --- ÍNDICE ---
story.append(Paragraph("Índice dos Capítulos", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=C_GOLD, spaceBefore=4, spaceAfter=14))

index_items = [
    "<b>Capítulo 1:</b> A Diferença entre Amor Cármico e Encontro de Almas",
    "<b>Capítulo 2:</b> O Código de Vênus: Seu Magnetismo Natural e Linguagem de Afeto",
    "<b>Capítulo 3:</b> A Casa 7: O Espelho Cósmico do Seu Parceiro Ideal",
    "<b>Capítulo 4:</b> Sinastria Prática: A Dança dos Elementos na Intimidade",
    "<b>Capítulo 5:</b> Como Quebrar os 3 Padrões Repetitivos de Decepção",
    "<b>Capítulo 6:</b> A Janela Astral: Quando os Portais de Encontro se Abrem",
    "<b>Capítulo 7:</b> O Ritual Sagrado de Magnetismo com Quartzo Rosa e Afirmação Diária"
]
for item in index_items:
    story.append(Paragraph(f"✦  {item}", body_style))
    story.append(Spacer(1, 4))

story.append(Spacer(1, 15))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_MUTED, spaceBefore=8, spaceAfter=18))

# --- CAPÍTULO 1 ---
story.append(Paragraph("Capítulo 1 • A Diferença entre Amor Cármico e Encontro de Almas", h1_style))
story.append(Paragraph(
    "Muitas pessoas confundem uma atração avassaladora com a presença de uma Alma Gêmea. Na sabedoria ancestral, relações marcadas por ansiedade constante, sensação de montanha-russa emocional e medo de rejeição são, na verdade, <b>ligações cármicas</b>. Elas surgem não para trazer paz duradoura, mas para forçar uma cura interna acelerada.",
    body_style
))
story.append(Paragraph(
    "O verdadeiro <b>Encontro de Almas</b> possui uma assinatura vibratória diferente: a sensação primordial não é de euforia desmedida, mas de <i>reconhecimento e serenidade</i>. A presença da outra pessoa parece familiar, e mesmo nos desentendimentos normais da convivência, existe uma base sólida de respeito onde você não precisa se diminuir para caber no mundo do outro.",
    body_style
))

# --- CAPÍTULO 2 ---
story.append(Spacer(1, 10))
story.append(Paragraph("Capítulo 2 • O Código de Vênus: Seu Magnetismo Natural", h1_style))
story.append(Paragraph(
    "Vênus no seu mapa astral governa aquilo que você valoriza, a sua postura de atração magnética e como você nutre o romance. Compreender o elemento da sua Vênus é a chave mestra para parar de forçar relacionamentos e deixar que o magnetismo correto atue:",
    body_style
))
story.append(Paragraph(
    "• <b>Vênus em Fogo (Áries, Leão, Sagitário):</b> Magnetismo radiante e direto. Atrai pela coragem e paixão viva. Precisa de admiração mútua e entusiasmo constante.<br/>"
    "• <b>Vênus em Terra (Touro, Virgem, Capricórnio):</b> Magnetismo sólido e sensual. Atrai pela presença confiável e elegância sutil. O amor é construído em atos de cuidado e estabilidade.<br/>"
    "• <b>Vênus em Ar (Gêmeos, Libra, Aquário):</b> Magnetismo intelectual e charmoso. A conexão nasce da conversa, da troca de ideias e do respeito mútuo à liberdade individual.<br/>"
    "• <b>Vênus em Água (Câncer, Escorpião, Peixes):</b> Magnetismo profundo e intuitivo. Conexão que transcende o plano físico. Busca cumplicidade de alma e entrega emocional autêntica.",
    body_style
))

story.append(PageBreak())

# --- CAPÍTULO 3 ---
story.append(Paragraph("Capítulo 3 • A Casa 7: O Espelho Cósmico do Parceiro", h1_style))
story.append(Paragraph(
    "Se o seu Ascendente (Casa 1) é a sua máscara pessoal e a forma como você se apresenta ao mundo, a <b>Casa 7 (o Descendente)</b> representa exatamente aquilo que você inconscientemente procura em um companheiro para encontrar equilíbrio de vida.",
    body_style
))
story.append(Paragraph(
    "É na Casa 7 que residem as qualidades que você tem dificuldade de expressar sozinho, e que por isso mesmo se tornam tão hipnóticas quando vistas no outro. Por exemplo, quem tem Descendente em Libra busca harmonia e tato social; quem tem Descendente em Áries é atraído por pessoas de atitude firme e assertividade protetora.",
    body_style
))

# --- CAPÍTULO 4 & 5 ---
story.append(Spacer(1, 10))
story.append(Paragraph("Capítulo 4 • Quebrando os 3 Padrões Repetitivos de Decepção", h1_style))
story.append(Paragraph(
    "Quando nos deparamos sempre com o mesmo tipo de problema amoroso (pessoas emocionalmente indisponíveis, parceiros controladores ou relacionamentos mornos), estamos operando sob uma ferida astrológica inconsciente. Aqui estão as 3 armadilhas mais comuns e como superá-las:",
    body_style
))
story.append(Paragraph(
    "<b>1. A Armadilha do Salvamento:</b> Acreditar que o seu amor pode transformar ou curar alguém que não quer mudar a si mesmo. <i>Cura:</i> Estabeleça limites firmes logo nas primeiras semanas de conversa.<br/>"
    "<b>2. O Medo da Rejeição Mascarado de Independência:</b> Afastar pretendentes de valor por medo secreto de ficar vulnerável. <i>Cura:</i> Permita-se ser cuidada e acolhida sem medo de perder sua autonomia.<br/>"
    "<b>3. A Pressa do Destino:</b> Querer garantias imediatas antes mesmo de conhecer o caráter real da pessoa. <i>Cura:</i> A calma é o maior filtro de relacionamentos duradouros.",
    body_style
))

# --- CAPÍTULO 6 ---
story.append(Spacer(1, 10))
story.append(Paragraph("Capítulo 5 • A Janela Astral: Quando os Portais se Abrem", h1_style))
story.append(Paragraph(
    "Os encontros predestinados raramente acontecem ao acaso. Eles coincidem com grandes trânsitos cósmicos no seu mapa: passagens de <b>Júpiter sobre o seu Sol ou Casa 7</b> (expansão do coração), o retorno dos <b>Nódulos Lunares</b> (realinhamento de propósito) ou eclipses sobre o eixo 1-7. Quando esses portais se abrem, é fundamental estar socialmente receptivo e em alta vibração interna.",
    body_style
))

# --- CAPÍTULO 7 & RITUAL ---
story.append(Spacer(1, 10))
story.append(Paragraph("Capítulo 6 • O Ritual Sagrado de Magnetismo Afetivo", h1_style))
story.append(Paragraph(
    "Para ancorar a energia da Alma Gêmea no plano físico, realize este ritual em uma noite de <b>Lua Nova ou Lua Crescente</b>, preferencialmente em uma sexta-feira (dia governado por Vênus):",
    body_style
))

ritual_card_data = [[
    Paragraph(
        "<b>RITUAL DA CHAMA DE VÊNUS:</b><br/><br/>"
        "<b>Elemento:</b> 1 Vela rosa ou branca e 1 pedra de Quartzo Rosa.<br/>"
        "<b>Passo 1:</b> Segure o cristal entre as mãos na altura do peito e respire fundo por 7 vezes, acalmando os batimentos cardíacos.<br/>"
        "<b>Passo 2:</b> Acenda a vela e mentalize não um rosto, mas a <i>sensação de segurança, amor leve e carinho profundo</i> que você deseja viver todos os dias.<br/>"
        "<b>Passo 3:</b> Pronuncie a Afirmação de Poder três vezes em voz alta:<br/><br/>"
        "<i>'Eu declaro que meu coração está livre de amarras do passado. Eu me abro para receber um amor nobre, recíproco, leal e sagrado. Que a minha alma gêmea reconheça minha vibração com facilidade e paz. Que assim seja e assim é.'</i>",
        box_style
    )
]]
ritual_table = Table(ritual_card_data, colWidths=[420])
ritual_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_BG_CARD),
    ('BOX', (0,0), (-1,-1), 1, C_ROSE),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(ritual_table)

story.append(Spacer(1, 30))
story.append(Paragraph("✦ Mahila Luz • O Mapa da Alma Gêmea • Todos os direitos reservados", ParagraphStyle('Foot', parent=body_style, alignment=1, fontSize=8.5, textColor=C_MUTED)))

doc.build(story)
print(f"E-book gerado com sucesso: {pdf_filename} ({os.path.getsize(pdf_filename)/(1024):.1f} KB)")
