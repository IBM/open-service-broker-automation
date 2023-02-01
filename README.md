# open-service-broker-automation

**Overview**

Service brokers manage the lifecycle of services. Platforms interact with service brokers to create, get access to, and manage the services they offer. The Open Service Broker API defines these interactions to allow software providers to offer their services to anyone regardless of the technology or infrastructure those software providers choose.

The software automates the process of configuring and deploying a broker service that has your required specifications.

**Before you begin:**

Ensure that the following pre-requisites are met before you use the script:

1. You must have an IBM Cloud account where the service needs to be on-boarded.
2. Access to IBM Cloud Code Engine.
3. Access to the GitHub account, where the source code is pushed to.
4. Set the following environment variables to run the script in the .env file.

   Note: All the environment variables are mandatory.

   a. Variable name: git_user_id: Specify the GIT username for the account, where the source code is pushed to.

   b. Variable name: token: Create and specify the Git Token with the following permissions:

   Access to all the repos - Provides full control of private repositories.

   Workflow access: workflow - To update GitHub action workflows.

   Write packages: write:packages - To upload packages to Github package repository.

   Delete packages: delete:packages - To delete packages from Github package repository.

   c. Variable name: apikey: Create your cloud API Key by using the link: Creating API Key and assign the following permissions using IBM Cloud Identity and Access Management (IAM) and specify it in the apikey field:

   Administrator access for the Catalog Management service

   Editor access for the Partner Center - Sell service

   Editor access for the IAM Access Groups service

   Editor access for IBM Cloud Code Engine

   Editor access for IBM Container Registry

   d. Variable name: region: Specify the region where you wish to deploy your CodeEngine project.

   e. Variable name: resource_group: Specify the resource where you wish to deploy your CodeEngine project or specify Default to deploy it in the Default resource group.

**Required resources**
To run the software, the following resources are required:

1. Install Python Version 3.
2. Setup Docker locally on your computer by following the instructions in this link: https://docs.docker.com/engine/install/
3. Install IBM Cloud Command Line Interface (CLI) and add Code Engine (CE) plugin.

**Installing the software**

Download the software from the Github repo link: https://github.com/IBM/open-service-broker-automation

To install the software, follow the steps below:

1. Open the command line interface.
2. Navigate to the path, where you have downloaded the script.
3. Execute the following command: python3 project-setup.py
4. Enter the number to select your preferred coding language.
5. Once the script starts running, you will get the following output as shown below:

INFO:Generating the source code for go-server using the swagger code-generator docker run --rm -v /Users/local swaggerapi/swagger-codegen-cli-v3 generate -i https://raw.githubusercontent.com/openservicebrokerapi/servicebroker/master/openapi.yaml -l go-server -o /local/osb-go-server-server INFO:Updating the local repo with readme and dockerfile, push swagger generated code to github repository INFO:add files and commit the changes INFO:Add git remote origin INFO:Completed pushing the code to github repository INFO:Create and deploy app in code engine ./create_codeEngine.sh --apikey mt64-xjeL1on8EkUkA6g68MXYyBGW3TqxugKC84kIl-0 --region us-south --resource_group Default --lang go-server --git_url https://github.com/OSB-Hackathon/osb-go-server-server.git --port_num 8080 https://test-go-server-app.vyy1fq8t3fh.us-south.codeengine.appdomain.cloud https://github.com/OSB-Hackathon/osb-go-server-server.git

The output of this script is an URL for the service broker, along with the CodeEngine URL. If the URL gets loaded successfully in a browser window, it implies that the service broker is generated successfully.

https://test-go-server-app.vyy1fq8t3fh.us-south.codeengine.appdomain.cloud - Sample URL for the service broker.

https://github.com/OSB-Hackathon/osb-go-server-server.git - Sample URL for the Gitrepo, where the code is pushed to.

6. Once you get the service broker URL, you can proceed with configuring the Broker service in IBM Partner Center for your Service under the Broker tab by clicking on Add Broker and specifying the broker URL.

**Next steps**

Once you have completed building the broker image, navigate to the Github location, where the code engine script is hosted, and follow the steps mentioned in the Readme file to update your service specific code for the broker.
