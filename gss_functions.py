import numpy as np

def columns():

    return [
    'year',
    'id',
    'wrkstat',
    'divorce',
    'marital',
    'martype',
    'sibs',
    'childs',
    'age',
    'educ',
    'degree',
    'sex',
    'race',
    'racecen1',
    'racecen2',
    'racecen3',
    'res16',
    'reg16',
    'adults',
    'income',
    'rincome',
    'region',
    'srcbelt',
    'partyid',
    'pres96',
    'pres00',
    'pres04',
    'pres08',
    'pres12',
    'polviews',
    'natspac',
    'natenvir',
    'natheal',
    'natcity',
    'natcrime',
    'natdrug',
    'nateduc',
    'natrace',
    'natarms',
    'nataid',
    'natfare',
    'natroad',
    'natsoc',
    'natmass',
    'natpark',
    'natchld',
    'natsci',
    'natenrgy',
    'spkath',
    'colath',
    'libath',
    'spksoc',
    'colsoc',
    'libsoc',
    'spkrac',
    'colrac',
    'librac',
    'spkcom',
    'colcom',
    'libcom',
    'spkmil',
    'colmil',
    'libmil',
    'spkhomo',
    'colhomo',
    'libhomo',
    'spkmslm',
    'colmslm',
    'libmslm',
    'cappun',
    'gunlaw',
    'grass',
    'relig',
    'fund',
    'attend',
    'reliten',
    'postlife',
    'pray',
    'popespks',
    'relig16',
    'prayer',
    'bible',
    'racmar',
    'racdin',
    'racpush',
    'racseg',
    'racopen',
    'raclive',
    'racclos',
    'racdis',
    'racinteg',
    'rachome',
    'racschol',
    'racfew',
    'rachaf',
    'racmost',
    'racpres',
    'racchurh',
    'affrmact',
    'happy',
    'hapmar',
    'health',
    'life',
    'helpful',
    'fair',
    'trust',
    'confinan',
    'conbus',
    'conclerg',
    'coneduc',
    'confed',
    'conlabor',
    'conpress',
    'conmedic',
    'contv',
    'conjudge',
    'consci',
    'conlegis',
    'conarmy',
    'satjob',
    'class',
    'satfin',
    'finrela',
    'union',
    'fehome',
    'fework',
    'fepres',
    'fepol',
    'abdefect',
    'abnomore',
    'abhlth',
    'abpoor',
    'abrape',
    'absingle',
    'abany',
    'chldidel',
    'sexeduc',
    'divlaw', # replaced 2021 with divlawnv and divlawv p. 245
    'divlawv',
    'famdif16',
    'divlawnv',
    'premarsx',
    'teensex',
    'xmarsex',
    'homosex',
    'pornlaw',
    'spanking',
    'letdie1',
    'polhitok',
    'polabuse',
    'polmurdr',
    'polescap',
    'polattak',
    'fear',
    'owngun',
    'pistol',
    'rowngun',
    'hunt',
    'phone',
    'fechld',
    'fehelp',
    'fepresch',
    'fefam',
    'racdif1',
    'racdif2',
    'racdif3',
    'racdif4',
    'god',
    'reborn',
    'savesoul',
    'racwork',
    'fejobaff',
    'discaffm',
    'discaffw',
    'fehire',
    'relpersn',
    'sprtprsn',
    'relexp',
    'spklang',
    'compuse',
    'hrsrelax',
    'trdunion',
    'wkracism',
    'wksexism',
    'wkharsex',
    'databank',
    'goodlife',
    'meovrwrk',
    'miracles',
    'relexper',
    'relactiv',
    'matesex',
    'frndsex',
    'acqntsex',
    'pikupsex',
    'paidsex',
    'othersex',
    'sexsex',
    'sexfreq',
    'sexsex5',
    'sexornt',
    'hhrace',
    'cohort',
    'ballot',
    'wtssall',
    'wtssps',
    'sexbirth',
    'sexnow',
    'eqwlth',
    'realinc',
    'realrinc',
    'coninc',
    'conrinc',
    'commun',
    'cantrust',
    'zodiac',
    ]

# Most of the code in this block comes from:
#  https://github.com/AllenDowney
    

def values(series):
    """Count the values and sort.

    series: pd.Series

    returns: series mapping from values to frequencies
    """
    return series.value_counts().sort_index()

def decorate(**options):
    """Decorate the current axes.
    Call decorate with keyword arguments like
    decorate(title='Title',
             xlabel='x',
             ylabel='y')
    The keyword arguments can be any of the axis properties
    https://matplotlib.org/api/axes_api.html
    """
    plt.gca().set(**options)
    plt.tight_layout()
    
from statsmodels.nonparametric.smoothers_lowess import lowess

def make_lowess(series, **options):
    """Use LOWESS to compute a smooth line.
    
    series: pd.Series
    
    returns: pd.Series
    """
    y = series.values
    x = series.index.values

    smooth = lowess(y, x, **options)
    index, data = np.transpose(smooth)

    return pd.Series(data, index=index) 

def plot_series_lowess(series, color):
    """Plots a series of data points and a smooth line.
    
    series: pd.Series
    color: string or tuple
    """
    series.plot(linewidth=0, marker='o', color=color, alpha=0.5)
    smooth = make_lowess(series)
    smooth.plot(label='_', color=color, lw=4)
    
def plot_columns_lowess(table, columns, color_map):
    """Plot the columns in a DataFrame.
    
    table: DataFrame with a cross tabulation
    columns: list of column names, in the desired order
    color_map: mapping from column names to color_map
    """
    for col in columns:
        series = table[col]
        plot_series_lowess(series, color_map[col])
        
        
