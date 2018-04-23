import behave
import requests

@step('I set base URL to "{base_url}"')
def set_base_url(context, base_url):
	context.base_url = base_url
	print(context.base_url)
	
@step('I add path "{path}" to base URL')
def add_path_to_url(context, path):
	context.base_url += "/" + path
	print(context.base_url)
	
@step ('make GET request')
def step_impl(context):
	context.r=requests.get(context.base_url, params=context.payload)
	assert context.r

