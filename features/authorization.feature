Feature: check request

	Scenario: run request test
		Given we have behave installed
		When send default authorization request
		Then back-end response is ok
