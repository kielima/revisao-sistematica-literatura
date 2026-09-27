import json,glob,re,openpyxl,sys
SP='/tmp/claude-0/-home-user-revisao-sistematica-literatura/e4059436-221b-590c-8cc1-b1e32ceb1c68/scratchpad/sempar/'
XL='/home/user/revisao-sistematica-literatura/meta_analysis_base.xlsx'
D='2026-09-27'
res={}
for f in sorted(glob.glob(SP+'resultado_lote_*.json')):
    try: d=json.load(open(f))
    except FileNotFoundError: continue
    if isinstance(d,dict): d=d.get('resultados') or d.get('artigos') or []
    for o in d: res[o['row_id']]=dict(o, _lote=f.split('_')[-1][:-5])
# --- decisoes da auditoria ---
EXCLUIR_ART={3215:'incoerente com o proprio inventario (10.300 kg/m3 com 380 kg de cimento; cenario inclui deposicao de lamas)',
 3272:'Tab.7 incoerente (8.922 t em 2.523 m3 = 3,54 t/m3; 920 kg CO2/t = factor de cimento); fck misto',
 3285:'total do edificio inteiro (acabamentos, aluminio, instalacoes) nao atribuivel ao betao',
 3346:'reconstrucao dependente de dados nao impressos; betao reutilizado conta zero (CO2 e transporte/cimbre)',
 3418:'pastas; CO2 por kg de cimento; conversao exigiria supor massa volumica da amassadura',
 3542:'GWP incoerente com o proprio traço (-60% com -20% de cimento; fibras de aco acrescentadas); M6 copia o NC',
 3543:'duplicado de 3542 (mesma obra) e mesma incoerencia',
 3553:'UF = 1 t de ligante seco; legenda "1 m3" fisicamente impossivel; massa volumica da pasta nao impressa',
 3834:'factor 141 kg CO2/t de cimento (~6x abaixo do normal) e "Sum" da Tab.10 incoerente com as parcelas',
 3852:'so o intervalo interquartil (240-466) e impresso; sem valor central',
 4102:'unidade da coluna "Emission CO2" da Fig.7 nao impressa',
 4739:'volume de material da laje waffle inclui provavelmente os caixotes de EPS; laje tradicional sem fck',
 4827:'fck indefinido (30 ou 40)',
 5015:'metodo UFSM soma "CO2 no ar" como materia-prima; total > 2x o CO2 fossil do inventario (dupla contagem provavel)',
 5016:'metodo UFSM (idem 5015): 1.839-2.099 kg/m3 incoerente com o inventario',
 5019:'metodo UFSM (idem 5015)', 5043:'metodo UFSM (idem 5015)',
 5046:'total inclui lajotas ceramicas, formas e concreto feito em obra de volume nao impresso (divisor incompleto)',
 2668:'volume de betao e massa volumica nao impressos (so 472 t)',
 4792:'PENDENTE decisao da Kie (via so-fundacao vs decisao de 12/09)',
 4768:'PENDENTE confirmacao visual da Fig.4', 4500:'PENDENTE Fig.8 (valores de GWP herdados, nao vistos)',
}
def keep(rid,l):
    m=(l.get('material') or '').lower(); sr=l.get('sheet_row_existente_ou_null'); c=l.get('co2_kg_m3')
    if rid==2599: return sr==613
    if rid==2687: return sr==1856
    if rid==2738: return 'so a parcela' in m
    if rid==2739: return sr!=176
    if rid==2828: return sr==708
    if rid==3162: return "so a coluna 'concrete'" in m
    if rid==3301: return 'termo independente' not in m and 'parcela sem armadura' not in m
    if rid==3359: return sr!=391
    if rid==3424: return '100 anos' not in m and 'cenario 2' not in m
    if rid==3620: return sr==1067
    if rid==3685: return 'so constituintes' in m
    if rid==4161: return 'pilar' not in m
    if rid==4349: return sr==1301
    if rid==4452: return 'regular mix' not in m
    if rid==4560: return 'so fase de fabrico' in m
    if rid==4584: return sr==1601
    if rid==4709: return not ('394a' in m or '394b' in m)
    if rid==4789: return sr==1788
    if rid==4806: return sr==1793
    if rid==5018: return sr==43
    if rid==5041: return 'so (cimento' not in m and 'sem aco/formas' not in m
    if rid==5052: return 'superestrutura' not in m
    return True
