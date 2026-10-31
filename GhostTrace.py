'''____________________________________
   https://github.com/G4OSTs/GhostTrace
   */'''

import requests
import os
import json
import ipaddress
from flask import Flask, request, render_template_string
from datetime import datetime


mlogo = '''
\033[38;2;0;128;255m
  [0;37m                  [0;94m▄▄[0;37m                                                          [0m
[0;94;44m▒▓[0;94m▀▀▀▀[0;37m [0;94m██[0;37m  [0;94m██[0;37m [0;94m█[0;94;44m▓[0;94m▀▀██[0;37m [0;94;44m▒▓[0;94m▀▀██[0;37m [0;94;44m▓[0;94m█▀██▀[0;94;44m▓▒[0;37m      [0;94;44m▓[0;94m█▀██▀[0;94;44m▓▒[0;37m [0;94m██▀▀██[0;37m [0;94;44m░▒[0;94m▀▀██[0;37m [0;94;44m░▒[0;94m▀▀██[0;37m [0;94m██▀▀[0;94;44m▒░[0m
[0;94;44m▓[0;94m█[0;37m [0;94m▀██[0;37m [0;94m██▀▀██[0;37m [0;94;44m▓▒[0;37m  [0;94m██[0;37m [0;94;44m▓[0;94m█▄▄▄▄[0;37m    [0;94m██[0;37m            [0;94m██[0;37m    [0;94m██[0;37m     [0;94;44m▒▓[0;37m  [0;94m██[0;37m [0;94;44m▒▓[0;37m  [0;94m▀▀[0;37m [0;94m██▄▄[0;94;44m▓▒[0m
[0;94m██▄▄█[0;94;44m▓[0;37m [0;94m██[0;37m  [0;94m██[0;37m [0;94m█[0;94;44m▓[0;94m▄▄██[0;37m [0;34m▄▄[0;37m  [0;94;44m▒▒[0;37m    [0;94m██[0;37m            [0;94m██[0;37m    [0;94m██[0;37m     [0;94;44m▓[0;94m█▀▀██[0;37m [0;94;44m▓[0;94m█▄▄█[0;94;44m▓[0;37m [0;94m██▄▄▄▄[0m
[0;37m    [0;94m▀▀[0;37m        [0;94m▀▀[0;37m     [0;34m▀▀▀▀▀▀[0;37m                               [0;94m▀▀[0;37m         [0;94m▀▀[0;37m       [0m 
           \033[38;2;255;255;255m                       by G40ST
'''
print(mlogo)
print("\033[38;2;128;255;0m=\033[38;2;255;255;255m"*79,'\n')


