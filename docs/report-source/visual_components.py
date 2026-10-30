from reportlab.platypus import Flowable, Paragraph, Spacer
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle

PALETTE=['#246D64','#A85631','#53649A']
PAPER=HexColor('#FAF9F4')
class RouteVisual(Flowable):
    def __init__(self,kind='flow',en=False):
        super().__init__();self.kind=kind;self.en=en;self.width=495;self.height=190 if kind=='hta' else 174
    def draw(self):
        c=self.canv
        st=ParagraphStyle('maptext',fontName='Arial',fontSize=9,leading=12,textColor=HexColor('#234B41'))
        def box(x,y,w,h,label,color='#E9F1EA'):
            c.setFillColor(HexColor(color));c.roundRect(x,y,w,h,8,fill=1,stroke=0)
            q=Paragraph(label,st);_,hh=q.wrap(w-16,h-12);q.drawOn(c,x+8,y+(h-hh)/2)
        if self.kind=='hta':
            top='0. Obtain water and continue' if self.en else '0. Obter água e continuar'
            box(125,140,245,43,top)
            labels=['Set start','Assess point','Plan stops','Follow + check'] if self.en else ['Definir início','Avaliar ponto','Planear paragens','Seguir + confirmar']
            for i,label in enumerate(labels):
                c.setStrokeColor(HexColor('#97B7AA'));c.setLineWidth(1.3);c.line(247,140,i*125+57,119)
                box(i*125,62,115,57,f'<b>{i+1:02d}</b><br/>'+label,['#E9F1EA','#F7EEE2','#EBEDF6','#E9F1EA'][i])
            note='Plan: 1 → 2 → 3 → 4. If verification fails, choose another point. If export fails, save text.' if self.en else 'Plano: 1 → 2 → 3 → 4. Se a verificação falhar, escolher outro ponto. Se a exportação falhar, guardar texto.'
            box(0,0,490,48,note)
            return
        c.setFillColor(HexColor('#EAF1E7'));c.roundRect(0,24,495,146,12,fill=1,stroke=0)
        # An explicitly conceptual map: no street or verified geographic claim.
        c.setStrokeColor(HexColor('#D2DDD0'));c.setLineWidth(18)
        for a,b,d,e in [(0,60,495,134),(70,24,180,170),(270,24,380,170)]:c.line(a,b,d,e)
        p=c.beginPath();p.moveTo(35,55);p.curveTo(145,35,90,136,205,122);p.curveTo(300,110,310,49,450,128)
        c.setStrokeColor(HexColor('#276D60'));c.setLineWidth(3);c.setDash(4,4);c.drawPath(p);c.setDash()
        for i,(x,y,label) in enumerate([(35,55,'INÍCIO' if not self.en else 'START'),(205,122,'ÁGUA' if not self.en else 'WATER'),(329,84,'PAUSA' if not self.en else 'REST'),(450,128,'SEGUIR' if not self.en else 'CONTINUE')]):
            color=PALETTE[i%3];c.setFillColor(HexColor(color));c.circle(x,y,14,fill=1,stroke=0);c.setFillColor(white);c.setFont('ArialBold',10);c.drawCentredString(x,y-3,str(i+1));
            c.setFillColor(HexColor('#173E34'));c.setFont('ArialBold',8);c.drawCentredString(max(30,min(459,x)),y-29,label)
        c.setFillColor(HexColor('#52665E'));c.setFont('Arial',8)
        c.drawString(0,7,'Conceptual journey, not a street map or verified directory.' if self.en else 'Percurso conceptual, não é um mapa de ruas nem um inventário verificado.')

