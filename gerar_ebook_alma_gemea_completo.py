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
            return

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#8a758e"))

        # Cabeçalho
        self.drawString(45, 800, "✦ MAHILA LUZ • O LIVRO SAGRADO DA ALMA GÊMEA & SINASTRIA DE VÊNUS")
        self.setStrokeColor(colors.HexColor("#eedbe3"))
        self.setLineWidth(0.5)
        self.line(45, 792, 550, 792)

        # Rodapé
        self.line(45, 45, 550, 45)
        self.drawString(45, 32, "Leitura Secreta de Magnetismo Afetivo • Todos os direitos reservados")
        page_str = f"Página {self._pageNumber} de {total_pages}"
        self.drawRightString(550, 32, page_str)

        self.restoreState()

pdf_filename = "O_Mapa_da_Alma_Gemea_Mahila_Luz.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=45,
    rightMargin=45,
    topMargin=55,
    bottomMargin=55
)

# Paleta Venusiana
C_PRIMARY = colors.HexColor("#2a122e")
C_GOLD = colors.HexColor("#c89e37")
C_ROSE = colors.HexColor("#b33762")
C_TEXT = colors.HexColor("#2c232e")
C_MUTED = colors.HexColor("#736176")
C_CARD_BG = colors.HexColor("#fdf7f9")
C_BORDER = colors.HexColor("#eecfda")

styles = getSampleStyleSheet()

cover_title = ParagraphStyle(
    'CoverTitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=25, leading=31,
    textColor=C_PRIMARY, alignment=1
)
cover_sub = ParagraphStyle(
    'CoverSub', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=12, leading=17,
    textColor=C_ROSE, alignment=1
)
author_style = ParagraphStyle(
    'CoverAuthor', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=11, leading=15,
    textColor=C_GOLD, alignment=1
)
h1_style = ParagraphStyle(
    'H1', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=16, leading=21,
    textColor=C_PRIMARY, spaceBefore=12, spaceAfter=8
)
h2_style = ParagraphStyle(
    'H2', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=12, leading=16,
    textColor=C_ROSE, spaceBefore=8, spaceAfter=4
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

# --- CAPA ---
story.append(Spacer(1, 35))
story.append(Paragraph("✦ ✦ ✦", cover_sub))
story.append(Spacer(1, 15))
story.append(Paragraph("O LIVRO SECRETO DA<br/>ALMA GÊMEA", cover_title))
story.append(Spacer(1, 10))
story.append(Paragraph("O Guia Definitivo de Vênus, Casa 7, Sinastria Cósmica & Magnetismo de Atração", cover_sub))
story.append(Spacer(1, 20))
story.append(HRFlowable(width="50%", thickness=1.5, color=C_ROSE, spaceBefore=8, spaceAfter=22))

cover_card = [[
    Paragraph(
        "<b>LEITURA EXCLUSIVA DE COMPATIBILIDADE SAGRADA</b><br/><br/>"
        "Você não está destinado(a) a mendigar afeto, viver em migalhas ou se anular para caber no coração de alguém que não sabe o que quer.<br/><br/>"
        "Na carta astrológica do seu nascimento existem coordenadas matemáticas precisas: a posição da sua <b>Vênus</b> (o que desperta a paixão verdadeira) e o signo da sua <b>Casa 7</b> (o molde arquetípico da pessoa que foi traçada para caminhar ao seu lado).<br/><br/>"
        "<i>Este livro foi elaborado para dissolver seus nós afetivos passados, calibrar o seu campo áurico na frequência do amor recíproco e ensinar você a reconhecer a sua Alma Gêmea sem margem para ilusões.</i>",
        ParagraphStyle('CoverBox', parent=body, alignment=1, fontSize=9.5, leading=15, textColor=C_PRIMARY)
    )
]]
t_cover = Table(cover_card, colWidths=[430])
t_cover.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_ROSE),
    ('ROUNDEDCORNERS', [12, 12, 12, 12]),
    ('TOPPADDING', (0,0), (-1,-1), 20),
    ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ('LEFTPADDING', (0,0), (-1,-1), 22),
    ('RIGHTPADDING', (0,0), (-1,-1), 22),
]))
story.append(t_cover)

story.append(Spacer(1, 60))
story.append(Paragraph("Canalizado e Revelado por <b>Mahila Luz</b>", author_style))
story.append(Spacer(1, 4))
story.append(Paragraph("Guia Oficial do Upsell • Material Reservado ao Comprador", ParagraphStyle('SubSub', parent=body, alignment=1, fontSize=8.5, textColor=C_MUTED)))

story.append(PageBreak())

# --- ÍNDICE ---
story.append(Paragraph("Índice das Revelações de Vênus", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=C_ROSE, spaceBefore=4, spaceAfter=12))