#ip lookup
def iplookup():
    os.system("clear")

    logo1 = '''
    \033[38;2;128;255;0m

            _,--',   _._.--._____
    .--.--';_'-.', ";_      _.,-'
    .'--'.  _.'    {`'-;_ .-.>.'
        '-:_      )  / `' '=.
            ) >     {_/,     /~)
            |/               `^ .'
    \033[38;2;255;255;255m
                IP LOOKUP
    '''
    print(logo1)

    print("\033[38;2;128;255;0m=\033[38;2;255;255;255m"*48,'\n')
     
    ip = input("Enter IP \033[38;2;255;26;26m==>\033[38;2;255;255;255m ").strip()
    print("\n")
    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=10
        )
        r.raise_for_status()
        data = r.json()

        if data.get("status") == "success":
            print("\033[38;2;0;64;255m____________________RESULTS____________________\n")
            print(f"\033[38;2;255;26;26mIP Address   \033[38;2;255;255;255m: {data['query']}")
            print(f"\033[38;2;255;26;26mCountry      \033[38;2;255;255;255m: {data['country']}")
            print(f"\033[38;2;255;26;26mCountry Code \033[38;2;255;255;255m: {data['countryCode']}")
            print(f"\033[38;2;255;26;26mRegion       \033[38;2;255;255;255m: {data['regionName']}")
            print(f"\033[38;2;255;26;26mCity         \033[38;2;255;255;255m: {data['city']}")
            print(f"\033[38;2;255;26;26mZIP          \033[38;2;255;255;255m: {data['zip']}")
            print("\033[38;2;128;255;0m===============================================\n")
            print(f"\033[38;2;255;26;26mLatitude     \033[38;2;255;255;255m: {data['lat']}")
            print(f"\033[38;2;255;26;26mLongitude    \033[38;2;255;255;255m: {data['lon']}")
            lat = data['lat']
            lon = data['lon']
            print(f"\033[38;2;255;26;26mTime Zone    \033[38;2;255;255;255m: {data['timezone']}")
            print("\033[38;2;128;255;0m===============================================\n")
            print(f"\033[38;2;255;26;26m______Google map url open it from browser______\n")
            url_l=f"https://www.google.com/maps/place/{lat},{lon}"
            print(f"\033[38;2;51;204;255mGoogle MAP Url \033[38;2;255;26;26m ==>\033[38;2;51;153;255m",url_l)
            print("\033[38;2;128;255;0m===============================================\n")
            print(f"\033[38;2;255;26;26mISP          \033[38;2;255;255;255m: {data['isp']}")
            print(f"\033[38;2;255;26;26mORG          \033[38;2;255;255;255m: {data['org']}")
            print(f"\033[38;2;255;26;26mAS           \033[38;2;255;255;255m: {data['as']}")
            print("\033[38;2;128;255;0m===============================================\n")

        else:
            print("\033[38;2;255;26;26m\nIP lookup failed:", data.get("message", "Invalid IP\033[38;2;255;255;255m"))

    except requests.RequestException as error:
        print(f"\nNetwork error: {error}")
    except ValueError:
        print("\033[38;2;255;26;26m\nCould not read the API response.")

    rm = input("\033[38;2;255;255;255m\nBACK TO MAIN MENU [y/n] \033[38;2;255;26;26m==>\033[38;2;255;255;255m ").lower().strip()

    if rm == "y":
        return 
    elif rm == "n":
        print("\033[38;2;0;128;255m.........Bye....! From G40ST......!\033[38;2;255;255;255m")
        raise SystemExit
    else:
        print("\033[38;2;255;26;26mInvalid choice. Returning to menu....!")
        return


