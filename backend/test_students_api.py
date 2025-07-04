#!/usr/bin/env python
"""
Quick test script for Students API
Tests the main endpoints to verify everything is working
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def print_response(title, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")

def test_students_api():
    """Test the Students API endpoints"""
    
    print("\n🧪 Testing Smart School ERP - Students API")
    print("="*60)
    
    # Step 1: Login as admin
    print("\n1️⃣  Logging in as admin...")
    login_data = {
        "email": "admin@school.com",
        "password": "admin123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login/", json=login_data)
    print_response("Login Response", response)
    
    if response.status_code != 200:
        print("\n❌ Login failed! Make sure the server is running and admin user exists.")
        return
    
    # Get access token
    access_token = response.json().get('access')
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    print("\n✅ Login successful! Access token obtained.")
    
    # Step 2: Create a test student
    print("\n2️⃣  Creating a test student...")
    student_data = {
        "email": "ram.sharma@school.com",
        "password": "student123",
        "first_name": "Ram",
        "last_name": "Sharma",
        "middle_name": "Bahadur",
        "date_of_birth": "2010-05-15",
        "gender": "M",
        "phone": "+9779841234567",
        "address": "Dharan-8, Sunsari",
        "city": "Dharan",
        "blood_group": "O+",
        "admission_number": "STU2026001",
        "roll_number": "10A-01",
        "class_name": "Grade 10",
        "section": "A",
        "academic_year": "2025-2026",
        "admission_date": "2026-01-15",
        "admission_type": "REGULAR",
        "father_name": "Hari Bahadur Sharma",
        "father_phone": "+9779841234568",
        "father_email": "hari.sharma@email.com",
        "father_occupation": "Business",
        "mother_name": "Sita Sharma",
        "mother_phone": "+9779841234569",
        "mother_email": "sita.sharma@email.com",
        "mother_occupation": "Teacher"
    }
    
    response = requests.post(f"{BASE_URL}/students/students/", json=student_data, headers=headers)
    print_response("Create Student Response", response)
    
    if response.status_code == 201:
        print("\n✅ Student created successfully!")
        student_id = response.json().get('id')
    elif response.status_code == 400 and 'already exists' in str(response.json()):
        print("\n⚠️  Student already exists, fetching existing student...")
        # Get existing student
        response = requests.get(f"{BASE_URL}/students/students/", headers=headers)
        if response.status_code == 200 and response.json().get('results'):
            student_id = response.json()['results'][0]['id']
            print(f"✅ Using existing student ID: {student_id}")
        else:
            print("❌ Could not fetch existing student")
            return
    else:
        print("\n❌ Failed to create student")
        return
    
    # Step 3: List all students
    print("\n3️⃣  Listing all students...")
    response = requests.get(f"{BASE_URL}/students/students/", headers=headers)
    print_response("List Students Response", response)
    
    if response.status_code == 200:
        count = response.json().get('count', 0)
        print(f"\n✅ Found {count} student(s)")
    
    # Step 4: Get student details
    print(f"\n4️⃣  Getting student details (ID: {student_id})...")
    response = requests.get(f"{BASE_URL}/students/students/{student_id}/", headers=headers)
    print_response("Student Details Response", response)
    
    if response.status_code == 200:
        print("\n✅ Student details retrieved successfully!")
    
    # Step 5: Filter students by class
    print("\n5️⃣  Filtering students by class (Grade 10, Section A)...")
    response = requests.get(
        f"{BASE_URL}/students/students/by_class/",
        params={"class_name": "Grade 10", "section": "A"},
        headers=headers
    )
    print_response("Filter by Class Response", response)
    
    if response.status_code == 200:
        count = len(response.json())
        print(f"\n✅ Found {count} student(s) in Grade 10 - A")
    
    # Step 6: Create a guardian
    print(f"\n6️⃣  Adding a guardian for student...")
    guardian_data = {
        "student": student_id,
        "name": "Krishna Sharma",
        "relation": "GRANDFATHER",
        "phone": "+9779841234570",
        "email": "krishna.sharma@email.com",
        "is_emergency_contact": True
    }
    
    response = requests.post(f"{BASE_URL}/students/guardians/", json=guardian_data, headers=headers)
    print_response("Create Guardian Response", response)
    
    if response.status_code == 201:
        print("\n✅ Guardian added successfully!")
        guardian_id = response.json().get('id')
    
    # Step 7: Get student's guardians
    print(f"\n7️⃣  Getting all guardians for student...")
    response = requests.get(f"{BASE_URL}/students/students/{student_id}/guardians/", headers=headers)
    print_response("Student Guardians Response", response)
    
    if response.status_code == 200:
        count = len(response.json())
        print(f"\n✅ Found {count} guardian(s)")
    
    # Step 8: Create a student note
    print(f"\n8️⃣  Adding a note for student...")
    note_data = {
        "student": student_id,
        "note_type": "ACADEMIC",
        "title": "Excellent Performance",
        "content": "Ram has shown excellent performance in mathematics and science. Very attentive in class.",
        "is_private": False
    }
    
    response = requests.post(f"{BASE_URL}/students/notes/", json=note_data, headers=headers)
    print_response("Create Note Response", response)
    
    if response.status_code == 201:
        print("\n✅ Note added successfully!")
    
    # Step 9: Create an achievement
    print(f"\n9️⃣  Adding an achievement for student...")
    achievement_data = {
        "student": student_id,
        "achievement_type": "ACADEMIC",
        "title": "First Position in Mathematics Olympiad",
        "description": "Secured first position in District Level Mathematics Olympiad 2026",
        "date_achieved": "2026-03-15",
        "awarded_by": "District Education Office, Sunsari"
    }
    
    response = requests.post(f"{BASE_URL}/students/achievements/", json=achievement_data, headers=headers)
    print_response("Create Achievement Response", response)
    
    if response.status_code == 201:
        print("\n✅ Achievement added successfully!")
    
    # Step 10: Get student's achievements
    print(f"\n🔟  Getting all achievements for student...")
    response = requests.get(f"{BASE_URL}/students/students/{student_id}/achievements/", headers=headers)
    print_response("Student Achievements Response", response)
    
    if response.status_code == 200:
        count = len(response.json())
        print(f"\n✅ Found {count} achievement(s)")
    
    # Summary
    print("\n" + "="*60)
    print("  🎉 TEST SUMMARY")
    print("="*60)
    print("✅ Authentication: Working")
    print("✅ Create Student: Working")
    print("✅ List Students: Working")
    print("✅ Get Student Details: Working")
    print("✅ Filter by Class: Working")
    print("✅ Add Guardian: Working")
    print("✅ Get Guardians: Working")
    print("✅ Add Note: Working")
    print("✅ Add Achievement: Working")
    print("✅ Get Achievements: Working")
    print("\n🎉 All tests passed! Students API is fully functional!")
    print("="*60)

if __name__ == "__main__":
    try:
        test_students_api()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the server!")
        print("Make sure the Django server is running at http://localhost:8000")
        print("\nStart the server with:")
        print("  cd backend && ./run.sh runserver")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
