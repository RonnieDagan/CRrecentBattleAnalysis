from battle_fetch import recBattles
import json
import requests

# Get the public IP address
response = requests.get("https://api.ipify.org?format=json")
ip_data = response.json()

# Extract the IP address
ip_address = ip_data["ip"]

# Print the IP address
print(f"My public IP address is: {ip_address}")

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjZiMDA5NTZmLWM3MzktNDhkMi1iMDU5LTQxNTE1YzU5MmI5MyIsImlhdCI6MTcxNjQwNTA0NCwic3ViIjoiZGV2ZWxvcGVyLzc0NTYzNDA3LWZhMTQtMmQyNS0xYTIzLTMwM2Y5YWI1NTQxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzIuMTgyLjIzMi40MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.kxdV0sMXkyK5M0CWWJXVu3sGvgWvpGw8f22JT4cHHQWj_3wmBcslAJZQALYhH4ZMc6OAVDV3Kh4Leco-soi2Zg'

rb = recBattles(api_key, "J2LJQY0U")
with open("sample.txt", "w") as file:
    file.write(str(json.dumps(rb.recent_battles(), indent=4)))