#ip pishing
def ipfish():
    os.system("clear")
    logo2='''
        \033[38;2;255;26;26m
        ⢰⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠈⢧⠨⠢⡀⠀⠀⠀⠀⠀⠀⠲⢒⠒⠦⠤⣀⡀⠀⠀⠀⠀⢀⣠⣤⠴⠒⠋⠙⡄
        ⠀⠸⠀⠐⢱⠀⠀⠀⠀⠀⠀⢀⣈⠦⠤⠀⠒⠊⠉⠉⠀⠈⠁⣀⠭⠀⢁⣀⣀⣹
        ⠀⠀⠖⠀⠃⠓⢤⠖⠒⠚⠉⠀⠀⡀⠀⠀⠀⢀⣰⢴⠶⠐⢈⣴⣿⠟⠿⢻⣿⡞
        ⠀⢰⠀⠀⠀⡤⢤⣄⠀⠀⠤⠤⠀⠀⣐⠄⠀⠼⡏⡧⠄⢢⡾⠋⠀⠀⢠⣎⡟⠀
        ⢠⠃⣀⠴⠋⠀⠀⠈⠑⠢⢄⣀⣠⠊⠀⢀⠎⠀⠡⠅⠀⠻⢿⣤⣤⡴⣾⣴⣿⠀
        ⡬⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⣠⠶⣇⣀⣀⠀⠀⠀⠀⠀⣀⣌⡠⠤⠘⠋⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣔⡡⠚⠁⠀⠀⠀⠈⠉⠉⠉⠻⡍⠙⡄⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠃⠀⠀⠀⠀⠀
        \033[38;2;255;255;255m
                 IP PISHING     
        '''
    print(logo2)
    
    print("\033[38;2;128;255;0m=\033[38;2;255;255;255m"*90,'\n')

    app = Flask(__name__)

    #web page
    HTML_PAGE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Cyber Earth</title>
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                background: #03080d;
                color: #00ff9c;
                font-family: Consolas, monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 20px;
            }

            .panel {
                max-width: 600px;
                width: 100%;
                padding: 30px 20px;
                border: 1px solid #00ff9c;
                border-radius: 14px;
                background: #07131b;
                box-shadow: 0 0 25px #00ff9c33;
            }

            h1 { text-shadow: 0 0 15px #00ff9c; }
            .earth { font-size: 85px; margin: 25px 0; }
            .status { border: 1px solid #164c3a; padding: 12px; }
            .note { color: #9bb8b0; font-size: 13px; line-height: 1.7; }
        </style>
    </head>
    <body>
        <main class="panel">
            <h1>CYBER EARTH</h1>
            <div class="earth">🌍</div>
            <p class="status">● SYSTEM ONLINE</p>
            <p>Visitor connection logging is enabled.</p>
            <p id="ip">Checking your public IP...</p>
            <p class="note">
                by G40ST...!
            </p>
        </main>

        <script>
            async function loadIP() {
                const output = document.getElementById("ip");

                try {
                    const response = await fetch(
                        "https://api.ipify.org?format=json"
                    );

                    if (!response.ok) throw new Error("Lookup failed");

                    const data = await response.json();
                    output.textContent = "Public IP: " + data.ip;

                    const result = await fetch("/record-ip", {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({public_ip: data.ip})
                    });

                    if (!result.ok) {
                        output.textContent =
                            "IP checked; server could not record the result.";
                    }
                } catch (error) {
                    output.textContent = "Public IP lookup unavailable.";
                }
            }

            loadIP();
        </script>
    </body>
    </html>
    """

    #flask app route
    @app.route("/")
    def home():
        timestamp = datetime.now().astimezone().isoformat(
            timespec="seconds"
        )
        print(f"\033[38;2;255;26;26m[{timestamp}] Page visit; connection IP: {request.remote_addr}\033[38;2;255;255;255m")
        return render_template_string(HTML_PAGE)

   
    @app.route("/record-ip", methods=["POST"])
    def record_ip():
        data = request.get_json(silent=True) or {}
        public_ip = data.get("public_ip", "")

        try:
            parsed_ip = ipaddress.ip_address(public_ip)
        except ValueError:
            return {"error": "Invalid IP"}, 400

        timestamp = datetime.now().astimezone().isoformat(
            timespec="seconds"
        )
        print(f"\033[38;2;128;255;0m[{timestamp}] Public IP reported by browser: {parsed_ip}\033[38;2;255;255;255m")

        return {"status": "ok"}, 200
    
    #flask output
    if __name__ == "__main__":
        print("\033[38;2;255;26;26mDo not close terminal ...! send link to the target...! Eg:- http://192.168.10.101:5000\033[38;2;255;255;255m")
        print("\033[38;2;255;26;26mTo Exit tool and sever Press (Ctrl + C)\033[38;2;255;255;255m")
        print("="*90)
        print("SERVER STARTED....!")
        print("Local page: http://127.0.0.1:5000")

        app.run(host="0.0.0.0", port=5000, debug=False)


#Main menu
def menu():
    while True:
        
        print("\033[38;2;0;255;255m[\033[38;2;255;255;255m1\033[38;2;0;255;255m] IP Look Up")
        print("\033[38;2;0;255;255m[\033[38;2;255;255;255m2\033[38;2;0;255;255m] IP Pishing")
        print("\033[38;2;0;255;255m[\033[38;2;255;255;255m0\033[38;2;0;255;255m] Exit")

        try:
            cel = int(input(
                "\033[38;2;255;26;26m===> "
                "\033[38;2;255;255;255m"
            ))
        except ValueError:
            print("Please enter a valid number.")
            input("Press Enter to continue...")
            continue

        if cel == 1:
            iplookup()

        elif cel == 2:
            ipfish()

        elif cel == 0:
            print("Exiting program...")
            print("\033[38;2;0;128;255m.........Bye....! From G40ST......!\033[38;2;255;255;255m")
            os._exit(0)
            break

        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    menu()


rv=menu()

if rv==1:
    hf=iplookup()
elif rv==2:
    hf=ipfish()



