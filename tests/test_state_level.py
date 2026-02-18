import os
import requests

BASE = 'https://api.ceda.ashoka.edu.in/v1'
H = {'Authorization': f'Bearer {os.getenv("CEDA_API_KEY", "")}'}

# Try state-level data (no district/market filter)
r = requests.post(BASE+'/agmarknet/prices', headers=H, json={
    'commodity_id': 23,  # Onion
    'state_id': 27,  # Maharashtra
    'from_date': '2024-06-01',
    'to_date': '2025-11-09'
})

d = r.json()['output']['data']
print(f'✅ Found {len(d)} records at state level!')

if d:
    print('\n📊 Sample records:')
    for rec in d[:10]:
        print(f"  {rec['date']}: ₹{rec['modal_price']}/qtl (₹{rec['modal_price']/100:.2f}/kg)")
    
    print(f'\n💰 Average modal price: ₹{sum(r["modal_price"] for r in d)/len(d):.2f}/qtl')
    print('🎉 CEDA API IS WORKING!')
else:
    print('❌ No data for this combination')


