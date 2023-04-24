#!/usr/bin/env python3

import requests
import argparse
import time
from colored import fg, attr
import sys
def status_code_manage(statusCode):
    if statusCode >= 200 and statusCode < 300:
        return f"{fg(10)}{attr(1)}[{statusCode}]"
    elif statusCode >= 300 and statusCode < 400:
        return f"{fg(226)}{attr(1)}[{statusCode}]"
    elif statusCode >= 400 and statusCode < 500:
        return f"{fg(9)}{attr(1)}[{statusCode}]"
    elif statusCode >= 500 and statusCode < 600:
        return f"{fg(212)}{attr(1)}[{statusCode}]"

def valsubs(file, timeout):
    with open(file, 'r') as f:
        for line in f:
            sub = line.strip()
            url = f'https://{sub}'
            try:
               response =  requests.head(url)
               print(url + status_code_manage(response.status_code) + f"{attr(0)}")
               time.sleep(timeout)
            except :
               pass
            
            




if __name__ == '__main__':
    
    print(f'''{fg(87)}{attr(1)}
                             _    __      __           __        
                            | |  / /___ _/ /______  __/ /_  _____
                            | | / / __ `/ / ___/ / / / __ \/ ___/
                            | |/ / /_/ / (__  ) /_/ / /_/ (__  ) 
                            |___/\__,_/_/____/\__,_/_.___/____/  

                                                                version: 1.0

                            
                                                        Created By: @Siradj
                                                        Github: github.com/ahmedsiradj

{attr(0)}''')




    parser = argparse.ArgumentParser(description='Validate Subdomains')
    parser.add_argument('-i', '--input', help='input file')
    parser.add_argument('-t','--timeout', help='timeout',required=False, default=0.20)

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    valsubs(args.input, args.timeout)