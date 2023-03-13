**Readme for updating server specific code using NodeJs:**

Follow the instructions below to update your server specific code using NodeJs:

1. Log into your Github account and clone the source code from the GitHub repo: https://github.com/OSB-Onboarding/osb-nodejs-server-server.
2. Extract the source files in your local system.
3. Make the following code change in index.js file to accept encoded path.

```
  // Add these lines below var http = require('http');
  var bodyParser = require("body-parser");
  var cors = require("cors");

  // Add the code below var app = expressAppConfig.getApp();

  app.use(cors());
  app.use(bodyParser.urlencoded({ extended: false }));
  app.use(bodyParser.json());
```

4. With the help of the table below, create your service specific code by updating the file name and function name for each of the tasks that you wish to configure for your service.

**Open Service Broker API Specifications for NodeJs:**

| S.No | Task Name                                                     | File Name                        | Function Name                           |
| ---- | ------------------------------------------------------------- | -------------------------------- | --------------------------------------- |
| 1    | Get a Service instance                                        | controllers/ ServiceInstances.js | serviceInstanceGetUsingGET              |
| 2    | Provisioning new service instance                             | controllers/ ServiceInstances.js | serviceInstanceProvisionUsingPUT        |
| 3    | Deprovisioning service instance                               | controllers/ ServiceInstances.js | serviceInstanceDeprovisionUsingDELETE   |
| 4    | Update a service instance                                     | controllers/ ServiceInstances.js | serviceInstanceUpdateUsingPATCH         |
| 5    | Get the latest requested operation state for service instance | controllers/ ServiceInstances.js | serviceInstanceLastOperationGetUsingGET |
| 6    | Get a service binding                                         | controllers/ ServiceBindings.js  | serviceBindingGetUsingGET               |
| 7    | Generate a service binding                                    | controllers/ ServiceBindings.js  | serviceBindingBindingUsingPUT           |
| 8    | Deprovision a service binding                                 | controllers/ ServiceBindings.js  | serviceBindingUnbindingUsingDELETE      |
| 9    | Get the latest requested operation state for service binding  | controllers/ ServiceBindings.js  | serviceBindingLastOperationGetUsingGET  |
| 10   | Get Catalog                                                   | controllers/Catalog.js           | catalogGetUsingGET                      |

5. Commit the code changes and push the changes to the main branch.
6. Open the command line terminal and execute the following command to update the broker image and to deploy your service specific code:

   **python3 application_update.py**

**Note**: Ensure that the environment variables are set in the **.env** file.

Enter the number to select your preferred coding language.

Once the script starts running, you will get the following output as shown below:

      python3 application_update.py --git_url=https://github.com/OSB-Onboarding/osb-nodejs-server-server
      INFO:updating the code engine
      select language to generate src code
        Supported Languages to generate source code
        =======================================
        |1. spring                            |
        |2. python-flask                      |
        |3. scala                             |
        |4. nodejs-server                     |
        |5. go-server                         |
        |6. ruby                              |
        =======================================
      select number for specific language
      4
      INFO:updating application in code engine
      https://osb-go-server-app.vyy1fq8t3fh.us-south.codeengine.appdomain.cloud

The output of this script is the CodeEngine URL for your service broker. If the URL gets loaded successfully in a browser window, it implies that the service broker is generated successfully.

**Note**: To run the code locally, first do npm install and then npm start. Visit http://localhost:8080/
