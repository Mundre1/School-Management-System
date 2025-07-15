import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import api from '../../services/api';

const StudentProfile = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const [student, setStudent] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStudent();
  }, [id]);

  const fetchStudent = async () => {
    try {
      setLoading(true);
      const response = await api.get(`/students/students/${id}/`);
      setStudent(response.data);
    } catch (error) {
      console.error('Error fetching student:', error);
      alert('Failed to load student details');
      navigate('/students');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
          <p className="mt-4 text-gray-600">Loading student profile...</p>
        </div>
      </div>
    );
  }

  if (!student) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-600 text-lg">Student not found</p>
          <button
            onClick={() => navigate('/students')}
            className="mt-4 bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md"
          >
            Back to Students
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">Student Profile</h1>
              <p className="text-sm text-gray-600">View student details</p>
            </div>
            <div className="flex space-x-3">
              <button
                onClick={() => navigate('/students')}
                className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md text-sm font-medium transition"
              >
                ← Back to Students
              </button>
              <button
                onClick={() => navigate(`/students/edit/${id}`)}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium transition"
              >
                Edit Profile
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Left Column - Profile Card */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow p-6">
              <div className="text-center">
                {student.photo ? (
                  <img
                    src={student.photo}
                    alt={student.first_name}
                    className="w-32 h-32 rounded-full mx-auto object-cover border-4 border-blue-500"
                  />
                ) : (
                  <div className="w-32 h-32 rounded-full mx-auto bg-blue-500 flex items-center justify-center text-white text-4xl font-bold border-4 border-blue-600">
                    {student.first_name?.charAt(0)}{student.last_name?.charAt(0)}
                  </div>
                )}
                <h2 className="mt-4 text-2xl font-bold text-gray-900">
                  {student.first_name} {student.last_name}
                </h2>
                <p className="text-gray-600">Grade {student.grade} - Section {student.section}</p>
                <div className="mt-4">
                  <span className={`px-3 py-1 inline-flex text-sm leading-5 font-semibold rounded-full ${
                    student.status === 'active' 
                      ? 'bg-green-100 text-green-800' 
                      : 'bg-red-100 text-red-800'
                  }`}>
                    {student.status || 'Active'}
                  </span>
                </div>
              </div>

              <div className="mt-6 border-t pt-6">
                <div className="space-y-3">
                  <div className="flex items-center">
                    <span className="text-2xl mr-3">🎓</span>
                    <div>
                      <p className="text-xs text-gray-500">Admission Number</p>
                      <p className="text-sm font-semibold text-gray-900">{student.admission_number}</p>
                    </div>
                  </div>
                  <div className="flex items-center">
                    <span className="text-2xl mr-3">📧</span>
                    <div>
                      <p className="text-xs text-gray-500">Email</p>
                      <p className="text-sm font-semibold text-gray-900">{student.email || 'N/A'}</p>
                    </div>
                  </div>
                  <div className="flex items-center">
                    <span className="text-2xl mr-3">📱</span>
                    <div>
                      <p className="text-xs text-gray-500">Phone</p>
                      <p className="text-sm font-semibold text-gray-900">{student.phone || 'N/A'}</p>
                    </div>
                  </div>
                  <div className="flex items-center">
                    <span className="text-2xl mr-3">🩸</span>
                    <div>
                      <p className="text-xs text-gray-500">Blood Group</p>
                      <p className="text-sm font-semibold text-gray-900">{student.blood_group || 'N/A'}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Right Column - Details */}
          <div className="lg:col-span-2 space-y-6">
            {/* Personal Information */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 pb-2 border-b">Personal Information</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <p className="text-sm text-gray-500">First Name</p>
                  <p className="text-base font-semibold text-gray-900">{student.first_name}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Last Name</p>
                  <p className="text-base font-semibold text-gray-900">{student.last_name}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Date of Birth</p>
                  <p className="text-base font-semibold text-gray-900">
                    {student.date_of_birth ? new Date(student.date_of_birth).toLocaleDateString() : 'N/A'}
                  </p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Gender</p>
                  <p className="text-base font-semibold text-gray-900 capitalize">{student.gender}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Blood Group</p>
                  <p className="text-base font-semibold text-gray-900">{student.blood_group || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Admission Date</p>
                  <p className="text-base font-semibold text-gray-900">
                    {student.admission_date ? new Date(student.admission_date).toLocaleDateString() : 'N/A'}
                  </p>
                </div>
              </div>
            </div>

            {/* Contact Information */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 pb-2 border-b">Contact Information</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <p className="text-sm text-gray-500">Email</p>
                  <p className="text-base font-semibold text-gray-900">{student.email || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Phone</p>
                  <p className="text-base font-semibold text-gray-900">{student.phone || 'N/A'}</p>
                </div>
                <div className="md:col-span-2">
                  <p className="text-sm text-gray-500">Address</p>
                  <p className="text-base font-semibold text-gray-900">{student.address || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">City</p>
                  <p className="text-base font-semibold text-gray-900">{student.city || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">State/Province</p>
                  <p className="text-base font-semibold text-gray-900">{student.state || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Country</p>
                  <p className="text-base font-semibold text-gray-900">{student.country || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Postal Code</p>
                  <p className="text-base font-semibold text-gray-900">{student.postal_code || 'N/A'}</p>
                </div>
              </div>
            </div>

            {/* Academic Information */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 pb-2 border-b">Academic Information</h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                  <p className="text-sm text-gray-500">Grade</p>
                  <p className="text-base font-semibold text-gray-900">Grade {student.grade}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Section</p>
                  <p className="text-base font-semibold text-gray-900">Section {student.section}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Status</p>
                  <p className="text-base font-semibold text-gray-900 capitalize">{student.status || 'Active'}</p>
                </div>
              </div>
            </div>

            {/* Parent/Guardian Information */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 pb-2 border-b">Parent/Guardian Information</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <p className="text-sm text-gray-500">Parent/Guardian Name</p>
                  <p className="text-base font-semibold text-gray-900">{student.parent_name || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Parent Phone</p>
                  <p className="text-base font-semibold text-gray-900">{student.parent_phone || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Parent Email</p>
                  <p className="text-base font-semibold text-gray-900">{student.parent_email || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-500">Emergency Contact</p>
                  <p className="text-base font-semibold text-gray-900">{student.emergency_contact || 'N/A'}</p>
                </div>
              </div>
            </div>

            {/* Quick Actions */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 pb-2 border-b">Quick Actions</h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                <button className="flex flex-col items-center p-4 bg-blue-50 hover:bg-blue-100 rounded-lg transition">
                  <span className="text-3xl mb-2">📊</span>
                  <span className="text-sm font-medium text-gray-900">View Results</span>
                </button>
                <button className="flex flex-col items-center p-4 bg-green-50 hover:bg-green-100 rounded-lg transition">
                  <span className="text-3xl mb-2">✅</span>
                  <span className="text-sm font-medium text-gray-900">Attendance</span>
                </button>
                <button className="flex flex-col items-center p-4 bg-purple-50 hover:bg-purple-100 rounded-lg transition">
                  <span className="text-3xl mb-2">💰</span>
                  <span className="text-sm font-medium text-gray-900">Fee Details</span>
                </button>
                <button className="flex flex-col items-center p-4 bg-yellow-50 hover:bg-yellow-100 rounded-lg transition">
                  <span className="text-3xl mb-2">📝</span>
                  <span className="text-sm font-medium text-gray-900">Assignments</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentProfile;
