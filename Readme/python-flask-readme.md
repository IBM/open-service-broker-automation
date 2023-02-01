**Readme for updating server specific code using Python:**

Follow the instructions below to update your server specific code using Python:

1. Log into your Github account and clone the source code from the GitHub repo: https://github.com/OSB-Hackathon/osb-python-flask-server.
2. Extract the source files in your local system.
3. With the help of the table below, create your service specific code by updating the file name and function name for each of the tasks that you wish to configure for your service.

| S.No | Task Name                                                     | File Name                       | Function Name                       |
|------|---------------------------------------------------------------|---------------------------------|-------------------------------------|
| 1    | Get a Service instance                                        | service_instances_controller.py | service_instance_get                |
| 2    | Provisioning new service instance                             | service_instances_controller.py | service_instance_provision          |
| 3    | Deprovisioning service instance                               | service_instances_controller.py | service_instance_deprovision        |
| 4    | Update a service instance                                     | service_instances_controller.py | service_instance_update             |
| 5    | Get the latest requested operation state for service instance | service_instances_controller.py | service_instance_last_operation_get |
| 6    | Get a service binding                                         | service_bindings_controller.py  | service_binding_get                 |
| 7    | Generate a service binding                                    | service_bindings_controller.py  | service_binding_binding             |
| 8    | Deprovision a service binding                                 | service_bindings_controller.py  | service_binding_unbinding           |
| 9    | Get the latest requested operation state for service binding  | service_bindings_controller.py  | service_binding_last_operation_get  |
| 10   | Get Catalog                                                   | catalog_controller.py           | catalog_get                         |

4. Commit the code changes and push the changes to the main branch.
5. Open the command line terminal and execute the following command to update the broker image and to deploy your service specific code:

   **python3 application_update.py**

**Note**: Ensure that the environment variables are set in the **.env** file.

Enter the number to select your preferred coding language.

Once the script starts running, you will get the following output as shown below:

      python3 application_update.py --git_url=https://github.com/OSB-Hackathon/osb-python-flask-server
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
      2
      INFO:updating application in code engine 
      https://osb-go-server-app.vyy1fq8t3fh.us-south.codeengine.appdomain.cloud
  
The output of this script is the CodeEngine URL for your service broker. If the URL gets loaded successfully in a browser window, it implies that the service broker is generated successfully.

