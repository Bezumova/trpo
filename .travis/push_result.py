from git

script:
- ./.travis/$JOB.sh 2>&1 | tee /tmp/$JOB.log
- echo "$(PIPESTATUS[0])" > /tmp/$JOB.res

deplay:
- provider: script
script: python .travis/push_result.py
skip_cleanup: true
