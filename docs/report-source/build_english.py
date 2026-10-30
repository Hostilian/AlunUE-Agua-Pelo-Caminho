from pathlib import Path
# Reuse the reviewed typography, tables and layout helpers without running the Portuguese document body.
exec((Path(__file__).parent/'build_report.py').read_text(encoding='utf-8').split("p('INTERAÇÃO PESSOA-MÁQUINA")[0])

class EnglishDiagram(RouteVisual):
    def __init__(self,hta=False):super().__init__('hta' if hta else 'flow',en=True)

p('HUMAN-COMPUTER INTERACTION · INF13186L','SmallPT')
p('AlunUÉ<br/>Water along the way','TitlePT')
p('Exploratory research and requirements for refill discovery and student walking journeys in Évora.','H2PT')
p('Eren Ozturk · University of Évora · 30 October 2026')
p('<b>English review copy.</b> The Portuguese PDF is the intended coursework version. This copy explains the same evidence, design proposals and limitations for the author to review.','SmallPT')
p('<link href="https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/"><u>Open the app · GitHub Pages</u></link> | <link href="https://github.com/Hostilian/AlunUE-Agua-Pelo-Caminho"><u>Repository and checks</u></link>','SmallPT')
story.append(EnglishDiagram())
h('Scope and course fit')
p('The proposal is an essential-services and mobility module within AlunUÉ: find trustworthy information about a place to refill a bottle and continue the student day. Supermarkets, cultural stops and willing shops are optional extensions. Phase 1 focuses on research and requirements; a working prototype supports exploration and does not establish that the concept has been validated.')
h('State of the work')
p('This is individual work. The author says the lecturer approved individual work; documentary approval is not presented. Available research includes three individually reconstructed conversations from the previous week and general recalled feedback. The three personas and maps are provisional and now trace to concrete needs in those accounts. No recoverable structured survey or usability study has been completed. Evidence, interpretation and proposed design are kept distinct; missing data is not replaced by fabricated findings.')

title('02','Method and exploratory signals')
h('Source and conditions of collection')
p('The author informally spoke with acquaintances, including Erasmus students and people in his faculty, during the week before his account on 30 October 2026. Following loss of the original notes, he reconstructed three individual cases: C1-C3 (appendix). The author confirmed that all three are UÉ students and agreed to anonymous coursework summaries. Exact dates and locations were not recovered; enrolment and permission are confirmed through the author’s account. About 30 interlocutors remains an approximate recollection; the three cases are not a representative sample.')
p('Remembered prompts asked what people would like and whether an app would be useful. The proposal was discussed, but the precise question order was not recovered. This is retrospective reconstruction from a convenience sample, subject to selective recall and social-desirability bias. It does not measure adoption or problem frequency.')
table([['ID / source','Available signal and implication'],['E1/E2 · general recollection','Positive reactions, repeated water purchases and lack of awareness of refill locations, according to the author. No percentages or auditable counts.'],['E3 · author preference','Trust, walking routes, groceries, views and voluntary shops are scope decisions, not survey rankings.'],['E4 · operational state','No shop is confirmed as a participant. A network requires future agreements.'],['E5 · C1','Difficulty finding fountains in a new city and perceived difficulty finding inexpensive purchases and card payment. Investigate discovery, cost and payment information.'],['E6 · C2','A regular runner wants places to drink water and rest. Investigate route continuity and rest stops.'],['E7 · C3','Positive reaction and interest in receiving news. Investigate voluntary updates; this does not establish adoption or authorise automated notifications.']])
h('Interpretation and participant protection')
p('The cases support specific needs to investigate, not generalisations about all students. C1’s view of local retail is a perception, not a survey of Évora businesses. No individual objections were recalled; this does not establish their absence. Anonymous codes replace names; contacts and private messages are not published. The author confirmed permission for anonymous summaries of these three cases. Obtain renewed permission if the use changes.')

