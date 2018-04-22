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
	

@step ('make GET request')
def step_impl(context):
	context.r=requests.get(context.base_url, params=context.payload)
	assert context.r

@step('status code will be "{status}"')
def step_impl(context, status):
	assert context.r.status_code==int(status)
	
@step('result will be "{result}"')
def step_impl(context, result):
	context.rjson=context.r.json()
	assert context.rjson['result']==int(result)