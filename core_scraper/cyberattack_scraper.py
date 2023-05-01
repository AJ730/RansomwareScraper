import numpy as np
import pandas as pd


def scrape_cyberattack():

    df = pd.read_csv('../cyberattacks/cyberattacks.csv', sep=';')

    #These are useless columns
    df = df.drop(columns=['Individual(s) name(s) leaked/exposed', 'Address(es) leaked/exposed','Level of digital intensity'
                          ,'Organisation size',  'Prevention, Detection and Recovery' , 'Improper network segmentation',
                          'Inappropriate remote access','Absence of encryption','Detector','Restructuring after attack',
                          'Free identity or credit theft monitoring','Additional disclosure of information',
                          'Number of users affected','Overall nature of attack','Impact on data',
                          'Aspect of Confidentiality-Integrity-Availability triad affected','Other personally identifiable information (PII) leaked/exposed',
                          'Track 1 - Credit card details leaked/exposed','Track 2 - Credit card details leaked/exposed',
                            'Social security number/tax number leaked/exposed','Subsequent fraudulent use of data', 'Investigation',
                          'Undertook investigation', 'Litigation by public', 'Cyber security role', 'Bribe/ransom paid',
                          'Cyber security frameworks', 'Education and awareness policy','Policy',
                          'Penalties/settlement paid or actions imposed','Imposed penalties or actions on organisation',
                          'Fines issued by government or relevant body','Settlement paid',
                          'Effect on share price', 'Unnamed: 43'
                          ])

    pattern = r"[mM][aA][lL][wW][aA][rR][eE]|[rR][aA][nN][sS][oO][mM][wW][aA][rR][eE]"
    mask = np.column_stack([df['Summary'].str.contains(pattern, na=False) for col in df])
    df = df.loc[mask.any(axis=1)]

    df.to_csv('../cyberattacks/refined_cyberattacks.csv', index=False)



if __name__ == '__main__':
    scrape_cyberattack()