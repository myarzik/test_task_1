import behave
import requests

@given('empty payload')
def step_impl(context):
    context.payload=('')
    
@when ('make GET request')
def step_impl(context):
    context.r=requests.get(context.base_url)
    assert context.r

@then('the result page will include "200"')
def step_impl(context):
    assert context.r.status_code==200