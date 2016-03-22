from github3 import login
gh = login('uaweb', password='uaweb2016')
print(gh.user('yglukhov').name)
x=gh.user('yglukhov')
print(x.followers)


