#!/usr/bin/env python
"""
Simple API test
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

# Step 1: Login
print("1. Logging in...")
response = requests.post(f"{BASE_URL}/auth/login/", json={
    "email": "admin@school.com",
    "password": "admin123"
})

print(f"Status: {response.status_code}")
data = response.json()
print(f"Success: {data.get('success')}")

if response.status_code == 200:
    access_token = data['data']['tokens']['access']
    print(f"✅ Login successful!")
    print(f"Token (first 50 chars): {access_token[:50]}...")
    
    # Step 2: Get profile
    print("\n2. Getting profile...")
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(f"✅ Profile retrieved!")
        print(f"User: {response.json()['data']['email']}")
    else:
        print(f"❌ Failed: {response.json()}")
    
    # Step 3: List students
    print("\n3. Listing students...")
    response = requests.get(f"{BASE_URL}/students/students/", headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        count = response.json().get('count', 0)
        print(f"✅ Found {count} students")
    else:
        print(f"❌ Failed: {response.text[:200]}")
else:
    print("❌ Login failed")
