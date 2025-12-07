from flask import Flask, jsonify, request 

app = Flask(__name__)
networks = [
   {"id": 1, "name": "Net1", "subnets": ["1.1.1.1/8", "192.168.1.0/24"},
   {"id": 2, "name": "Net1", "subnets": ["1.1.1.1/8", "192.168.1.0/24"]},
]

@app.route("/networks", methods=["GET"])
def get_networks():
    return jsonify({"networks": networks})


@app.route("/network/<int:id>", methods=["GET"])
def get_network(id):
    for net in networks:
        if net["id"] == id:
            return jsonify({"network": net})
        return jsonify({"error": "Network ID was not found"}), 404
        
@app.route("/network", methods=["POST"])
def create_network():
    data = request.get_json()
    if not data or not("name" in data and "subnets" in data):
        return jsonify ({"error": "the data is not valid"}), 400
    new_network = {
        "id": len(networks) + 1,
        "name": data["name"],
        "subnets": data["subnets"],
    }
    networks.append(new_network)
    return jsonify({"network": new_network}), 201
                    
@app.route("/network/<int:id>", methods=["put"])
def update_network(id):
    for net in networks:
        if net["id"] == id:
            data = request.get_json()
            if not data or not ("name" in data and "subnets" in data):
                return jsonify({"error": "The data is now valid"}), 400
            net.update(data)
            return jsonify({"Network": net}),201

@app.route("/network/<int:id>", methods=["DELETE"])
def DELETE_network(id):
    for net in networks:
        if net["id"] == id:
            networks.remove(net)
            return jsonify({"info": "network successfully delete"}),200
    return jsonify({"Error": "network was not foun"})

if __name__ == "__main__":
    app.run(host="192.168.68.101", port=5050, debug=True)