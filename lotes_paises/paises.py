"""Normalizacao de paises para o mapa de publicacoes (2026-10-13).

Nome tal como aparece na fonte (Web of Science, Crossref, PDF) -> (nome em portugues, ISO 3166-1 alfa-3).
Inglaterra, Escocia e Pais de Gales contam como Reino Unido (o mapa e por pais soberano).
"""

PAISES = {
    'Argentina': ('Argentina', 'ARG'), 'Australia': ('Australia', 'AUS'), 'Austria': ('Austria', 'AUT'),
    'Bangladesh': ('Bangladesh', 'BGD'), 'Belgium': ('Belgica', 'BEL'), 'Brazil': ('Brasil', 'BRA'),
    'Brasil': ('Brasil', 'BRA'), 'Canada': ('Canada', 'CAN'), 'Chile': ('Chile', 'CHL'),
    'China': ('China', 'CHN'), 'Peoples R China': ('China', 'CHN'), 'Colombia': ('Colombia', 'COL'),
    'Czech Republic': ('Chequia', 'CZE'), 'Czechia': ('Chequia', 'CZE'), 'Denmark': ('Dinamarca', 'DNK'),
    'Ecuador': ('Equador', 'ECU'), 'Egypt': ('Egipto', 'EGY'), 'England': ('Reino Unido', 'GBR'),
    'Scotland': ('Reino Unido', 'GBR'), 'Wales': ('Reino Unido', 'GBR'), 'North Ireland': ('Reino Unido', 'GBR'),
    'UK': ('Reino Unido', 'GBR'), 'United Kingdom': ('Reino Unido', 'GBR'), 'Estonia': ('Estonia', 'EST'),
    'Ethiopia': ('Etiopia', 'ETH'), 'Finland': ('Finlandia', 'FIN'), 'France': ('Franca', 'FRA'),
    'Germany': ('Alemanha', 'DEU'), 'Ghana': ('Gana', 'GHA'), 'Greece': ('Grecia', 'GRC'),
    'Hungary': ('Hungria', 'HUN'), 'India': ('India', 'IND'), 'Indonesia': ('Indonesia', 'IDN'),
    'Iran': ('Irao', 'IRN'), 'Iraq': ('Iraque', 'IRQ'), 'Ireland': ('Irlanda', 'IRL'), 'Israel': ('Israel', 'ISR'),
    'Italy': ('Italia', 'ITA'), 'Japan': ('Japao', 'JPN'), 'Jordan': ('Jordania', 'JOR'),
    'Korea': ('Coreia do Sul', 'KOR'), 'South Korea': ('Coreia do Sul', 'KOR'), 'Latvia': ('Letonia', 'LVA'),
    'Lebanon': ('Libano', 'LBN'), 'Lithuania': ('Lituania', 'LTU'), 'Luxembourg': ('Luxemburgo', 'LUX'),
    'Malaysia': ('Malasia', 'MYS'), 'Mexico': ('Mexico', 'MEX'), 'Morocco': ('Marrocos', 'MAR'),
    'Netherlands': ('Paises Baixos', 'NLD'), 'New Zealand': ('Nova Zelandia', 'NZL'), 'Nigeria': ('Nigeria', 'NGA'),
    'Norway': ('Noruega', 'NOR'), 'Pakistan': ('Paquistao', 'PAK'), 'Peru': ('Peru', 'PER'),
    'Philippines': ('Filipinas', 'PHL'), 'Poland': ('Polonia', 'POL'), 'Portugal': ('Portugal', 'PRT'),
    'Qatar': ('Catar', 'QAT'), 'Russia': ('Russia', 'RUS'), 'Saudi Arabia': ('Arabia Saudita', 'SAU'),
    'Serbia': ('Servia', 'SRB'), 'Singapore': ('Singapura', 'SGP'), 'Slovakia': ('Eslovaquia', 'SVK'),
    'Slovenia': ('Eslovenia', 'SVN'), 'South Africa': ('Africa do Sul', 'ZAF'), 'Spain': ('Espanha', 'ESP'),
    'Sri Lanka': ('Sri Lanka', 'LKA'), 'Sweden': ('Suecia', 'SWE'), 'Switzerland': ('Suica', 'CHE'),
    'Thailand': ('Tailandia', 'THA'), 'Turkey': ('Turquia', 'TUR'), 'Turkiye': ('Turquia', 'TUR'),
    'U Arab Emirates': ('Emirados Arabes Unidos', 'ARE'), 'United Arab Emirates': ('Emirados Arabes Unidos', 'ARE'),
    'USA': ('Estados Unidos', 'USA'), 'United States': ('Estados Unidos', 'USA'), 'Vietnam': ('Vietname', 'VNM'),
    'Cuba': ('Cuba', 'CUB'), 'Croatia': ('Croacia', 'HRV'), 'Taiwan': ('Taiwan', 'TWN'), 'Hong Kong': ('China', 'CHN'),
}

