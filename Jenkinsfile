pipeline {
    agent any

    stages {
        stage('Commit info') {
            steps {
                sh 'git log -1 --pretty="Commit: %h %s (%an, %ar)"'
            }
        }
        stage('Environment') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'python3 -m unittest discover -s tests -t . -v'
            }
        }
    }

    post {
        always {
            withCredentials([
                string(credentialsId: 'webex-bot-token', variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'webex-room-id',  variable: 'WEBEX_ROOM')
            ]) {
                withEnv(["BUILD_STATUS=${currentBuild.currentResult}"]) {
                    sh '''
python3 - <<'PY'
import json, os, subprocess, urllib.request

commit = subprocess.run(["git", "log", "-1", "--pretty=%h %s (%an)"],
                        capture_output=True, text=True).stdout.strip()
status = os.environ.get("BUILD_STATUS", "UNKNOWN")
label = "PASSED" if status == "SUCCESS" else "FAILED"
md = (f"**Jenkins build {label}**\\n\\n"
      f"- Job: {os.environ.get('JOB_NAME', '?')} #{os.environ.get('BUILD_NUMBER', '?')}\\n"
      f"- Status: {status}\\n"
      f"- Commit: `{commit}`\\n"
      f"- Console: {os.environ.get('BUILD_URL', '')}console")

req = urllib.request.Request(
    "https://webexapis.com/v1/messages",
    data=json.dumps({"roomId": os.environ["WEBEX_ROOM"], "markdown": md}).encode(),
    headers={"Authorization": "Bearer " + os.environ["WEBEX_TOKEN"],
             "Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=15) as resp:
    print("Webex notification sent, HTTP", resp.status)
PY
'''
                }
            }
        }
    }
}
