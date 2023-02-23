#!/usr/bin/env bash
###############################################################################
# SCRIPT NAME: update_codeEngine.sh
#
# AUTHOR     : Prasad Kasthuri
#
# PURPOSE    : Script to create a project and deploy in codeEngine.
# SYNTAX     : create_codeEngine.sh <API> <Region> <APIKEY> <ResourceGroup>
#
# PARAMETERS : "API", "Region",  "API Key", "ResourceGroup", "Language", "Git url with source code", "Server Port num"
#
# RETURN CODES
#          0 : Successful run 
###############################################################################

Time=`date "+%D %T"`
echo -e "Update code Engine and deployment script started at $Time \n"
set -x 

while [[ $# -gt 0 ]]
  do
    key="$1"
    value="$2"
    case $key in
        --region)
         region=$value
         shift
         shift
         ;;
        --apikey)
         apikey=$value
         shift
         shift
         ;;
        --resource_group)
         resource_group=$value
         shift
         shift
         ;;
        --ce_project_name)
         ce_project_name=$value
         shift
         shift
         ;;
        --lang)
         lang=$value
         shift
         shift
         ;;
        --git_url)
         git_url=$value;
         shift
         shift
         ;;
        --port_num)
          port_num=$value;
          shift
          shift
          ;;
        *)
    esac
done

echo "########## Connecting to IBM Cloud #############"
ibmcloud login -a https://cloud.ibm.com -r "$region" --apikey "$apikey" -g "$resource_group"

echo "########## Selecting Code Engine project, Updating the application revision, build and deployment to IBM Cloud #############"

for ((n=1;n<=10;n++))
    do
        ibmcloud ce project select -n $ce_project_name
        if [ $? -eq 0 ]
            then
              break
        fi
        echo "##### Failed to select the project, Retrying $n attempt  #####"
        sleep 30
    done

# Application port is running on 3000, hence passed listening port number
result=$(ibmcloud ce  app update --name osb-$lang-app --build-source $git_url --build-strategy dockerfile  --cpu 1 --memory 4G --ephemeral-storage 0.4G --min-scale 1 --port $port_num 2>&1)
exit_code=$?
echo $exit_code
if [ $exit_code -eq 0 ]
then
    echo $result
fi
exit $exit_code
#ibmcloud ce  app create --name nodejs-server-test4 --build-source https://github.com/OSB-Hackathon/osb-nodejs-server.git --build-strategy dockerfile  --cpu 1 --memory 4G --ephemeral-storage 0.4G --min-scale 1 --port 3000

#ibmcloud ce  app create --name php-slim-server-test4 --build-source https://github.com/OSB-Hackathon/osb-php-slim-server-1.git --build-strategy dockerfile  --cpu 1 --memory 4G --ephemeral-storage 0.4G --min-scale 1 --port 80
 

#--build-dockerfile Dockerfile

#ibmcloud ce application create --name APP_NAME ((--image IMAGE_REF | (--build-source SOURCE [--image IMAGE_REF])) [--argument ARGUMENT] [--build-commit BUILD_COMMIT] [--build-context-dir BUILD_CONTEXT_DIR] [--build-dockerfile BUILD_DOCKERFILE] [--build-git-repo-secret BUILD_GIT_REPO_SECRET] [--build-size BUILD_SIZE] [--build-strategy BUILD_STRATEGY] [--build-timeout BUILD_TIMEOUT] [--cluster-local] [--command COMMAND] [--concurrency CONCURRENCY] [--concurrency-target CONCURRENCY_TARGET] [--cpu CPU] [--env ENV] [--env-from-configmap ENV_FROM_CONFIGMAP] [--env-from-secret ENV_FROM_SECRET] [--ephemeral-storage EPHEMERAL_STORAGE] [--force] [--max-scale MAX_SCALE] [--memory MEMORY] [--min-scale MIN_SCALE] [--mount-configmap MOUNT_CONFIGMAP] [--mount-secret MOUNT_SECRET] [--no-cluster-local] [--no-wait] [--output OUTPUT] [--port PORT] [--quiet] [--registry-secret REGISTRY_SECRET] [--request-timeout REQUEST_TIMEOUT] [--revision-name REVISION_NAME] [--service-account SERVICE_ACCOUNT] [--user USER] [--visibility VISIBILITY] [--wait] [--wait-timeout WAIT_TIMEOUT]

