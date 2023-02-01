# read -p "Please enter the URL : " url
export url=$1
echo "URL entered : ${url}" 

echo "Get Catalog"
curl -X GET "${url}/v2/catalog" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Get Service Instance"
curl -X GET "${url}/v2/service_instances/instance_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Put Service Instance"
curl -X PUT "${url}/v2/service_instances/instance_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17" -H "Content-Type: application/json" -d "{\"context\":{},\"organization_guid\":\"string\",\"parameters\":{},\"plan_id\":\"string\",\"service_id\":\"string\",\"space_guid\":\"string\"}"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Delete Service Instance"
curl -X DELETE "${url}/v2/service_instances/instance_id?service_id=service_id&plan_id=plan_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Patch Service Instance"
curl -X PATCH "${url}/v2/service_instances/instance_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17" -H "Content-Type: application/json" -d "{\"context\":{},\"parameters\":{},\"plan_id\":\"string\",\"previous_values\":{\"organization_id\":\"string\",\"plan_id\":\"string\",\"service_id\":\"string\",\"space_id\":\"string\"},\"service_id\":\"string\"}"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Get the last requested operation state for service instance"
curl -X GET "${url}/v2/service_instances/instance_id/last_operation" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Get a service binding"
curl -X GET "${url}/v2/service_instances/instance_id/service_bindings/binding_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Generate a service binding"
curl -X PUT "${url}/v2/service_instances/instance_id/service_bindings/binding_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17" -H "Content-Type: application/json" -d "{\"app_guid\":\"string\",\"bind_resource\":{\"app_guid\":\"string\",\"route\":\"string\"},\"context\":{},\"parameters\":{},\"plan_id\":\"string\",\"predecessor_binding_id\":\"string\",\"service_id\":\"string\"}"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Deprovision a service binding"
curl -X DELETE "${url}/v2/service_instances/instance_id/service_bindings/binding_id?service_id=service_id&plan_id=plan_id" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'

echo "Get the last requested operation state for service binding"
curl -X GET "${url}/v2/service_instances/instance_id/service_bindings/binding_id/last_operation" -H "accept: application/json" -H "X-Broker-API-Version: 2.17"
cat headers | head -n 1 | cut '-d ' '-f2'