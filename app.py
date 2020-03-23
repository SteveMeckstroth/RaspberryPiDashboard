from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return """
<html>
<head>
<script>
setTimeout(function() {
        location.reload();
}, 30000);
</script>
</head>
<body>
<div><h1>Hello</h1></div>
</body>
</html>

"""

if __name__ == "__main__":
        app.run(host='0.0.0.0')