title('03','Three personas traced to the accounts')
p('These are provisional need-based personas anchored in C1-C3, not invented biographies or statistically validated segments. The author confirmed all three interlocutors’ UÉ connection. Generalising each profile to other students still requires validation. No unreported age, nationality, income or occupation is assigned.')
table([['Profile / basis','Goal, evidence and assumptions'],['P1 · Discovery in a new city / C1','Goal: find water and inexpensive alternatives without knowing the city. Recalled issues: fountains are hard to find; uncertainty about low-cost purchases and card acceptance. Implication: clear sources and cost; show payment information only when verified. Do not assume language ability.'],['P2 · Runner with water stops / C2','Goal: drink water and rest along regular running routes. Recalled fact: runs often and wants water/rest locations. Implication: plan and verify stops. Running times, distances and medical needs were not collected.'],['P3 · Person interested in following the service / C3','Goal: learn when the service is available. Recalled response: positive reaction and interest in news. Implication: a future voluntary update mechanism. Preferred channel, frequency, notification tolerance and actual usage remain unknown.']])
h('Supported needs and remaining validation')
p('Discovery and cost trace to C1; running, water and rest to C2; interest in news to C3. Emotions, detailed flows and interfaces are design proposals. Each profile has only one reconstructed source and needs further interviews to establish recurring patterns. P3 describes communication interest, without establishing a third distinct refill need.')
p('Next research: ask for concrete experiences before showing the prototype, investigate water/rest and update preferences, preserve negative responses and record date, context and permission. Do not replace memory gaps with assumptions.')

title('04','Empathy maps with traceability')
p('“Says / goal” summarises recalled feedback without quotation marks or claims of verbatim transcription. Other dimensions distinguish reported facts from hypotheses.')
for name,says,thinks,does,feels in [
('P1 · Discovery in a new city / C1','Recalled: fountains are hard to find; affordable purchases and card payment matter.','Hypothesis: how can I find an alternative and know the cost?','Not reconstructed: actual search route, purchases or app use.','Not collected; possible uncertainty remains a hypothesis.'),
('P2 · Runner / C2','Recalled: wants places to drink water regularly and rest.','Hypothesis: can I fit water and rest into the route?','Reported: runs often. Routes, distances and times unknown.','Not collected; do not assume fatigue or anxiety.'),
('P3 · Following the service / C3','Recalled: positive about the idea and would like news.','Hypothesis: how will I know when the service is available?','Expressed interest in updates; product use was not observed.','Positive reaction recalled; intensity not measured.')]:
    h(name);table([['Dimension','Identified account or hypothesis'],['Says / goal',says],['Thinks',thinks],['Does',does],['Feels',feels]],[120,375])
p('Confirm interpretations with the people concerned. Empathy maps do not establish direct knowledge of their thoughts.','SmallPT')

title('05','Proposed user journey')
p('Design scenario: a student needs to refill a bottle while travelling through the city. This sequence has not been observed in a field study or usability test.')
story.append(EnglishDiagram())
table([['Stage','Action and possible difficulty','Design response'],['1 · Need','Look for water without knowing where to start.','Searchable list, optional location and manual start.'],['2 · Assess','Distinguish a useful point from uncertain map data.','Source, date, access, cost and verification status.'],['3 · Plan','Choose stops without an unnecessary detour.','Adjustable order and optional grocery/cultural stops.'],['4 · Travel','Move the plan to external navigation.','Walking directions export and a text alternative.'],['5 · Arrive','Encounter a closure or incorrect information.','Show limits, seek an alternative and prepare a correction.'],['6 · Continue','Continue without pressure to spend or interact.','No purchase requirement; shops only with explicit opt-in.']],[65,215,215])
h('Variations traced to the accounts')
p('<b>P1 / C1:</b> discover water and inspect verified cost/payment information. <b>P2 / C2:</b> plan water and rest while running. <b>P3 / C3:</b> discover proposal → request news → choose channel and consent → receive news → opt out. The update flow is proposed and not implemented.')
p('The map uses real historic-centre geometry and OSM landmarks. Blue circles identify water candidates, not confirmed services. The table describes a proposed journey; no unvalidated walking route is drawn.','SmallPT')