class EvidenceVisual(Flowable):
    def __init__(self,en=False):super().__init__();self.width=495;self.height=290;self.en=en
    def draw(self):
        c=self.canv
        rows=[('C1','Discover + cost/payment','P1 · New-city discovery','R3 / R8'),('C2','Water + rest while running','P2 · Running with stops','R4 / R8'),('C3','Voluntary progress updates','P3 · Following the service','R9')] if self.en else [('C1','Descoberta + custo/pagamento','P1 · Descoberta na cidade','R3 / R8'),('C2','Água + descanso na corrida','P2 · Corrida com paragens','R4 / R8'),('C3','Novidades por adesão','P3 · Acompanhar o serviço','R9')]
        labels=['ACCOUNT','RECALLED NEED','WORKING PERSONA','REQUIREMENT'] if self.en else ['RELATO','NECESSIDADE RECORDADA','PERSONA PROVISÓRIA','REQUISITO']
        xs=[0,54,237,421];widths=[43,172,173,74]
        c.setFont('ArialBold',7);c.setFillColor(HexColor('#52665E'))
        for x,label in zip(xs,labels):c.drawString(x,275,label)
        for i,row in enumerate(rows):
            y=189-i*85; color=HexColor(PALETTE[i])
            for j,(x,w,label) in enumerate(zip(xs,widths,row)):
                c.setFillColor(color if j==0 else HexColor(['#EDF5F0','#FAEFE7','#EEF0F8'][i]));c.roundRect(x,y,w,61,8,fill=1,stroke=0)
                st=ParagraphStyle('evidence',fontName='ArialBold' if j in [0,3] else 'Arial',fontSize=9,leading=12,textColor=white if j==0 else HexColor('#233A34'))
                q=Paragraph(label,st);_,h=q.wrap(w-14,55);q.drawOn(c,x+7,y+(61-h)/2)
                if j<3:c.setStrokeColor(color);c.setLineWidth(1.5);c.line(x+w+1,y+30,xs[j+1]-2,y+30)

class PersonaCards(Flowable):
    def __init__(self,rows):super().__init__();self.rows=rows;self.width=495;self.height=330
    def draw(self):
        c=self.canv
        for i,row in enumerate(self.rows):
            y=224-i*110;c.setFillColor(HexColor(['#EDF5F0','#FAEFE7','#EEF0F8'][i]));c.roundRect(0,y,495,103,9,fill=1,stroke=0)
            c.setFillColor(HexColor(PALETTE[i]));c.roundRect(0,y,8,103,4,fill=1,stroke=0)
            hs=ParagraphStyle('ph',fontName='ArialBold',fontSize=10,leading=13,textColor=HexColor(PALETTE[i]))
            bs=ParagraphStyle('pb',fontName='Arial',fontSize=9.1,leading=12.3,textColor=HexColor('#233A34'))
            q=Paragraph(row[0],hs);_,h=q.wrap(452,30);q.drawOn(c,22,y+103-h-11)
            q=Paragraph(row[1],bs);_,h=q.wrap(452,80);q.drawOn(c,22,y+103-h-35)

class EmpathyVisual(Flowable):
    def __init__(self,rows):super().__init__();self.rows=rows;self.width=495;self.height=150
    def draw(self):
        c=self.canv
        for i,(label,value) in enumerate(self.rows):
            x=(i%2)*253;y=77 if i<2 else 0;w=242;h=72
            c.setFillColor(HexColor(['#E8F2EA','#F8EDE2','#EDF0F7','#F1EFE5'][i]));c.roundRect(x,y,w,h,7,fill=1,stroke=0)
            c.setFillColor(HexColor('#246D64'));c.setFont('ArialBold',8);c.drawString(x+10,y+h-14,label.upper())
            st=ParagraphStyle('empathy',fontName='Arial',fontSize=8.8,leading=11.5,textColor=HexColor('#233A34'))
            q=Paragraph(value,st);_,hh=q.wrap(w-20,50);q.drawOn(c,x+10,y+h-23-hh)

def paint_page(c,doc,en=False):
    c.saveState();c.resetTransforms();c.setFillColor(PAPER);c.rect(0,0,595.28,841.89,fill=1,stroke=0)
    c.setFillColor(HexColor('#246D64'));c.rect(0,819,595.28,23,fill=1,stroke=0)
    c.setFont('ArialBold',7);c.setFillColor(white);c.drawString(50,827,'ALUNUÉ / WATER ALONG THE WAY' if en else 'ALUNUÉ / ÁGUA PELO CAMINHO')
    c.setFillColor(HexColor('#C57D45'));c.roundRect(50,48,495,2,1,fill=1,stroke=0)
    c.setFont('Arial',8);c.setFillColor(HexColor('#52665E'));c.drawString(50,31,'ENGLISH REVIEW · 30/10/2026' if en else 'INVESTIGAÇÃO E REQUISITOS · 30/10/2026')
    c.setFont('ArialBold',9);c.drawRightString(545,30,f'{doc.page:02d}');c.restoreState()
