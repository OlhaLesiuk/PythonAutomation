from requests import get, post, put, patch, delete

getresponse = get('https://reqres.in/api/users?page=2')
postresponse = post('https://reqres.in/api/users')
putresponse = put('https://reqres.in/api/users/2')
patchresponse = patch('https://reqres.in/api/users/2')
deleteresponse = delete('https://reqres.in/api/users/2')
print(getresponse.content, postresponse.content, putresponse.content, patchresponse.content, deleteresponse.content)
print(getresponse.text, postresponse.text, putresponse.text, patchresponse.text, deleteresponse.text)
print(getresponse.status_code, postresponse.status_code, putresponse.status_code, patchresponse.status_code,
      deleteresponse.status_code)