title('06','Hierarchical task analysis')
p('Goal 0: obtain water and continue the journey. This HTA describes intended tasks and recovery paths, rather than behaviour already observed.')
story.append(EnglishDiagram(True))
table([['Task','Subtasks and completion conditions'],['1 · Set a start','1.1 Choose centre/campus or coordinates. 1.2 Request location only if wanted. 1.3 Keep a manual option when permission is refused.'],['2 · Assess a point','2.1 Inspect the list. 2.2 Read source and date. 2.3 Check water suitability, cost, access and operation. 2.4 Reject unconfirmed candidates from a real water journey.'],['3 · Plan stops','3.1 Add an eligible point. 3.2 Optionally add a supermarket or cultural stop. 3.3 Reorder. 3.4 Review. 3.5 Export in parts or save text.'],['4 · Follow and check','4.1 Consult external navigation. 4.2 Confirm conditions at the location. 4.3 Refill if allowed. 4.4 Choose an alternative and record a suggestion if information fails.']])
h('Plans and exceptions')
p('Main plan: 1 → 2 → 3 → 4. Repeat task 2 if no eligible point is available. Without internet, show a dated stored snapshot and saved itinerary; do not promise offline street maps. Without location, use task 1.1. If external services fail, preserve the list and offer text. A shop without agreement must not be shown as a participating partner.')
h('Operations explored in the prototype')
p('Type filters, search, an identified demonstration mode, selected and ordered stops, walking export, share/copy with text-file fallback, device-only suggestion drafts and optional service requests. There is no verified operational directory, moderation service or real partner registration.')

title('07','Requirements and evaluation criteria')
p('Project priorities: <b>P0</b> essential; <b>P1</b> extension. Targets below are proposed criteria for future testing, not measured results.')
table([['ID / priority','Requirement and traceability','Proposed criterion'],['R1 · P0','Distinguish candidates, demonstrations and confirmed points. E2 plus misinformation risk.','Never describe an unverified candidate as guaranteed drinking water.'],['R2 · P0','Find water without an account or mandatory location. E1/E2 and accessibility hypothesis.','At least 4 of 5 participants complete a manual-start task.'],['R3 · P0','Show source, date, cost and access. E2 and trust decision.','At least 4 of 5 correctly identify uncertainty before choosing.'],['R4 · P0','Preserve all stops on export. E3.','No chosen stop is lost; a readable text alternative exists.'],['R5 · P0','Recover from network/API failure. Robustness decision.','The plan is preserved and the failure explained.'],['R6 · P1','Combine optional grocery/cultural stops. E3.','Each extension can be excluded while keeping water as the focus.'],['R7 · P1','Voluntary shops without mandatory purchase. E3/E4.','No shop is listed as a partner without explicit agreement.'],['R8 · P1','Water/rest along a route; cost/payment when verified. E5/E6.','Never claim confirmed rest, price or card acceptance without a source.'],['R9 · P1','Future updates with explicit opt-in. E7.','No contact collection or notifications without permission; allow withdrawal. Not implemented.']],[60,240,195])
h('Usability and accessibility')
p('Design goals: European Portuguese labels, visible focus, keyboard access, readable contrast, zoom without content loss, suitable touch controls and recovery messages. Evaluate status recognition, completion, errors, task time and satisfaction. No SUS result was collected in this phase.')
h('Information architecture')
p('<b>Discover:</b> search, filters and sources. <b>My journey:</b> start, stops and export. <b>Community:</b> opt-in proposal and local drafts. <b>The project:</b> evidence, limits and sources. Planning a journey does not require joining the shop network.')

title('08','Limits, next steps and sources')
h('Limits affecting this phase')
p('The research is exploratory and retrospective. Three individual accounts have been reconstructed, but original notes/transcripts, a structured questionnaire, a verified participant population and independent persona validation are missing. A positive reaction to a presented idea does not measure adoption. The design artefacts must therefore not be treated as the results of a completed user study. Losing the notes explains the limitation but does not remove it.')
h('Water-source desk review · 30 October 2026')
table([['Source','What it establishes / limit'],['Municipality · 2026','The official page lists public-supply water-quality bulletins, including Q2 2026. These do not establish access, hours or operation at individual fountains.'],['Municipality · October 2012','The maintenance report records four drinking fountains outside green areas, one inoperative during that assessment. This is historical evidence, not a current operational inventory.'],['OSM · retrieved extract','15 water records grouped into 14 nearby candidates in the historic centre. Coordinates are mapped data, not confirmation of potability, free access or operation.']],[110,385])
p('The 2022 municipal water-heritage itinerary does not certify drinking water. No participating shop is confirmed. Next: verify points with the municipality and on site, complete student research and test the design artefacts.','SmallPT')
h('Use of generative AI')
p('Generative AI assisted report structure and Portuguese drafting, design artefacts, diagrams, prototype code and translation. The author supplied recollections and scope decisions. AI did not conduct interviews or verify places. The author should review and understand the content and remains responsible for the authenticity of the submission.')
h('Sources and supporting materials')
p('1. INF13186L, <i>Introdução à UC</i>, pp. 5-6: AlunUÉ scope, ten-page report limit and AI disclosure.<br/>2. INF13186L, <i>gemini_fase1</i>, p. 1: research, personas, empathy/journey maps and HTA. Later example pages were not used as interview evidence.<br/>3. Author statements and recollections, 30 October 2026.<br/>4. <link href="https://www.openstreetmap.org/copyright"><u>OpenStreetMap attribution</u></link>; <link href="https://developers.google.com/maps/documentation/urls/get-started"><u>official Google Maps URLs documentation</u></link>.<br/>5. <link href="https://www.cm-evora.pt/municipe/areas-de-acao/aguas/qualidade-da-agua/"><u>Municipal water-quality page / 2026 bulletins</u></link>; municipal maintenance report (2012), p. 78; <i>Percursos e Memórias da Água</i> (2022). Full sources/candidates in the repository.<br/>6. <link href="https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/"><u>Public app</u></link> and <link href="https://github.com/Hostilian/AlunUE-Agua-Pelo-Caminho"><u>dedicated repository</u></link>. The PDF stands on its own; links do not replace the required design artefacts.','SmallPT')