def ignore_warnings():
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.filterwarnings("ignore")

NA = np.nan

def replace_invalid(df, columns, bad):
    for column in columns:
        df[column].replace(bad, NA, inplace=True)


def gss_replace_invalid(df):
    """Replace invalid data with NaN.

    df: DataFrame
    """
    # different variables use different codes for invalid data
    df.cohort.replace([0, 9999], NA, inplace=True)

    # since there are a lot of variables that use 0, 8, and 9 for invalid data,
    # I'll use a loop to replace all of them
    columns = [
        "abany",
        "abdefect",
        "abhlth",
        "abnomore",
        "abpoor",
        "abrape",
        "absingle",
        "acqntsex",
        "affrmact",
        "bible",
        "cappun",
        "colath",
        "colcom",
        "colhomo",
        "colmil",
        "colmslm",
        "colrac",
        "colsoc",
        "compuse",
        "conarmy",
        "conbus",
        "conclerg",
        "coneduc",
        "confed",
        "confinan",
        "conjudge",
        "conlabor",
        "conlegis",
        "conmedic",
        "conpress",
        "consci",
        "contv",
        "databank",
        "discaffm",
        "discaffw",
        "divlaw",
        "divlawv",
        "divlawnv",
        "divorce",
        "eqwlth",
        "fair",
        "fear",
        "fechld",
        "fefam",
        "fehelp",
        "fehire",
        "fehome",
        "fejobaff",
        "fepol",
        "fepres",
        "fepresch",
        "fework",
        "finrela",
        "frndsex",
        "fund",
        "god",
        "goodlife",
        "grass",
        "gunlaw",
        "hapmar",
        "happy",
        "health",
        "helpful",
        "hhrace",
        "homosex",
        "hunt",
        "libath",
        "libcom",
        "libhomo",
        "libmil",
        "libmslm",
        "librac",
        "libsoc",
        "life",
        "matesex",
        "meovrwrk",
        "miracles",
        "nataid",
        "natarms",
        "natchld",
        "natcity",
        "natcrime",
        "natdrug",
        "nateduc",
        "natenrgy",
        "natenvir",
        "natfare",
        "natheal",
        "natmass",
        "natpark",
        "natrace",
        "natroad",
        "natsci",
        "natsoc",
        "natspac",
        "othersex",
        "paidsex",
        "pikupsex",
        "polabuse",
        "polattak",
        "polescap",
        "polhitok",
        "polmurdr",
        "polviews",
        "popespks",
        "pornlaw",
        "postlife",
        "pray",
        "prayer",
        "premarsx",
        "pres00",
        "pres04",
        "pres08",
        "pres12",
        "pres96",
        "racchurh",
        "racclos",
        "racdif1",
        "racdif2",
        "racdif3",
        "racdif4",
        "racdin",
        "racdis",
        "racfew",
        "rachaf",
        "rachome",
        "racinteg",
        "raclive",
        "racmar",
        "racmost",
        "racopen",
        "racpres",
        "racpush",
        "racschol",
        "racseg",
        "racwork",
        "reborn",
        "relexp",
        "relexper",
        "reliten",
        "relpersn",
        "res16",
        "rowngun",
        "satfin",
        "satjob",
        "savesoul",
        "sexbirth",
        "sexeduc",
        "sexnow",
        "sexornt",
        "sexsex",
        "sexsex5",
        "spanking",
        "spkath",
        "spkcom",
        "spkhomo",
        "spklang",
        "spkmil",
        "spkmslm",
        "spkrac",
        "spksoc",
        "sprtprsn",
        "teensex",
        "trdunion",
        "trust",
        "union",
        "wkharsex",
        "wkracism",
        "wksexism",
        "xmarsex",
        "commun",
    ]
    replace_invalid(df, columns, [0, 8, 9])

    columns = ["degree", "partyid"]
    replace_invalid(df, columns, [8, 9])

    df.phone.replace([0, 2, 9], NA, inplace=True)
    df.owngun.replace([0, 3, 8, 9], NA, inplace=True)
    df.pistol.replace([0, 3, 8, 9], NA, inplace=True)
    df["class"].replace([0, 5, 8, 9], NA, inplace=True)

    df.chldidel.replace([-1, 8, 9], NA, inplace=True)
    df.sexfreq.replace([-1, 8, 9], NA, inplace=True)

    df.attend.replace([9], NA, inplace=True)
    df.childs.replace([9], NA, inplace=True)
    df.adults.replace([9], NA, inplace=True)

    df.age.replace([0, 98, 99], NA, inplace=True)
    df.relig.replace([0, 98, 99], NA, inplace=True)
    df.relig16.replace([0, 98, 99], NA, inplace=True)
    df.relactiv.replace([0, 98, 89], NA, inplace=True)

    # note: sibs contains some unlikely numbers
    df.sibs.replace([-1, 98, 99], NA, inplace=True)
    df.hrsrelax.replace([-1, 98, 99], NA, inplace=True)

    df.educ.replace([97, 98, 99], NA, inplace=True)

    df.realinc.replace([0], NA, inplace=True)
    df.realrinc.replace([0], NA, inplace=True)

    df.income.replace([0, 13, 98, 99], NA, inplace=True)
    df.rincome.replace([0, 13, 98, 99], NA, inplace=True)

    # check that we've cleaned all columns that need it;
    # all columns we've added NaN to should be floats

