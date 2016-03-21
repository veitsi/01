from github3 import login
gh = login('veitsi', password='<somepass>')
print(gh.user('xtfkpi'))
x=gh.user('xtfkpi')
print(x.followers)


