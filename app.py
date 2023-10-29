
from flask import Flask, render_template, request, session, redirect
import requests, json

# Data Access Objects
import dao.ProdMangerDao as ProdMangerDao, dao.UserMangerDao as UserMangerDao
# modules
import module.auth as auth, module.randompick as randompick

# config
app = Flask(__name__)
app.secret_key = randompick.pick(30)

with open('config/config.json', 'r') as f: 
    config = json.load(f)

def CurrentIP():
    return request.headers.get("CF-Connecting-IP", request.remote_addr)

@app.route('/', methods=['GET'])
def index():
    if 'user_name' in session:
        return render_template('index.html', prod_list=ProdMangerDao.get_allprod(), user_name = session["user_name"])
    else:
        return render_template('index.html', prod_list=ProdMangerDao.get_allprod(), user_name = "비회원")


@app.route('/prod/<prod_id>', methods=['GET'])
def info(prod_id):
    return render_template('prod_page.html', prod_list=ProdMangerDao.get_prod(prod_id))
    
@app.route('/register/', methods=['GET'])
def registers():
    if (session): 
        return redirect(f'http://{config["production"]["domain"]}/')
    else:
        return render_template('register.html')

@app.route('/login/', methods=['GET'])
def logins():
    if (session): 
        return redirect(f'http://{config["production"]["domain"]}/')
    else:
        return render_template('login.html')


@app.route('/api/register', methods=['POST'])
def register():
    if (session):
        return redirect(f'http://{config["production"]["domain"]}/')
    else:
        if ("g-recaptcha-response" in request.form):
            if ("userid" in request.form and "phone" in request.form and "password" in request.form):
                captcha_secret = ""
                captcha_result = requests.get("https://www.google.com/recaptcha/api/siteverify?secret=" + captcha_secret + "&response=" + request.form["g-recaptcha-response"] + "&remoteip=" + CurrentIP()).json()
                if (captcha_result["success"] == True):
                    authcode = randompick.pick(6)
                    UserMangerDao.register(request.form["userid"], request.form["password"], request.form["phone"], authcode, str(0))
                    auth.phone(str(request.form["phone"]), authcode)
                    return "ok"
                else:
                    return "reCAPTCHA 오류가 발생했습니다. 새로고침 후 재시도해주세요."
            else:
                return "목록이 비어있습니다."
        else: 
            return "오류가 발생했습니다."

@app.route('/upload/', methods=['GET'])
def uploadsite():
        return render_template('upload.html')


@app.route('/api/setuserid/<setuserid>/', methods=['GET'])
def test(setuserid):
        session["user_name"] = setuserid
        return redirect(f'http://{config["production"]["domain"]}/') 

@app.route('/api/login', methods=['POST'])
def login():
    if ("user_id" in request.form and "user_password" in request.form):
        login = UserMangerDao.login(request.form["user_id"], request.form["user_password"])
        if login == False:
            return "아이디 또는 비밀번호가 틀립니다."
        else:
            if login == True:
                return redirect(f'http://{config["production"]["domain"]}/api/setuserid/{request.form["user_id"]}/') 
    else:
        return "목록이 비어있습니다."


@app.route('/api/upload', methods=['POST'])
def upload():
    if ("prod_name" in request.form and "prod_image" in request.form and "prod_price" in request.form and "prod_tag" in request.form):
        ProdMangerDao.upload(request.form["prod_name"],request.form["prod_image"],request.form["prod_price"],randompick.pick(18),request.form["prod_tag"])
        return redirect(f'http://{config["production"]["domain"]}/') 
    else:
        return "목록이 비어있습니다."

app.run(host=config["host"]["ip"],port=config["host"]["port"],debug=config["production"]["debug"])