###############################################################
# Name : project-setup.py
#
# Project : Accelerating partner service onboarding
#           
# Maintainer : Meetali Solanki, Ankitha 
#
# Description : An automated script to generate and push source
#               code for a service broker using openapi 
#               specifications
###############################################################
### generate server code, mvn install , get the code and build
import os
import re
import json
import argparse
import shutil
import logging
import subprocess
import requests
from git import Repo, Git
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

#variables
release_note = "Initial Source code"
orgs_id = os.environ.get("orgs_id")
git_user_id = os.environ.get("git_user_id")
token = os.environ.get("token")
apikey = os.environ.get("apikey")
region = os.environ.get("region")
resource_group = os.environ.get("resource_group")
ce_project_name = os.environ.get("ce_project_name")
headers = {'Authorization': 'token %s' % token}
user_id = orgs_id if orgs_id else git_user_id

###############################################################
# Initialize variables based on input arguments
###############################################################
def initGlobalVariables(srcCodeLanguage):

    global git_repo_id
    git_repo_id = "osb-"+srcCodeLanguage+"-server"

    global PATH_OF_GIT_REPO
    PATH_OF_GIT_REPO = os.path.join(os.getcwd(), git_repo_id)


# ###############################################################
# # Installs swagger-codegen on local system 
# ###############################################################
def getSwaggerImageandyaml(srcCodeLanguage):

    swaggerCodegenImage="swaggerapi/swagger-codegen-cli"
    openapiYamlPath="https://raw.githubusercontent.com/IBM/open-service-broker-automation/main/swagger-2.0.yaml"
    
    logging.info("Choose the swagger codegen image based for " + srcCodeLanguage)

    if (srcCodeLanguage == "nodejs-server" or  srcCodeLanguage == "go-server") :
        swaggerCodegenImage="swaggerapi/swagger-codegen-cli-v3"
        openapiYamlPath="https://raw.githubusercontent.com/IBM/open-service-broker-automation/main/openapi-3.0.3.yaml"
        #os.path.join(os.getcwd(), "/openapi-3.0.3.yaml")
    
    logging.info("Image being used for is : " + swaggerCodegenImage)
    return (swaggerCodegenImage ,openapiYamlPath)

###############################################################
# Delete/Create a git repository
###############################################################


def verifyRepoExists():
    logging.info("Checking repository already exist or not")
    url = "https://api.github.com/repos/{user_id}/{repo_id}".format(user_id=user_id, repo_id=git_repo_id)
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        logging.info("{} repository already exist".format(git_repo_id))
        return True, url
    return False, ''


def deleteGitRepo():
    url = "https://api.github.com/repos/{user_id}/{repo_id}".format(user_id=user_id, repo_id=git_repo_id)
    resp = requests.delete(url, headers=headers)
    if resp.status_code == 204:
        logging.info("{} repository deleted successfully".format(git_repo_id))
    elif resp.status_code == 403:
        logging.error("Unable to delete repository")
        raise Exception(resp.json()['message'])


