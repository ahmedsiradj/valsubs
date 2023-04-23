#!/usr/bin/env python3

import requests
import argparse
import time
def valsubs(file):
    with open(file, 'r') as f:
        for line in f:
            sub = line.strip()
            url = f'https://{sub}'
            try:
               response =  requests.head(url)
               print(f"{url} --> {response.status_code}")
               time.sleep(0.15)
            except :
               pass
            
            




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate Subdomains')
    parser.add_argument('-i', '--input', help='input file')
    args = parser.parse_args()
    valsubs(args.input)