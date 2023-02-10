from flask import Flask, render_template, request
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s')

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    logging.info("New request for / from %s", request.remote_addr)
    return render_template('home.html')

@app.route('/compiler', methods=["POST"])
def compiler():
    logging.info("compile request from IP %s", request.remote_addr)

    compflags = request.form.get("compflags")
    if compflags.find("-DDEATH") != -1:
        death = True
    else:
        death = False


    delay = "2000"
    destination = "'/alive'"
    if death:
        destination = "'/dead'"
        delay = "6000"
        if request.form.get("compiler") == "clang15":
            if (request.form.get("opts") == "more" or request.form.get("opts") == "moremore"):
                destination = "'/solved?flag=ctf{optimized_undefined_behavior}'"
                delay = "2000"

    doc = '''
        <!DOCTYPE html>
        <html>
          <head><title>Compiling and testing</title></head>
          <body>
            <h1>Compiling and testing</h1>'''

    if death:
        doc += '<img src="static/death.jpg" alt="So you have chosen death" height="580">'

    doc += '''<script>
            setTimeout(function(){
            window.location.href='''

    doc += destination + ";}," + delay +''');
            </script>
          </body>
        </html>'''
    return doc


@app.route('/alive')
def alive():
    return '''
        <!DOCTYPE html>
        <html>
          <head><title>You survived!</title></head>
          <body>
            <h1>You survived!</h1>
            <p>Your program executed normally and gave the following output:</p>
            <code>You chose to live! But alas, you didn't get the flag.</code>
            
            <p>May I recommend the awesome
            <a href="https://godbolt.org/z/czMjr9aG3" target="_blank">Compiler Explorer</a>
            to try out some options?</p>
            
            <h3><a href="/">Start over</a></h3>
             
          </body>
        </html>'''


@app.route('/dead')
def dead():
    return '''
        <!DOCTYPE html>
        <html>
          <head><title>You died!</title></head>
          <body>
            <h1>You died!</h1>
            <p>We had to kill your program.</p>
            <code>Killed - processing time exceeded</code><br>
            <p>May I recommend the awesome
            <a href="https://godbolt.org/z/czMjr9aG3" target="_blank">Compiler Explorer</a>
            to try out some options?</p>

            <h3><a href="/">Start over</a></h3>

          </body>
        </html>'''


@app.route('/solved')
def solved():
    flag = request.args.get('flag')
    if flag == None:
        return "<h1>Cheaters never win.</H1>"

    return '''
        <!DOCTYPE html>
        <html>
          <head><title>You did it!</title></head>
          <body>
            <h1>You reached the unreachable code!</h1>
            
            <p>Program output:</p>
            <code>You've reached the unreachable code<br>
            The flag is ''' + flag + '''</code><br>

            <h3><a href="/">Start over</a></h3>

          </body>
        </html>'''

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)

