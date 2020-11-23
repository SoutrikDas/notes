# Locked page for previous code

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
  print("DONE")
```