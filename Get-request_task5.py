from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/Get_request_task5", methods=["GET"])

def handle_request():
    if(request.method=="GET"):
        return jsonify([
{
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium",
    "hide": False
  },
  {
    "postId": 1,
    "id": 2,
    "name": "quo vero reiciendis velit similique earum",
    "email": "Jayne_Kuhic@sydney.com",
    "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et",
    "hide": False
  },
  {
    "postId": 1,
    "id": 3,
    "name": "odio adipisci rerum aut animi",
    "email": "Nikita@garfield.biz",
    "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione",
    "hide": False
  },
])
        
@app.route("/Get_request_part2", methods=["GET"])

def Get_request_part2():
    if(request.method=="GET"):
        return jsonify(['Mercedes','BMW', 'Audi'])
    
    
@app.route("/Get_request_part3/<id>", methods=["GET"])

def Get_request_part3(id):
    if(request.method=="GET"):
        index_number = int(id)
        data = ["Karan", "Sam", "Ishant"]
        
        return jsonify(data[index_number])
        
if __name__ == "__main__":
    app.run(debug=True, port=2400)
    
    