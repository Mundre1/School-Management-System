import React, { useEffect, useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import api from '../../services/api';
import { FaSchool, FaChalkboardTeacher, FaUserGraduate, FaUsers } from 'react-icons/fa';

const ModernDashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    schools: 69,
    teachers: 88,
    students: 90,
    parents: 128,
  });

  const attendanceData = [
    { year: '2019', value: 20 },
    { year: '2020', value: 40 },
    { year: '2021', value: 80 },
    { year: '2022', value: 60 },
    { year: '2023', value: 70 },
    { year: '2024', value: 50 },
    { year: '2025', value: 90 },
    { year: '2026', value: 75 },
  ];

  const educationalStages = [
    { name: 'Primary School', count: 90, color: '#7c3aed' },
    { name: 'Elementary School', count: 145, color: '#fbbf24' },
    { name: 'Preschool', count: 88, color: '#10b981' },
  ];

  const topStudents = [
    { name: 'Rowan Hossam', percentage: 99.88, rank: '1st', color: 'bg-green-500', image: '👨‍🎓' },
    { name: 'Rony Beyablo', percentage: 98.17, rank: '2nd', color: 'bg-purple-600', image: '👨‍🎓' },
    { name: 'Adam Hossam', percentage: 97.32, rank: '3rd', color: 'bg-yellow-500', image: '👨‍🎓' },
  ];

  const months = [
    { name: 'January', color: 'bg-white' },
    { name: 'February', color: 'bg-orange-400' },
    { name: 'March', color: 'bg-yellow-400' },
    { name: 'April', color: 'bg-green-500' },
    { name: 'May', color: 'bg-orange-400' },
    { name: 'June', color: 'bg-yellow-400' },
    { name: 'July', color: 'bg-white' },
    { name: 'August', color: 'bg-orange-400' },
    { name: 'September', color: 'bg-yellow-400' },
    { name: 'October', color: 'bg-white' },
    { name: 'November', color: 'bg-orange-400' },
    { name: 'December', color: 'bg-yellow-400' },
  ];

  const activities = [
    'Elimination Game',
    'Freshman Orientation',
    'Spring Sports Rally',
  ];

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await api.get('/students/students/');
      setStats(prev => ({
        ...prev,
        students: response.data.count || 90,
      }));
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    }
  };

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar */}
      <div className="w-64 bg-gradient-to-b from-purple-900 to-purple-700 text-white">
        <div className="p-6">
          <div className="flex items-center space-x-3 mb-8">
            <div className="w-12 h-12 bg-white rounded-lg flex items-center justify-center">
              <FaSchool className="text-purple-700 text-2xl" />
            </div>
          </div>
          
          <nav className="space-y-2">
            <button className="w-full text-left px-4 py-3 rounded-lg bg-purple-800 hover:bg-purple-600 transition">
              Dashboard
            </button>
            <button 
              onClick={() => navigate('/students')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-purple-600 transition"
            >
              Students
            </button>
            <button 
              onClick={() => navigate('/staff')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-purple-600 transition"
            >
              Teachers
            </button>
            <button className="w-full text-left px-4 py-3 rounded-lg hover:bg-purple-600 transition">
              Parents
            </button>
            <button 
              onClick={() => navigate('/events')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-purple-600 transition"
            >
              Events
            </button>
            <button className="w-full text-left px-4 py-3 rounded-lg hover:bg-purple-600 transition">
              Exams
            </button>
            <button 
              onClick={() => navigate('/assignments')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-purple-600 transition"
            >
              Assignment
            </button>
          </nav>
        </div>

        <div className="absolute bottom-8 left-6 right-6">
          <button
            onClick={handleLogout}
            className="w-full bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition"
          >
            Logout
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {/* Header */}
        <div className="bg-white border-b px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-gray-800">Welcome to Itahari International School</h1>
              <p className="text-sm text-gray-500">School Year 2025 - 2026</p>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-right">
                <p className="text-sm font-semibold">{user?.first_name} {user?.last_name}</p>
                <p className="text-xs text-gray-500">{user?.role}</p>
              </div>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="p-8">
          <div className="grid grid-cols-4 gap-6 mb-8">
            <div className="bg-white rounded-xl p-6 shadow-sm border-l-4 border-red-400">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-500 text-sm mb-2">Schools</p>
                  <p className="text-4xl font-bold text-gray-800">{stats.schools}</p>
                </div>
                <FaSchool className="text-5xl text-red-400" />
              </div>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-sm border-l-4 border-blue-500">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-500 text-sm mb-2">Teachers</p>
                  <p className="text-4xl font-bold text-gray-800">{stats.teachers}</p>
                </div>
                <FaChalkboardTeacher className="text-5xl text-blue-500" />
              </div>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-sm border-l-4 border-yellow-400">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-500 text-sm mb-2">Students</p>
                  <p className="text-4xl font-bold text-gray-800">{stats.students}</p>
                </div>
                <FaUserGraduate className="text-5xl text-yellow-400" />
              </div>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-sm border-l-4 border-green-500">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-500 text-sm mb-2">Parents</p>
                  <p className="text-4xl font-bold text-gray-800">{stats.parents}</p>
                </div>
                <FaUsers className="text-5xl text-green-500" />
              </div>
            </div>
          </div>

          {/* Charts and Info Section */}
          <div className="grid grid-cols-2 gap-6 mb-8">
            {/* Calendar Attendance */}
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Calendar Attendance</h3>
              <ResponsiveContainer width="100%" height={200}>
                <BarChart data={attendanceData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="year" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#7c3aed" radius={[8, 8, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
              
              <div className="grid grid-cols-4 gap-2 mt-4">
                {months.map((month, index) => (
                  <div key={index} className={`${month.color} p-2 rounded text-center text-xs font-medium`}>
                    {month.name}
                  </div>
                ))}
              </div>
            </div>

            {/* Educational Stage */}
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Educational stage</h3>
                <p className="text-xs text-gray-400">All data in Thousand 2021 - 2022</p>
              </div>
              
              <div className="space-y-4">
                {educationalStages.map((stage, index) => (
                  <div key={index} className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <div className={`w-3 h-3 rounded-full`} style={{ backgroundColor: stage.color }}></div>
                      <span className="text-sm text-gray-700">{stage.name}</span>
                    </div>
                    <span className="text-lg font-bold text-gray-800">{stage.count}</span>
                  </div>
                ))}
              </div>

              <div className="mt-6 h-40 flex items-end justify-around">
                {educationalStages.map((stage, index) => (
                  <div
                    key={index}
                    className="w-20 rounded-t-lg"
                    style={{
                      backgroundColor: stage.color,
                      height: `${(stage.count / 145) * 100}%`,
                    }}
                  ></div>
                ))}
              </div>
            </div>
          </div>

          {/* Bottom Section */}
          <div className="grid grid-cols-2 gap-6">
            {/* Activities & Events */}
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Activities & Events</h3>
                <button className="text-sm text-green-600 border border-green-600 px-4 py-1 rounded-full hover:bg-green-50">
                  View All
                </button>
              </div>
              
              <div className="space-y-3">
                {activities.map((activity, index) => (
                  <div key={index} className="p-3 bg-gray-50 rounded-lg hover:bg-gray-100 cursor-pointer">
                    <p className="text-sm text-gray-700">{activity}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Top Students */}
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Top Students</h3>
              
              <div className="grid grid-cols-3 gap-4">
                {topStudents.map((student, index) => (
                  <div key={index} className={`${student.color} rounded-xl p-4 text-white text-center`}>
                    <div className="text-4xl mb-2">{student.image}</div>
                    <p className="font-semibold text-sm mb-1">{student.name}</p>
                    <p className="text-2xl font-bold mb-1">{student.percentage}%</p>
                    <div className="bg-white bg-opacity-30 rounded-full px-3 py-1 text-xs font-medium">
                      {student.rank}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModernDashboard;