def createGitRepo():
    if orgs_id:
        logging.info("creating a git repository in organization {}".format(orgs_id))
        cmd = "curl -u \"" + git_user_id +":" + token +"\" https://api.github.com/orgs/{id}/repos".format(id=orgs_id) + " -d '{\"name\":\"" + git_repo_id + "\"}' "
    else:
        logging.info("creating a git repository ")
        cmd = "curl -u \"" + git_user_id +":" + token +"\" https://api.github.com/user/repos -d '{\"name\":\"" + git_repo_id + "\"}' "
    os.system(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    proc.communicate()
    if proc.returncode != 0:
        raise Exception("error while generating src code")

###############################################################
# generate the project code using <App>-openapi.yaml using 
# swagger-codegen installed in previous step
# Considerations 
###############################################################


def generateProjectCode(srcCodeLanguage):
    logging.info("Generating the source code for {} using the swagger code-generator".format(srcCodeLanguage))

    if os.path.exists(git_repo_id):
        os.system("rm -rf " + git_repo_id)

    os.mkdir(git_repo_id)
    swaggerCodegenImage, openapiYamlPath = getSwaggerImageandyaml(args.srcCodeLanguage)

    cmd = "docker run --rm -v \"" + os.getcwd() + "\":/local " + swaggerCodegenImage + " generate  -i " +openapiYamlPath
    cmd = cmd + " -l " + srcCodeLanguage
    cmd = cmd + " -o " + "/local/" + git_repo_id

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    proc.communicate()
    if proc.returncode != 0:
        raise Exception("error while generating src code")


###############################################################
#Push the source code folder to git
# 
###############################################################


def pushCodeToGithub(srcCodeLanguage):
    logging.info("Updating the local repo with readme and  dockerfile, "
                 "push swagger generated code to github repository")
    git_url = ""

    try:
        shutil.copy('dockerfiles/{lan}-Dockerfile'.format(lan=srcCodeLanguage), PATH_OF_GIT_REPO + '/Dockerfile')
        shutil.copy('Readme/{lan}-readme.md'.format(lan=srcCodeLanguage), PATH_OF_GIT_REPO + '/README.md')
        repo = Repo.init(PATH_OF_GIT_REPO)
        logging.info("add files and commit the changes")
        repo.git.add(".")
        repo.index.commit(release_note)

        logging.info("Add git remote origin")
        if "origin" not in repo.remotes:
            user_id = orgs_id if orgs_id else git_user_id
            o = repo.create_remote(name='origin',
                                   url="https://" + token + "@github.com/" + user_id + "/" + git_repo_id + ".git")
            git_url = "https://github.com/" + user_id + "/" + git_repo_id + ".git"
        else:
            o = repo.remotes.origin
        o.push(repo.active_branch.name)
        logging.info("Completed pushing the code to github repository")
        return git_url
    except Exception as e:
        print('Some error occurred while pushing the code', e)
        logging.exception('Some error occurred while pushing the code', e)


###################################################################
# deploy app in code engine
###################################################################

def deploy_app_in_code_engine(args):
    # run sh script
    with open("dockerfiles/{lan}-Dockerfile".format(lan=args.srcCodeLanguage), "r") as file_one:
        patrn = "EXPOSE "
        for line in file_one:
            if re.search(patrn, line):
                port = line.split(patrn)[-1].split("/")[0].replace("\n", "")
                break

    logging.info("Create and deploy app in code engine")
    cmd = "./create_codeEngine.sh --apikey {api} --region {region} --resource_group {resource_group} " \
          "--ce_project_name {ce_project_name} --lang {srcCodeLanguage} --git_url {git_url} --port_num {port}".format(
            api=apikey, region=region, resource_group=resource_group, ce_project_name=ce_project_name,
            srcCodeLanguage=args.srcCodeLanguage, git_url=args.git_url, port=port)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if proc.returncode == 0:
        url_list = re.findall(r'(https?://\S*codeengine.appdomain.cloud\S*)', str(out))
        return url_list[0].replace('\\n"', "")
    return "Some error while creating app, needs to be investigated"

###################################################################
# print the supported languages
###################################################################


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
        |6. php-slim                          |
        =======================================
        '''
    )

###################################################################


if __name__ == "__main__":
    #getSwaggerCodegen()
    parser = argparse.ArgumentParser(description='Input params required to create OSB')

    print_supported_langs()
    lang = input("select number for specific language \n")
    with open('supported_langs.json') as json_file:
        langs = json.load(json_file)
    parser.add_argument('--srcCodeLanguage', help='Language to generate src code',
                        default=langs["langs_supported"][lang])

    args = parser.parse_args()
    initGlobalVariables(args.srcCodeLanguage)
    repo_exists, git_repo_url = verifyRepoExists()
    if repo_exists:
        option = input('''
        =======================================
        |1. Do you want to continue with existing code repo, press c  |
        |2. Do you want to delete and recreate the code repo, press d |
        |3. Do you want to quit the run, press q                      |
        =======================================
        ''')
        if option == 'd':
            deleteGitRepo()
            createGitRepo()
            generateProjectCode(args.srcCodeLanguage)
            git_repo_url = pushCodeToGithub(args.srcCodeLanguage)
        elif option == 'c':
            pass
        elif option == 'q':
            quit()
        else:
            quit("Quiting the execution as did not provide the required option")
    else:
        createGitRepo()
        generateProjectCode(args.srcCodeLanguage)
        git_repo_url = pushCodeToGithub(args.srcCodeLanguage)

    if not git_repo_url:
        raise Exception("Error while pushing the src code to github")
    parser.add_argument('--git_url', help='git repo url', default=git_repo_url)
    args = parser.parse_args()
    print(deploy_app_in_code_engine(args))
    print(git_repo_url)
