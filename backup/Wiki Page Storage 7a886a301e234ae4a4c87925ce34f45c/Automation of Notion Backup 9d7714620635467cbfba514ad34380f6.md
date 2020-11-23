# Automation of Notion Backup

Column: Nov 14, 2020 7:44 AM
Last edited by: Soutrik das

This is the script that does all of the job 

```python
image: python:3.8

backup:
  only:
    - schedules
  script:
    - git remote set-url origin https://${GITLAB_USER_ID}:${CI_PUSH_TOKEN}@gitlab.com/${CI_PROJECT_PATH}.git
    - git config --global user.email ${GITLAB_USER_EMAIL}
    - git config --global user.name ${GITLAB_USER_ID}
    - ./notion_export_gen.py && ./merge_gen.sh

.before_script_template: &before_script_template |
  cat >notion_export_gen.py <<EOL
  #!/usr/bin/env python
  import os
  import json
  import time
  import urllib
  import urllib.request

  TZ = os.getenv("TZ", "Europe/Amsterdam")
  NOTION_API = os.getenv('NOTION_API', 'https://www.notion.so/api/v3')
  EXPORT_FILENAME = os.getenv('EXPORT_FILENAME', 'export.zip')
  NOTION_TOKEN_V2 = os.environ['NOTION_TOKEN_V2']
  NOTION_SPACE_ID = os.environ['NOTION_SPACE_ID']

  ENQUEUE_TASK_PARAM = {
      "task": {
          "eventName": "exportSpace", "request": {
              "spaceId": NOTION_SPACE_ID,
              "exportOptions": {"exportType": "markdown", "timeZone": TZ, "locale": "en"}
          }
      }
  }

  def request(endpoint: str, params: object):
      req = urllib.request.Request(
          f'{NOTION_API}/{endpoint}',
          data=json.dumps(params).encode('utf8'),
          headers={
              'content-type': 'application/json',
              'cookie': f'token_v2={NOTION_TOKEN_V2}; '
          },
      )
      response = urllib.request.urlopen(req)
      return json.loads(response.read().decode('utf8'))

  def export():
      task_id = request('enqueueTask', ENQUEUE_TASK_PARAM).get('taskId')
      print(f'Enqueued task {task_id}')

      while True:
          time.sleep(2)
          tasks = request("getTasks", {"taskIds": [task_id]}).get('results')
          task = next(t for t in tasks if t.get('id') == task_id)
          print(f'\rPages exported: {task.get("status").get("pagesExported")}', end="")

          if task.get('state') == 'success':
              break

      export_url = task.get('status').get('exportURL')
      print(f'\nExport created, downloading: {export_url}')

      urllib.request.urlretrieve(
          export_url, EXPORT_FILENAME,
          reporthook=lambda c, bs, ts: print(f"\r{int(c * bs * 100 / ts)}%", end="")
      )
      print(f'\nDownload complete: {EXPORT_FILENAME}')

  if __name__ == "__main__":
      export()
  EOL

  cat > merge_gen.sh <<EOL
  #!/bin/bash
  set -e

  mkdir -p backup
  rm -rf backup/* && unzip -q "$EXPORT_FILENAME" -d backup/

  stats="\$(git diff --shortstat | xargs)"
  if [ -z "\${stats}" ]; then stats=none; fi

  printf "Updated: %s\n\nUpdates: %s" "\$(date)" "\$stats" > README.md

  git add backup README.md && git commit -m "Updates: \$stats"
  git push origin HEAD:master
  EOL

  chmod +x notion_export_gen.py
  chmod +x merge_gen.sh

before_script:
  - *before_script_template
```

This is just the python part 

```python
import os
  import json
  import time
  import urllib
  import urllib.request

  TZ = os.getenv("TZ", "Europe/Amsterdam")
  NOTION_API = os.getenv('NOTION_API', 'https://www.notion.so/api/v3')
  EXPORT_FILENAME = os.getenv('EXPORT_FILENAME', 'export.zip')
  NOTION_TOKEN_V2 = os.environ['NOTION_TOKEN_V2']
  NOTION_SPACE_ID = os.environ['NOTION_SPACE_ID']

  ENQUEUE_TASK_PARAM = {
      "task": {
          "eventName": "exportSpace", "request": {
              "spaceId": NOTION_SPACE_ID,
              "exportOptions": {"exportType": "markdown", "timeZone": TZ, "locale": "en"}
          }
      }
  }

  def request(endpoint: str, params: object):
      req = urllib.request.Request(
          f'{NOTION_API}/{endpoint}',
          data=json.dumps(params).encode('utf8'),
          headers={
              'content-type': 'application/json',
              'cookie': f'token_v2={NOTION_TOKEN_V2}; '
          },
      )
      response = urllib.request.urlopen(req)
      return json.loads(response.read().decode('utf8'))

  def export():
      task_id = request('enqueueTask', ENQUEUE_TASK_PARAM).get('taskId')
      print(f'Enqueued task {task_id}')

      while True:
          time.sleep(2)
          tasks = request("getTasks", {"taskIds": [task_id]}).get('results')
          task = next(t for t in tasks if t.get('id') == task_id)
          print(f'\rPages exported: {task.get("status").get("pagesExported")}', end="")

          if task.get('state') == 'success':
              break

      export_url = task.get('status').get('exportURL')
      print(f'\nExport created, downloading: {export_url}')

      urllib.request.urlretrieve(
          export_url, EXPORT_FILENAME,
          reporthook=lambda c, bs, ts: print(f"\r{int(c * bs * 100 / ts)}%", end="")
      )
      print(f'\nDownload complete: {EXPORT_FILENAME}')

  if __name__ == "__main__":
      export()
```

