from flask import Flask, send_file
from plot import samples_per_class, affiliate_channel_percentage, provider, signup_app_per_age
app = Flask(__name__)

@app.route('/api/samples_per_class', methods=['GET'])
def func():
    bytes_obj = samples_per_class()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route('/api/affiliate_channel_percentage', methods=['GET'])
def func2():
    bytes_obj = affiliate_channel_percentage()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route('/api/provider', methods=['GET'])
def func3():
    bytes_obj = provider()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route('/api/signup_app_per_age', methods=['GET'])
def func4():
    bytes_obj = signup_app_per_age()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=False)