title('09','Appendix A · Reconstructed accounts')
p('Source: the author’s account on 30 October 2026, describing conversations during the previous week. The author confirmed all three people’s UÉ connection and agreement to anonymous coursework summaries. Anonymous codes replace names. Questions and answers are paraphrases, not direct quotations. Exact dates, locations and question order were not recovered.')
h('C1 · First person consulted')
table([['Field','Recalled summary'],['Question','What would you like to find, or what would be useful in this proposal? Approximate wording.'],['Response','Fountains are hard to find, and it can be difficult to know what to do in a new city. Mentioned difficulty finding inexpensive items such as water and shops accepting cards, and a perceived lack of chain shops.'],['Interpretation','Investigate discovery and cost/payment information. The retail perception does not establish actual business conditions.']],[100,395])
h('C2 · Person who runs regularly')
table([['Field','Recalled summary'],['Question','What would you like to find in the service? Approximate wording.'],['Response','Runs often and wants places to drink water regularly and rest.'],['Interpretation','Water and rest are explicit needs. Route, exact frequency, duration and locations were not recalled. The author subsequently confirmed this person’s identity; the analysis retains the anonymous code.']],[100,395])
h('C3 · Person interested in news')
table([['Field','Recalled summary'],['Question','The author recalls asking similar questions about the proposal; the precise sequence is unavailable.'],['Response','Reacted positively, considered the idea useful and wanted to receive news.'],['Interpretation','Declared interest in following progress, with no channel or frequency established. This is neither permission to publish personal data nor proof of adoption.']],[100,395])
p('The author also reports a list of other interested people, but no names, contacts or further responses were supplied. That list is not counted as additional participants or treated as authorised notification subscriptions.','SmallPT')

title('10','Visual synthesis · Evidence to design')
p('Each row connects a reconstructed account to a need, a working persona and the corresponding requirements. Colours identify cases; they do not encode percentages, intensity or frequency.')
story.append(EvidenceVisual(en=True))
h('How to read the project')
table([['Layer','What can be claimed'],['ACCOUNT','The author recalled three conversations and confirmed UÉ connection and permission for anonymous summaries.'],['INTERPRETATION','Themes guide design. The connections shown are project analysis, not statistical conclusions.'],['PROPOSAL','Personas, maps, targets and future features require confirmation through research and testing.']],[100,395])
h('The validation path')
p('<b>Recall and document</b> → confirm with participants → deepen the research → revise artefacts → test tasks → measure and improve. Visual clarity communicates the work; evidence quality supports its decisions.')

def footer_en(c,doc):
    paint_page(c,doc,en=True)
pdf=OUT/'AlunUE_Water_Along_The_Way_Phase1_EN_Review_v5.pdf'
SimpleDocTemplate(str(pdf),pagesize=(595.28,841.89),rightMargin=50,leftMargin=50,topMargin=43,bottomMargin=57,title='AlunUÉ - Water along the way - English review',author='Eren Ozturk').build(story,onFirstPage=footer_en,onLaterPages=footer_en)
print(pdf)
