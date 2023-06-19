import json
import requests

import quart
import quart_cors
from quart import request

# Note: Setting CORS to allow chat.openapi.com is only required when running a localhost plugin
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
HOST_URL = "https://search.dip.bundestag.de"

@app.get("/members")
async def get_members():
    end_date = request.args.get("end_date")
    res = requests.get(
        f"{HOST_URL}/api/v1/person?f.datum.start={end_date}&f.datum.end={end_date}&format=json&apikey=rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF")
    body = res.json()
    return quart.Response(response=json.dumps(body), status=200)

@app.get("/activities")
async def get_activities():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    res = requests.get(
        f"{HOST_URL}/api/v1/aktivitaet?f.datum.start={start_date}&f.datum.end={end_date}&format=json&apikey=rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF")
    body = res.json()
    #return quart.Response(response=json.dumps(body), status=200)

    # Filter the response
    filtered_response = {}
    for document in body['documents']:
        vorgangsbezug_titel = document['vorgangsbezug'][0]['titel'] if document['vorgangsbezug'] else None
        pdf_url = document['fundstelle']['pdf_url']

        # Check if the combination of vorgangsbezug_titel and pdf_url has been seen before
        if (vorgangsbezug_titel, pdf_url) not in filtered_response:
            filtered_response[(vorgangsbezug_titel, pdf_url)] = [document['titel']]
        else:
            filtered_response[(vorgangsbezug_titel, pdf_url)].append(document['titel'])

    # Convert the dictionary to a list of dictionaries for the response
    response = []
    for (vorgangsbezug_titel, pdf_url), titel in filtered_response.items():
        response.append({
            'vorgangsbezug_titel': vorgangsbezug_titel,
            'pdf_url': pdf_url,
            'titel': titel
        })

    return quart.Response(response=json.dumps(response), status=200)

@app.get("/protocols")
async def get_protocols():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    res = requests.get(
        f"{HOST_URL}/api/v1/plenarprotokoll?f.datum.start={start_date}&f.datum.end={end_date}&f.zuordnung=BT&format=json&apikey=rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF")

    # Filter the response
    if res.status_code == 200:
        data = res.json()
        # Extract only results where entries of "Plenarprotokoll" are listed
        plenarprotokolle = [item for item in data['documents'] if item['dokumentart'] == 'Plenarprotokoll']
        #for protokoll in plenarprotokolle:
        #    print(protokoll)
        return quart.Response(response=json.dumps(plenarprotokolle), status=200)

    else:
        print(f'Error: {res.status_code}')

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        # This is a trick we do to populate the PLUGIN_HOSTNAME constant in the manifest
        text = text.replace("PLUGIN_HOSTNAME", f"http://{host}")
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        # This is a trick we do to populate the PLUGIN_HOSTNAME constant in the OpenAPI spec
        text = text.replace("PLUGIN_HOSTNAME", f"http://{host}")
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5001)

if __name__ == "__main__":
    main()