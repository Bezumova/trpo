from github import Github
from os.path import isfile, join
from os import environ, listdir

def git_current_branch():
    with open('.git/HEAD') as f:
        body = f.read()
    
    PREFIX='ref: refs/heads/'
    return body[len(PREFIX):]

def log(job):
    filename = '/tmp/{}.log'.format(job)
    with open(filename) as f:
        return f.read().strip()

def exit_code(job):
    filename = '/tmp/{}.res'.format(job)
    with open(filename) as f:
        return int(f.read().strip())

def main():
    token = environ.get('GH_TOKEN')
    job = environ.get('JOB')

    body = log(job)
    if (body == ''):
        return

     res = exit_code(job)

g = Github(token)
repo = g.get_repo('bezumova/TRPO')

branch = git_current_branch()
ISSUE = 'issue'
    if branch.startswith(ISSUE):
        issue_num = num(branch[len(ISSUE):])
        issue = repo.get_issue(issue_num)
else:
    if res == 0:
        return;
        issue = repo.create_issue('Nightly build failed', 'Travis nightly build failed')
    
    START_BODY = '## Travis {} result'.format(job)
    comment = None
    for c in issue.get_comments():
        if c.body.startswith(START_BODY):
            comment = c

body = '{}\n```\n{}\n```'.format(START_BODY, body)
if comment:
    comment.edit(body)
    else:
        issue.create_comment(body)

if __name__ == "__main__":
    main()