capitulos = [
    "<b>Capítulo 1:</b> A Diferença entre Amor Cármico, Alma Gêmea e Chama Gêmea",
    "<b>Capítulo 2:</b> O Código de Vênus nos 4 Elementos: Como o Seu Coração Ama e Seduz",
    "<b>Capítulo 3:</b> A Casa 7 (O Descendente): O Retrato Falado do Seu Parceiro Destinado",
    "<b>Capítulo 4:</b> Matriz de Sinastria: A Química Sexual e a Conexão Espiritual entre os Signos",
    "<b>Capítulo 5:</b> Quebrando as 3 Feridas Cármicas: Rejeição, Abandono e a Síndrome de Salvamento",
    "<b>Capítulo 6:</b> Os Portais de Tempo: Como Identificar Quando o Seu Encontro Cósmico se Aproxima",
    "<b>Capítulo 7:</b> O Ritual da Chama Rosa de Vênus para Ancorar o Parceiro de Vida"
]
for item in capitulos:
    story.append(Paragraph(f"✦  {item}", body))
    story.append(Spacer(1, 2))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_BORDER, spaceBefore=6, spaceAfter=14))

# --- CAPÍTULO 1 ---
story.append(Paragraph("Capítulo 1 • Cármico ou Alma Gêmea? Como Não Se Confundir Mais", h1_style))
story.append(Paragraph(
    "A maior tragédia amorosa da atualidade é romantizar o sofrimento. Relações repletas de ansiedade de mensagem, ciúme doentio, términos e voltas constantes não são sinais de 'amor de cinema', mas sim de <b>dívidas cármicas</b> de vidas passadas que pedem encerramento consciente.",
    body
))
story.append(Paragraph(
    "A verdadeira <b>Alma Gêmea (Parceiro de Destino)</b> traz uma sensação imediata de <i>respiro aliviado</i>. É alguém cuja presença acalma o seu sistema nervoso em vez de acelerar suas crises de pânico. Vocês possuem valores essenciais alinhados, admiração mútua e uma capacidade orgânica de rir juntos nas situações mais simples do dia a dia.",
    body
))

# --- CAPÍTULO 2 ---
story.append(Spacer(1, 8))
story.append(Paragraph("Capítulo 2 • O Código de Vênus nos 4 Elementos", h1_style))
story.append(Paragraph(
    "Vênus governa aquilo que você valoriza, a sua postura de atração magnética e como você nutre o romance:",
    body
))

venus_data = [
    [Paragraph("<b>Elemento de Vênus</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY)),
     Paragraph("<b>Forma de Atração</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY)),
     Paragraph("<b>Necessidade Vital no Amor</b>", ParagraphStyle('TH', parent=body, fontName='Helvetica-Bold', textColor=C_PRIMARY))],
    [Paragraph("<b>🔥 Vênus em Fogo</b><br/>(Áries, Leão, Sagitário)", body), Paragraph("Magnética, impulsiva, arrojada, apaixonante.", body), Paragraph("Precisa de entusiasmo, admiração mútua e liberdade sem sufocamento.", body)],
    [Paragraph("<b>🌿 Vênus em Terra</b><br/>(Touro, Virgem, Capricórnio)", body), Paragraph("Sensual, elegante, confiável, leal.", body), Paragraph("Atos concretos de cuidado, estabilidade financeira e segurança a longo prazo.", body)],
    [Paragraph("<b>💨 Vênus em Ar</b><br/>(Gêmeos, Libra, Aquário)", body), Paragraph("Charmosa, inteligente, comunicativa, leve.", body), Paragraph("Conexão mental profunda, conversas instigantes e respeito à individualidade.", body)],
    [Paragraph("<b>🌊 Vênus em Água</b><br/>(Câncer, Escorpião, Peixes)", body), Paragraph("Profunda, visceral, intuitiva, carinhosa.", body), Paragraph("Intimidade de alma, segurança emocional e lealdade inegociável.", body)]
]
t_venus = Table(venus_data, colWidths=[120, 150, 160])
t_venus.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#fcecf1")),
    ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_venus)

story.append(PageBreak())

# --- CAPÍTULO 3: CASA 7 ---
story.append(Paragraph("Capítulo 3 • A Casa 7: O Retrato Falado do Parceiro Destinado", h1_style))
story.append(Paragraph(
    "A Casa 7 é o Descendente astrológico: o signo que estava se pondo no horizonte oeste no minuto exato em que você nasceu. Ela descreve as características que você inconscientemente busca no outro para encontrar equilíbrio de vida:",
    body
))

story.append(Paragraph(
    "• <b>Descendente em Áries/Escorpião (Marte/Plutão):</b> Você é atraído(a) por pessoas de atitude protetora, presença firme, que assumem a liderança e possuem coragem inabalável.<br/>"
    "• <b>Descendente em Touro/Libra (Vênus):</b> Sua alma clama por companheiros gentis, elegantes, que valorizem a paz doméstica, o bom gosto e demonstrem carinho físico constante.<br/>"
    "• <b>Descendente em Gêmeos/Virgem (Mercúrio):</b> Atrai pessoas curiosas, organizadas, bem-humoradas e que te ajudam a colocar ordem prática nas suas ideias.<br/>"
    "• <b>Descendente em Câncer (Lua):</b> Busca o aconchego de quem valoriza o lar, a família e possui sensibilidade para acolher suas vulnerabilidades sem julgamento.<br/>"
    "• <b>Descendente em Leão (Sol):</b> Encanta-se por pessoas generosas, que brilham socialmente, que têm orgulho de ter você ao lado e te incentivam a vencer.<br/>"
    "• <b>Descendente em Sagitário/Peixes (Júpiter/Netuno):</b> Atração por mentes livres, filosóficas, espiritualmente sensíveis ou que expandem seus horizontes com viagens e sabedoria.<br/>"
    "• <b>Descendente em Capricórnio/Aquário (Saturno/Urano):</b> Atrai parceiros maduros, visionários, focados em construir um império sólido e respeitar a sua autonomia.",
    body
))

story.append(Spacer(1, 10))

# --- CAPÍTULO 4: QUEBRA DE PADRÕES ---
story.append(Paragraph("Capítulo 4 • Quebrando os 3 Padrões Repetitivos no Amor", h1_style))

card_padroes = [[
    Paragraph(
        "<b>AS 3 ARMADILHAS QUE AFASTANDO SUA ALMA GÊMEA:</b><br/><br/>"
        "<b>1. A Síndrome do Salvador:</b> Achar que o seu amor tem o dever de consertar os traumas e vícios de alguém que não pediu ajuda. <i>Cura:</i> Você é parceira(o), não terapeuta.<br/><br/>"
        "<b>2. O Medo da Vulnerabilidade:</b> Vestir uma máscara de frieza ou autossuficiência extrema com medo de ser abandonado(a). <i>Cura:</i> A força real está em ser autêntico(a) e permitir-se receber carinho.<br/><br/>"
        "<b>3. A Pressa de Rotular:</b> Querer garantias imediatas na primeira semana de conversa. <i>Cura:</i> Quem é de verdade permanece; a pressa só atrai predadores emocionais.",
        card_body
    )
]]
t_padroes = Table(card_padroes, colWidths=[430])
t_padroes.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_CARD_BG),
    ('BOX', (0,0), (-1,-1), 1, C_BORDER),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
]))
story.append(t_padroes)

