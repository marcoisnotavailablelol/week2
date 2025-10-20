import requests, sys

if len(sys.argv) > 1:
    name = sys.argv[1].strip()
else:
    name = input("Please input a name: ").strip()
if not name:
    raise SystemExit("No name provided")

try:
    request_age = requests.get("https://api.agify.io", params={"name": name}, timeout=8)
    request_age.raise_for_status()
    agify_data = request_age.json()
    
    request_gender = requests.get("https://api.genderize.io", params={"name": name}, timeout=8)
    request_age.raise_for_status()
    genderize_data = request_gender.json()

    print(f"Your predicted age is {agify_data.get('age')}, and you have a {genderize_data.get('probability') * 100}% of being {genderize_data.get('gender')}.")
except requests.RequestException as e:
    print("Network Error: ", e)
except ValueError:
    print("stupid fucking dev")

