import pandas as pd
import configparser as cp

def render(csv):
    config = cp.ConfigParser()
    config.read_file(open(r'config.ini'))

    styles = config.get('STYLE',option='classic')
    js = config.get('JS',option='sort_functionality')

    file = pd.read_csv(csv, delimiter=';')
    table = file.to_html(classes=['sortable'])
    table += styles
    table += js

    html = open('table.html', 'w')
    html.write(table)
    html.close()

if __name__ == '__main__':
    render('csvtest.csv')

