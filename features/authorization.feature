Feature: authorization API tests

	Background: Setup environment
		Given I set base URL to "http://tv.domru.ru"
		And I add path "api/token/device" to base URL

	Scenario: empty req
		Given empty payload
		When make GET request
		Then status code will be "200"
		And result will be "0"
		
	Scenario: req with client_id
		Given payload contains "client_id"
		When make GET request
		Then status code will be "200"
		And result will be "0"
	
	Scenario: req with timestamp
		Given payload contains "timestamp"
		When make GET request
		Then status code will be "200"	
		And result will be "0"
		
	Scenario: req with device_id
		Given payload contains "device_id"
		When make GET request
		Then status code will be "200"
		And result will be "0"
		
	Scenario: req with client_id and timestamp
		Given payload contains "client_id,timestamp"
		When make GET request
		Then status code will be "200"
		And result will be "0"
		
	Scenario: req with client_id and device_id
		Given payload contains "client_id,device_id"
		When make GET request
		Then status code will be "200"
		And result will be "0"
		
	Scenario: req with timestamp and device_id
		Given payload contains "timestamp,device_id"
		When make GET request
		Then status code will be "200"
		And result will be "0"		
		
	Scenario: full req
		Given payload contains "client_id,timestamp,device_id"
		When make GET request
		Then status code will be "200"	
		And result will be "1"