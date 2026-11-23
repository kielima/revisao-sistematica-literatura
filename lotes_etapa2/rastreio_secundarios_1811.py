import json,csv,sys
p={d['id_sec']:d for d in json.load(open(sys.argv[1]))}
m={r['id_sec']:r for r in json.load(open(sys.argv[2]))}
prov={14:'betao geopolimerico vs OPC, CO2-e por m3 e classe de resistencia',17:'betao alcali-ativado (cinza volante + RHA), ACV e custo; ensaio de resistencia provavel',18:'betao alcali-ativado com silicato de vidro residual, ACV; resistencia provavel',21:'betao alcali-ativado por classe de resistencia (CO2 por m3)',22:'geopolimeros de argila, GWP de misturas de betao com resistencia',26:'betao geopolimerico de zeolita natural, ACV com resistencia',28:'betao alcali-ativado de pozolana vulcanica + GGBFS vs OPC, ACV com resistencia',31:'betoes alcali-ativados em ambiente marinho, ACV; resistencia provavel',16:'ACV de betao geopolimerico (misturas de referencia); confirmar se ha fck por mistura'}
duv={19:'pastas (nao betao) - fck de pasta nao e fck de betao',20:'sintese de albita (pasta), foco quimico',23:'revisao (secundario de secundario)',29:'mistura para protecao ao fogo (nao estrutural)',75:'reforco de vigas com FRP - CO2 do esquema de reforco, nao do betao',93:'reparacao de betao armado - CO2 do reparo'}
w=csv.writer(open(sys.argv[3],'w',newline='',encoding='utf-8'))
w.writerow(['id_sec','revisao','autor_ano','doi','titulo_crossref','tipo_crossref','acesso_aberto','pdf_oa','rastreio','motivo'])
from collections import Counter; c=Counter()
for i,d in sorted(p.items()):
    r=m.get(i,{})
    if i in prov: k,mo='provavel_E2',prov[i]
    elif i in duv: k,mo='duvidoso',duv[i]
    elif d['revisao'].startswith('ONSONGO'): k,mo='improvavel','fator de emissao/baseline do cimento ou revisao - sem par fck x CO2 de betao'
    else: k,mo='improvavel','ACV/LCC/SLCA de infraestrutura ou edificio (sistema), sem CO2 por m3 de betao com fck (F18)'
    c[k]+=1
    w.writerow([i,d['revisao'],d['autor_ano'],d['doi'],(r.get('title') or '').replace('\n',' ').split('  ')[0],r.get('type',''),r.get('is_oa',''),r.get('oa_pdf') or '',k,mo])
print(c)