OVR={ (3409,991):{'co2_kg_m3':626.2,'co2_conversao':'Tab.4 "Decking" CD 3,20 x 10^4 kg (expoente impresso 10^5 corrigido: com 10^5 os factores implicitos de TODOS os materiais sao absurdos - aco 14 kg/kg, Al 57 kg/kg, betao 6.262 kg/m3; com 10^4 ficam plausiveis) / 51,1 m3 de betao 35 MPa (Tab.3) = 626,2 [ALERTA ETAPA4: expoente corrigido por nos]','confianca':'baixa'},
 (4297,1264):{'fck_mpa':20,'_alerta':'CO2 e do processo Ecoinvent "Pre-cast concrete C 20/25" (Tab.5) -> pareado com fck 20; o betao real do reforco e C30'},
}
ALERTA_ART={2680:'fraccao do betao no GWP impressa no texto',3120:'eixo diz "per m2" mas o texto fala em metro linear',4092:'22 dos 26 traços sao da literatura (Tab.1-2), so os 4 RS sao ensaio proprio',
 4709:'fck = media de 2-4 registos da base compilada com o mesmo traço (so muda a concentracao bacteriana), calculada por nos; fonte externa',
 4698:'factores por classe do proprio artigo (tracos de quota orcamental), nao misturas ensaiadas',4716:'ton dos factores EPA nao definida; assumida metrica (se short ton, +10%)',
 4452:'misturas de modelo de optimizacao, nao ensaiadas',4724:'rotulo "kg-CO2eq/t" contra UF 1 m3; traço x factores reproduz a Fig.3',4498:'UF declarada 1 m2 mas totais por painel 6x1 m (Vconc Tab.5); inclui credito de reciclagem do aco',
 4161:'fck calculado pela formula de Bolomey, nao ensaiado',4584:'factor generico nacional (KLCI DB) de betao pronto',4297:'factor generico Ecoinvent',3034:'intensidade media do betao do edificio (0,17 kg/kg)',
 4789:'total A1-A3 inclui armadura e pequenos componentes nao estruturais',2687:'total do Metodo 1 inclui aco, cabos, cofragem e parcelas menores (membrana, asfalto)',4349:'classes mistas 4000-10000 psi; fck da classe dominante (lajes 5000 psi)',
 2599:'fck 80 MPa da argamassa 100% CEM apresentado na discussao (as restantes so tem limite inferior)'}
GROSS={4350:(287.0,'bruto sem creditos de reciclagem lido na Fig.8 (~287); liquido publicado 705 kg/4,4 m3 = 160,2'),
       (4505,'cflw'):(240.0,'bruto sem credito ~240 (liquido 225,8)')}
FIG_PEND={3105,2895,3133,3153,3238,3420,4033,3439,3203,3176,3120,4516}

def cs(s): return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',str(s)) if s is not None else None
def num(x):
    try: return float(str(x).replace(',','.'))
    except: return None

def run(dry=True):
    wb=openpyxl.load_workbook(XL); ws=wb['dados_fck']
    rows_by={}
    for r in range(2,ws.max_row+1): rows_by.setdefault(ws.cell(r,1).value,[]).append(r)
    stats={'upd':0,'new':0,'nao':0,'skip_pend':0}
    log=[]
    for rid,o in sorted(res.items()):
        if o.get('_lote')=='figuras': continue
        ver=str(o.get('veredicto',''))
        motivo_nc=None
        if rid in EXCLUIR_ART: motivo_nc=EXCLUIR_ART[rid]
        elif rid in FIG_PEND and rid not in FIGDONE: stats['skip_pend']+=1; continue
        elif rid in FIGLINES: pass
        elif not ver.startswith('PAR_CONVERTIVEL'): motivo_nc=f"{ver}: {o.get('motivo','')}"[:900]
        if motivo_nc:
            for r in rows_by.get(rid,[]):
                if ws.cell(r,37).value not in (None,''): continue
                ws.cell(r,36).value=cs(f'NAO CONVERTIDO - revisao {D} (leitura integral do PDF): {motivo_nc}')
                ws.cell(r,13).value=cs((ws.cell(r,13).value or '')+f' [REVISTO {D}, leitura integral dos Elegiveis sem par: {motivo_nc[:400]}]')
                stats['nao']+=1
            continue
        linhas=FIGLINES.get(rid) or o.get('linhas') or []
        for l in linhas:
            fck=num(l.get('fck_mpa')); co2=num(l.get('co2_kg_m3'))
            if fck is None or co2 is None or not keep(rid,l): continue
            sr=l.get('sheet_row_existente_ou_null')
            ov=OVR.get((rid,sr),{})
            if 'fck_mpa' in ov: fck=ov['fck_mpa']
            conv=cs(ov.get('co2_conversao') or l.get('co2_conversao') or '')
            conf=ov.get('confianca') or l.get('confianca') or ''
            m=(l.get('material') or '').lower()
            g=GROSS.get(rid) or (GROSS.get((rid,'cflw')) if 'cflw' in m else None)
            if g: co2=g[0]; conv=conv+' | '+g[1]
            if 'co2_kg_m3' in ov: co2=ov['co2_kg_m3']
            al=[x for x in (ALERTA_ART.get(rid),ov.get('_alerta')) if x]
            conv=cs(f"{conv} [REVISAO {D}, leitura integral; confianca {conf}]"+''.join(f' [ALERTA ETAPA4: {a}]' for a in al))
            if sr and sr in rows_by.get(rid,[]):
                r=sr; stats['upd']+=1
            else:
                base=rows_by.get(rid,[None])[0]
                r=ws.max_row+1; stats['new']+=1
                if base:
                    for c in (1,2,3,4,5,6,21,22): ws.cell(r,c).value=ws.cell(base,c).value
                else:
                    ws.cell(r,1).value=rid
                ws.cell(r,7).value=cs(l.get('material'))
                rows_by.setdefault(rid,[]).append(r)
            ws.cell(r,8).value=fck
            if l.get('fck_tipo') and not ws.cell(r,11).value: ws.cell(r,11).value=cs(l.get('fck_tipo'))
            if l.get('fck_local'): ws.cell(r,12).value=cs(l.get('fck_local'))
            ws.cell(r,34).value=cs(l.get('co2_original')); ws.cell(r,35).value=cs(l.get('co2_original_local'))
            ws.cell(r,36).value=conv; ws.cell(r,37).value=round(co2,2)
            v=num(l.get('vol_m3'))
            if v and not ws.cell(r,23).value: ws.cell(r,23).value=v; ws.cell(r,24).value=cs(l.get('vol_fonte'))
            vu=num(l.get('vida_util_anos'))
            if vu and not ws.cell(r,19).value: ws.cell(r,19).value=vu; ws.cell(r,20).value=cs(l.get('vida_util_local'))
            ws.cell(r,13).value=cs((ws.cell(r,13).value or '')+f' [REVISTO {D}, leitura integral dos Elegiveis sem par: par convertivel, co2_kg_m3={round(co2,2)}, familia sugerida {l.get("familia_sugerida")}]')
            log.append((rid,r,fck,round(co2,2),l.get('familia_sugerida')))
    print(stats)
    if not dry: wb.save(XL)
    return log
