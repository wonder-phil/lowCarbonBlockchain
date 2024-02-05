from flask import Flask, request
import requests
import os
import json
import time

app = Flask(__name__)

KUBERNETES_API = "https://kubernetes.default.svc.cluster.local:443/api/v1/namespaces/ns2/pods"
with open("/var/run/secrets/kubernetes.io/serviceaccount/token") as f:
    token = f.read()

KUBERNETES_HEADER = {
    "Authorization": "Bearer {}".format(token),
    "Content-Type": "application/json",
}

@app.route("/", methods=["POST"])
def launch_pod():
    # Get the JSON object from the request
    data = request.get_json()
    flips = data.get("heads")

    #Generate the correct ENV varibles.
    env_vars = [
        {
            "name": "heads",
            "value": str(flips)
        }
    ]

    # Define the pod definition that calls coinfipper image with the right varialbe.
    pod_def = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": "backend-coinflip-1",
        },
        "spec": {
            "containers": [
                {
                    "name": "coin-flipper",
                    "image": "gemajlia/coinflipper:latest",
                    "imagePullPolicy": "Always",
                    "env": env_vars,
                    "restartPolicy": "Never"
                }
            ]
        }
    }

    # Create the new POD.
    response = requests.post(KUBERNETES_API, headers=KUBERNETES_HEADER, data=json.dumps(pod_def), verify=False)


    # Get the name of the pod
    app.logger.info(response.json())
    pod_name = response.json()["metadata"]["name"]
    

    # Wait for the pod to complete
    while True:
        pod_status = "null"
        response = requests.get(f"{KUBERNETES_API}/{pod_name}", headers=KUBERNETES_HEADER, verify=False)
        if "lastState" in response.json()["status"]["containerStatuses"][0]:
            if "terminated" in response.json()["status"]["containerStatuses"][0]["lastState"]:
                if "reason" in response.json()["status"]["containerStatuses"][0]["lastState"]["terminated"]:
                    pod_status = response.json()["status"]["containerStatuses"][0]["lastState"]["terminated"]["reason"]
                else:
                    pod_status = "nullReason"
            else:
                pod_status = "nullTerminated"
        else:
            pod_status = "nullContainer"
        
        if pod_status == "Completed":
            break
        time.sleep(1)

    # Get the logs from the pod
    response = requests.get(f"{KUBERNETES_API}/{pod_name}/log", headers=KUBERNETES_HEADER, verify=False)
    logs = response.text

    response = requests.delete(f"{KUBERNETES_API}/{pod_name}", headers=KUBERNETES_HEADER, verify=False)

    #delete 

    return logs

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)












