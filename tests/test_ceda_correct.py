import os
import requests
import pandas as pd

API_KEY = os.getenv("CEDA_API_KEY", "")

print("=" * 70)
print("🧪 Testing CEDA Agmarknet API (Correct Endpoints)")
print("=" * 70)

# Try the subdomain endpoint
endpoints = [
    "https://agmarknet.ceda.ashoka.edu.in/v1/data",
    "https://agmarknet.ceda.ashoka.edu.in/api/v1/data",
    "https://agmarknet.ceda.ashoka.edu.in/data",
]

params = {
    "state": "Maharashtra",
    "commodity": "Onion",
    "limit": 5
}

headers_variants = [
    {},
    {"Authorization": f"Bearer {API_KEY}"},
    {"X-API-Key": API_KEY},
    {"api-key": API_KEY},
]

print("\n🔍 Testing different endpoints and auth methods...")

for endpoint in endpoints:
    print(f"\n📡 Endpoint: {endpoint}")
    
    for idx, headers in enumerate(headers_variants):
        auth_type = "No Auth" if not headers else list(headers.keys())[0]
        
        try:
            response = requests.get(endpoint, params=params, headers=headers, timeout=15)
            print(f"   [{auth_type}] Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ SUCCESS! Found working endpoint!")
                data = response.json()
                print(f"   Response keys: {data.keys()}")
                
                if "data" in data:
                    records = data["data"]
                    print(f"   ✅ Records: {len(records)}")
                    
                    if records:
                        print("\n   📊 Sample Record:")
                        sample = records[0]
                        for key, value in list(sample.items())[:8]:
                            print(f"      {key}: {value}")
                        
                        # Create DataFrame
                        df = pd.DataFrame(records)
                        print(f"\n   ✅ DataFrame: {len(df)} rows x {len(df.columns)} columns")
                        print(f"   Columns: {df.columns.tolist()}")
                        
                        print("\n" + "=" * 70)
                        print("🎉 WORKING CONFIGURATION FOUND!")
                        print("=" * 70)
                        print(f"Endpoint: {endpoint}")
                        print(f"Auth: {headers}")
                        print("=" * 70)
                        break
                        
            elif response.status_code != 404:
                print(f"   Response: {response.text[:100]}")
                
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    else:
        continue
    break

# If no success, try base URLs
print("\n\n🔍 Checking base URLs for documentation...")
base_urls = [
    "https://agmarknet.ceda.ashoka.edu.in/",
    "https://ceda.ashoka.edu.in/",
]

for url in base_urls:
    try:
        print(f"\n📡 {url}")
        response = requests.get(url, timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            # Check for API documentation links
            if "api" in response.text.lower() or "documentation" in response.text.lower():
                print("   ✅ Contains API/documentation references")
    except Exception as e:
        print(f"   ❌ {str(e)}")

print("\n" + "=" * 70)
print("📝 Summary:")
print("   The API endpoint structure needs verification from CEDA docs")
print("   Alternative: Use sample data mode which is working perfectly")
print("=" * 70)