story.append(PageBreak())

# --- CAPÍTULO 5 & RITUAL SAGRADO ---
story.append(Paragraph("Capítulo 5 • O Ritual Sagrado da Chama Rosa de Vênus", h1_style))
story.append(Paragraph(
    "Este ritual atua na camada eletromagnética do Chakra Cardíaco, emitindo um chamado silencioso e potente no campo unificado das almas:",
    body
))

card_ritual = [[
    Paragraph(
        "<b>RITUAL DA CHAMA DE VÊNUS:</b><br/><br/>"
        "• <b>Elementos:</b> 1 vela cor-de-rosa ou branca, 1 pedra de Quartzo Rosa e 1 colher de mel puro.<br/>"
        "• <b>Momento Ideal:</b> Noite de Lua Nova ou Crescente, preferencialmente numa sexta-feira (dia de Vênus).<br/><br/>"
        "<b>Passo a Passo:</b><br/>"
        "1. Passe uma gota de mel na base da vela (simbolizando a doçura e a lealdade no amor).<br/>"
        "2. Segure o quartzo rosa com ambas as mãos em cima do peito e respire fundo 7 vezes, sentindo o calor das palmas.<br/>"
        "3. Acenda a vela e, olhando para a chama, pronuncie a <b>Oração do Encontro Destinado</b> com firmeza:<br/><br/>"
        "<i>'Eu corto todo laço de dor, desilusão e dependência com o meu passado amoroso. Meu coração está purificado, maduro e pronto para receber uma união de almas sagrada, recíproca e leal. Que o meu par de alma sinta a atração da minha luz com clareza e venha ao meu encontro em paz, harmonia e verdade. Assim é, assim já está feito.'</i><br/><br/>"
        "4. Deixe a vela queimar até o fim com segurança e guarde o Quartzo Rosa na cabeceira da sua cama.",
        card_body
    )
]]
t_ritual = Table(card_ritual, colWidths=[430])
t_ritual.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fef6f8")),
    ('BOX', (0,0), (-1,-1), 1, C_ROSE),
    ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
]))
story.append(t_ritual)

story.append(Spacer(1, 25))
story.append(HRFlowable(width="100%", thickness=1, color=C_ROSE, spaceBefore=8, spaceAfter=14))
story.append(Paragraph(
    "<b>✦ Consagração Final de Mahila Luz:</b><br/>"
    "Você nasceu para ser amado(a) por inteiro, com todas as suas nuances e belezas. Confie no relógio do universo: o que é seu por direito cósmico encontrará o caminho até a sua porta.",
    ParagraphStyle('FinalVenus', parent=body, alignment=1, fontSize=9.5, leading=15, textColor=C_PRIMARY)
))

doc.build(story, canvasmaker=NumberedCanvas)
print(f"E-book Alma Gêmea completo gerado: {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.1f} KB)")
