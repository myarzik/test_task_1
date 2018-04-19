Feature: authorization API tests

	Background: Setup environment
		Given I set base URL to "http://tv.domru.ru"
		And I add path "api/token/device" to base URL

	Scenario: empty req
		Given empty payload
		When make GET request
		Then the result page will include "200"