FIGDONE={3105,2895,3120,3153,3238,3133,3420,4033,3439,3203,3176}; FIGLINES={}
EXCLUIR_ART[3133]='material de base biologica; as duas vias de conversao divergem ~50% (Fig.10/0,2 m vs Fig.8 x massa volumica)'
EXCLUIR_ART[3238]='CO2 so por tonelada de ligante; massa volumica da pasta nao impressa (fck 36,4 confirmado na Fig.9)'
EXCLUIR_ART[3420]='Fig.7/8/11 so indices normalizados; Fig.12 ilegivel na copia reduzida'
ALERTA_ART[3153]='eixo da Fig.25 impresso "t-CO2/m3" (impossivel); lido como kg/m3, coerente com a reducao de 6,15% do texto'
ALERTA_ART[3105]='fck aos 35 d (nao ha 28 d); CO2 com electricidade da rede (cenario renovavel mais baixo)'
import re as _re
_fig=json.load(open(SP+'resultado_figuras.json'))
def _n(x):
    if isinstance(x,dict): x=x.get('d35', x.get('grid'))
    if isinstance(x,str): x=_re.split(r'[ /(]',x.strip())[0]
    try: return float(str(x).replace(',','.'))
    except: return None
for _o in _fig:
    rid=_o['row_id']
    if rid in (3120,3133,3238,3420): continue
    L=[]
    for l in _o['leituras']:
        m=_re.search(r'sheet_row (\d+)', l.get('mistura',''))
        co=_n(l.get('co2_kg_m3')); fk=_n(l.get('fck_mpa'))
        if rid==3105 and 'renov' in l.get('mistura',''): continue
        L.append({'sheet_row_existente_ou_null': int(m.group(1)) if m else None,'material':_re.sub(r'\s*-?\s*sheet_row \d+','',l.get('mistura','')).replace('(,','(').replace(' ()','').replace('()','').strip(),
          'fck_mpa':fk,'co2_kg_m3':co,'co2_original':l.get('co2_original') or f"{l.get('co2_kg_m3')} ({l.get('unidade_eixo')})",'co2_original_local':l.get('local'),
          'co2_conversao':'leitura de figura com eixo numerico calibrado ('+str(l.get('incerteza'))+')','confianca':'media' if rid in (3176,4033,3203,2895) else 'baixa','familia_sugerida':None,'fck_local':l.get('local')})
    FIGLINES[rid]=L
if __name__=='__main__':
    lg=run(dry='--apply' not in sys.argv)
    json.dump(lg,open(SP+'aplicado_log.json','w'),ensure_ascii=False,default=str)
    print(len(lg))
