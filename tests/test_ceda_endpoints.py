import os
import requests

API_KEY = os.getenv("CEDA_API_KEY", "")

print("🔍 Testing CEDA API Endpoints...")
print("=" * 70)

# Try different endpoint variations
endpoints = [
    "https://api.ceda.ashoka.edu.in/agmarknet/v1/data",
    "https://api.ceda.ashoka.edu.in/agmarknet/data",
    "https://api.ceda.ashoka.edu.in/v1/agmarknet/data",
    "https://api.ceda.ashoka.edu.in/data",
    "https://ceda.ashoka.edu.in/api/agmarknet/v1/data",
]

params = {"state": "Maharashtra", "commodity": "Onion", "limit": 5}
headers = {"Authorization": f"Bearer {API_KEY}"}

for endpoint in endpoints:
    print(f"\n📡 Trying: {endpoint}")
    
    # Try without headers
    try:
        response = requests.get(endpoint, params=params, timeout=10)
        print(f"   Status (no auth): {response.status_code}")
        if response.status_code != 404:
            print(f"   ✅ Response: {response.text[:150]}")
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
    
    # Try with headers
    try:
        response = requests.get(endpoint, params=params, headers=headers, timeout=10)
        print(f"   Status (with auth): {response.status_code}")
        if response.status_code != 404:
            print(f"   ✅ Response: {response.text[:150]}")
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")

print("\n" + "=" * 70)
print("💡 Try checking CEDA documentation or contact them for correct endpoint")