But I need to understand and then implement what he is doing outside of python to actually make it work in github 

In the end this is the code for github `main.yml`

[Locked page for previous code ](Automation%20of%20Notion%20Backup%209d7714620635467cbfba514ad34380f6/Locked%20page%20for%20previous%20code%20e7028b240ee940e19a4f42ae71cc0f71.md)

```yaml
name: A workflow for my Hello World file
on: 
  schedule:
    - cron: 0 */1 * * *
jobs:
  build:
    name: Hello world action
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
      # - uses: ./action-a
      #   with:
      #     MY_NAME: "Soutrik"
      # - run: pip install numpy
#       - run: pip install os
      - run: |
          git config --global user.name ${{ secrets.CI_GITHUB_USERNAME }}
          git config --global user.email ${{ secrets.CI_GITHUB_EMAIL }}
          git remote set-url origin https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/$GITHUB_REPOSITORY
          git checkout master
          ls -la
      - run: python3 ./helloworld.py
        env:
          TZ: ${{secrets.TZ}}
          NOTION_TOKEN_V2: ${{secrets.NOTION_TOKEN_V2}}
          NOTION_SPACE_ID : ${{secrets.NOTION_SPACE_ID}}
          EXPORT_FILENAME : ${{secrets.EXPORT_FILENAME}}
          # PYTHONUNBUFFERED : ${{secrets.PYTHONUNBUFFERED}}
      - run: |
          ls -la
          set -e
          mkdir -p backup
          rm -rf backup/* && unzip -q "${{secrets.EXPORT_FILENAME}}" -d backup/
          stats="\$(git diff --shortstat | xargs)"
          if [ -z "\${stats}" ]; then stats=none; fi
          printf "Updated: %s\n\nUpdates: %s" "\$(date)" "\$stats" > README.md
          git add backup README.md && git commit -m "Updates: \$stats"
          git push origin master
#         git push origin HEAD:master
#         git add .
#         git commit -m "Github actions ran"
```

And thissi for python

But one problem is , you cannot delete files that easily , yes if you think you can `git clone ...` and then delete the things you want to and then commit , you maybe theoretically right , but today I got got this error , some files were lost trying to git clone , maybe this is a one time error , but I will keep an eye out . 

Thing is  , the current script takes backup of everything ( even the private non shared ones ) which I dont want to be in a public repository , so for that I want to try to export a page with its subpages 

This is the `enque task` for exporting a page ( or `block` as they call it ) 

```json
{task: {eventName: "exportBlock",…}}
task: {eventName: "exportBlock",…}
eventName: "exportBlock"
request: {blockId: "7a886a30-1e23-4ae4-a4c8-7925ce34f45c", recursive: true,…}
blockId: "7a886a30-1e23-4ae4-a4c8-7925ce34f45c"
exportOptions: {exportType: "markdown", timeZone: "Asia/Calcutta", locale: "en"}
exportType: "markdown"
locale: "en"
timeZone: "Asia/Calcutta"
recursive: true
```

```json
{
  "task": {
    "eventName": "exportBlock",
    "request": {
      "blockId": "7a886a30-1e23-4ae4-a4c8-7925ce34f45c",
      "recursive": true,
      "exportOptions": {
        "exportType": "markdown",
        "timeZone": "Asia/Calcutta",
        "locale": "en"
      }
    }
  }
}
```

![Automation%20of%20Notion%20Backup%209d7714620635467cbfba514ad34380f6/Untitled.png](Automation%20of%20Notion%20Backup%209d7714620635467cbfba514ad34380f6/Untitled.png)

And the following is for exporting the whole workspace 

```json
{
  "task": {
    "eventName": "exportSpace",
    "request": {
      "spaceId": "cf02cf21-d490-4d64-bd24-131afb6dcf3b",
      "exportOptions": {
        "exportType": "markdown",
        "timeZone": "Asia/Calcutta",
        "locale": "en"
      }
    }
  }
}
```

Observing them side by side gives us a few differences 

```json
{
  "task": {
    "eventName": "exportSpace",
    "request": {
      "spaceId": "cf02cf21-d490-4d64-bd24-131afb6dcf3b",
      "exportOptions": {
        "exportType": "markdown",
        "timeZone": "Asia/Calcutta",
        "locale": "en"
      }
    }
  }
}
```

```json
{
  "task": {
    "eventName": "exportBlock",
    "request": {
      "blockId": "7a886a30-1e23-4ae4-a4c8-7925ce34f45c",
      "recursive": true,
      "exportOptions": {
        "exportType": "markdown",
        "timeZone": "Asia/Calcutta",
        "locale": "en"
      }
    }
  }
}
```

Notice how theres an extra field named as `recursive:` which wasnt in the export spac