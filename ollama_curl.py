import json
import requests


def get_ollama_response(input_promt, model):
    print("ollama_curl engaged")
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{"model": "'+model+'", "prompt": "'+input_promt.replace("\n"," ").replace('"',"'")+'", "stream": false}'

    print("awaiting ollama response")
    response = requests.post('http://localhost:11434/api/generate', headers=headers, data=data)
    print("ollama response recived")
    print("this is ollama response: ", response.content)

    content = response.content

    str = content.decode("utf-8")
    my_json = json.loads(str)
    return my_json

