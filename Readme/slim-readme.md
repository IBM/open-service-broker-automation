**Readme for updating server specific code using slim:**

Follow the instructions below to update your server specific code using slim:

1. Log into your Github account and clone the source code from the GitHub repo: https://github.com/OSB-Onboarding/osb-slim-server.
2. Extract the source files in your local system.
3. With the help of the table below, update the file name and function name for each of the tasks that you wish to configure for your service.

| S.No | Task Name                                                     | File Name | Function Name                    |
| ---- | ------------------------------------------------------------- | --------- | -------------------------------- |
| 1    | Get a Service instance                                        | index.php | serviceInstance.get              |
| 2    | Provisioning new service instance                             | index.php | serviceInstance.provision        |
| 3    | Deprovisioning service instance                               | index.php | serviceInstance.deprovision      |
| 4    | Update a service instance                                     | index.php | serviceInstance.update           |
| 5    | Get the latest requested operation state for service instance | index.php | serviceBinding.lastOperation.get |
| 6    | Get a service binding                                         | index.php | serviceBinding.get               |
| 7    | Generate a service binding                                    | index.php | serviceBinding.binding           |
| 8    | Deprovision a service binding                                 | index.php | serviceBinding.unbinding         |
| 9    | Get the latest requested operation state for service binding  | index.php | serviceBinding.lastOperation.get |
| 10   | Get Catalog                                                   | index.php | catalog.get                      |

4. Commit the code changes and push the changes to the main branch.
5. Open the command line terminal and execute the following command to update the broker image and to deploy your service specific code:

   **python3 application_update.py**

**Note**: Ensure that the environment variables are set in the **.env** file.

Enter the number to select your preferred coding language.

Once the script starts running, you will get the following output as shown below:

      python3 application_update.py --git_url=https://github.com/OSB-Onboarding/osb-slim-server
      INFO:updating the code engine
      select language to generate src code
        Supported Languages to generate source code
        =======================================
        |1. spring                            |
        |2. python-flask                      |
        |3. slim                              |
        |4. nodejs-server                     |
        |5. go-server                         |
        |6. ruby                              |
        =======================================
      select number for specific language
      3
      INFO:updating application in code engine
      https://osb-go-server-app.vyy1fq8t3fh.us-south.codeengine.appdomain.cloud

The output of this script is the CodeEngine URL for your service broker. If the URL gets loaded successfully in a browser window, it implies that the service broker is generated successfully.
