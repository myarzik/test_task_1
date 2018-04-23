import behave
import requests

@step('empty payload')
def step_impl(context):
	context.payload=('')
	
@step('payload contains "{payload}"')
def step_impl(context, payload):
	context.payload={}
	if 'client_id' in payload:
		context.payload.update({'client_id': 'er_ottweb_device'})
	if 'timestamp' in payload:
		context.payload.update({'timestamp': 1497861974})
	if 'device_id' in payload:
		context.payload.update({'device_id': 123})
	print(payload)
	
@step('"{payload}" are incorrect')
def step_impl(context, payload):
	context.payload={}
	if 'client_id' in payload:
		context.payload.update({'client_id': 'azaz'})
	if 'timestamp' in payload:
		context.payload.update({'timestamp': 'azaz'})
	if 'device_id' in payload:
		context.payload.update({'device_id': 'azaz'})
	print(payload)
	

@step('status code will be "{status}"')
def step_impl(context, status):
	assert context.r.status_code==int(status), 'Wrong status'
	
@step('result will be "{result}"')
def step_impl(context, result):
	context.rjson=context.r.json()
	assert context.rjson['result']==int(result), 'Wrong result'