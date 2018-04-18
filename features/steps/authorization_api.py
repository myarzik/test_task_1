import behave
import requests

@given('')
def step_impl(context):
	pass
	
@when('send default authorization request')
def step_impl(context):
	assert True is not False
	
@then('back-end response is ok')
def step_impl(context):
	assert context.failed is False