# nomes em portugues (dos resultados da leitura dos PDFs) -> chave acima
PT = {v[0].lower(): v for v in PAISES.values()}
PT.update({'egito': ('Egipto', 'EGY'), 'irã': ('Irao', 'IRN'), 'irao': ('Irao', 'IRN'), 'coreia': ('Coreia do Sul', 'KOR'),
           'república checa': ('Chequia', 'CZE'), 'chéquia': ('Chequia', 'CZE'), 'eua': ('Estados Unidos', 'USA'),
           'estados unidos da américa': ('Estados Unidos', 'USA'), 'países baixos': ('Paises Baixos', 'NLD'),
           'holanda': ('Paises Baixos', 'NLD'), 'suíça': ('Suica', 'CHE'), 'suécia': ('Suecia', 'SWE'),
           'frança': ('Franca', 'FRA'), 'itália': ('Italia', 'ITA'), 'índia': ('India', 'IND'),
           'japão': ('Japao', 'JPN'), 'polónia': ('Polonia', 'POL'), 'polônia': ('Polonia', 'POL'),
           'bélgica': ('Belgica', 'BEL'), 'grécia': ('Grecia', 'GRC'), 'malásia': ('Malasia', 'MYS'),
           'méxico': ('Mexico', 'MEX'), 'nova zelândia': ('Nova Zelandia', 'NZL'), 'letónia': ('Letonia', 'LVA'),
           'lituânia': ('Lituania', 'LTU'), 'estónia': ('Estonia', 'EST'), 'eslováquia': ('Eslovaquia', 'SVK'),
           'eslovénia': ('Eslovenia', 'SVN'), 'sérvia': ('Servia', 'SRB'), 'canadá': ('Canada', 'CAN'),
           'áustria': ('Austria', 'AUT'), 'austrália': ('Australia', 'AUS'), 'colômbia': ('Colombia', 'COL'),
           'tailândia': ('Tailandia', 'THA'), 'finlândia': ('Finlandia', 'FIN'), 'noruega': ('Noruega', 'NOR'),
           'dinamarca': ('Dinamarca', 'DNK'), 'irlanda': ('Irlanda', 'IRL'), 'arábia saudita': ('Arabia Saudita', 'SAU'),
           'emirados árabes unidos': ('Emirados Arabes Unidos', 'ARE'), 'paquistão': ('Paquistao', 'PAK'),
           'vietnã': ('Vietname', 'VNM'), 'catar': ('Catar', 'QAT'), 'líbano': ('Libano', 'LBN'),
           'jordânia': ('Jordania', 'JOR'), 'etiópia': ('Etiopia', 'ETH'), 'nigéria': ('Nigeria', 'NGA'),
           'áfrica do sul': ('Africa do Sul', 'ZAF'), 'rússia': ('Russia', 'RUS'), 'turquia': ('Turquia', 'TUR'),
           'singapura': ('Singapura', 'SGP'), 'hungria': ('Hungria', 'HUN'), 'alemanha': ('Alemanha', 'DEU'),
           'espanha': ('Espanha', 'ESP'), 'reino unido': ('Reino Unido', 'GBR'), 'brasil': ('Brasil', 'BRA'),
           'portugal': ('Portugal', 'PRT'), 'china': ('China', 'CHN'), 'equador': ('Equador', 'ECU'),
           'marrocos': ('Marrocos', 'MAR'), 'indonésia': ('Indonesia', 'IDN'), 'cuba': ('Cuba', 'CUB'),
           'chile': ('Chile', 'CHL'), 'croácia': ('Croacia', 'HRV'), 'república tcheca': ('Chequia', 'CZE'),
           'filipinas': ('Filipinas', 'PHL'), 'líbano': ('Libano', 'LBN'), 'estados unidos': ('Estados Unidos', 'USA'), 'peru': ('Peru', 'PER'), 'argentina': ('Argentina', 'ARG')})


def normaliza(nome):
    """Devolve (nome_pt, iso3) ou None."""
    if not nome:
        return None
    n = nome.strip().rstrip('.')
    if n in PAISES:
        return PAISES[n]
    return PT.get(n.lower())
