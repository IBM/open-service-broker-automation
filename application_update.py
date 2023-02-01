import os
import re
import json
import argparse
import logging
import subprocess
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

apikey = os.environ.get("apikey")
region = os.environ.get("region")
resource_group = os.environ.get("resource_group")
ce_project_name = os.environ.get("ce_project_name")


def print_supported_langs():
    print(
        '''
        Supported Languages to generate source code
        =======================================
        |1. Java spring                       |
        |2. python-flask                      |
        |3. scala                             |
        |4. nodejs-server                     |
        |5. go-server                         |
        |6. ruby                              |
        =======================================
        '''
    )


def update_app_in_code_engine(args):
    with open("dockerfiles/{lan}-Dockerfile".format(lan=args.srcCodeLanguage), "r") as file_one:
        patrn = "EXPOSE "
        for line in file_one:
            if re.search(patrn, line):
                port = line.split(patrn)[-1].split("/")[0].replace("\n", "")
                break

    logging.info("updating application in code engine")
    cmd = "./update_codeEngine.sh --apikey {api} --region {region} --resource_group {resource_group} " \
          "--ce_project_name {ce_project_name} --lang {srcCodeLanguage} --git_url {git_url} --port_num {port}".format(
            api=apikey, region=region, resource_group=resource_group, ce_project_name=ce_project_name,
            srcCodeLanguage=args.srcCodeLanguage, git_url=args.git_url, port=port)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if proc.returncode == 0:
        url_list = re.findall(r'(https?://\S*codeengine.appdomain.cloud\S*)', str(out))
        return url_list[0].replace('\\n"', "")
    return "Some error while creating app, needs to be investigated"


if __name__ == "__main__":
    logging.info("updating the code engine")
    parser = argparse.ArgumentParser(description='Input params required to create OSB')
    parser.add_argument('--git_url', '-git_repo_url', help='git repo url', required=True)

    print("select language to generate src code")
    print_supported_langs()
    lang = input("select number for specific language \n")
    with open('supported_langs.json') as json_file:
        langs = json.load(json_file)
    parser.add_argument('--srcCodeLanguage', help='Language to generate src code',
                        default=langs["langs_supported"][lang])

    args = parser.parse_args()
    print(update_app_in_code_engine(args))
