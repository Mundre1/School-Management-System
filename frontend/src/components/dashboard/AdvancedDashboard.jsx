import React, { useEffect, useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import {
  BarChart, Bar, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer
} from 'recharts';
import api from '../../services/api';

const AdvancedDashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    totalStudents: 0,
    totalStaff: 0,
    totalClasses: 0,
    attendance: 0,
  });

  // Sample data for charts
  const attendanceData = [
    { name: 'Mon', present: 450, absent: 50 },
    { name: 'Tue', present: 480, absent: 20 },
    { name: 'Wed', present: 470, absent: 30 },
    { name: 'Thu', present: 490, absent: 10 },
    { name: 'Fri', present: 460, absent: 40 },
    { name: 'Sat', present: 440, absent: 60 },
  ];

  const gradesData = [
    { month: 'Jan', average: 75 },
    { month: 'Feb', average: 78 },
    { month: 'Mar', average: 82 },
    { month: 'Apr', average: 80 },
    { month: 'May', average: 85 },
    { month: 'Jun', average: 88 },
  ];

  const studentDistribution = [
    { name: 'Grade 1', value: 60, color: '#3b82f6' },
    { name: 'Grade 2', value: 55, color: '#10b981' },
    { name: 'Grade 3', value: 58, color: '#f59e0b' },
    { name: 'Grade 4', value: 62, color: '#ef4444' },
    { name: 'Grade 5', value: 50, color: '#8b5cf6' },
    { name: 'Grade 6', value: 48, color: '#ec4899' },
    { name: 'Grade 7', value: 52, color: '#14b8a6' },
    { name: 'Grade 8', value: 45, color: '#f97316' },
  ];

  const timetableData = [
    { time: '08:00 - 09:00', mon: 'Math', tue: 'English', wed: 'Science', thu: 'History', fri: 'Math', sat: 'Sports' },
    { time: '09:00 - 10:00', mon: 'English', tue: 'Math', wed: 'History', thu: 'Science', fri: 'English', sat: 'Art' },
    { time: '10:00 - 11:00', mon: 'Science', tue: 'History', wed: 'Math', thu: 'English', fri: 'Science', sat: 'Music' },
    { time: '11:00 - 12:00', mon: 'History', tue: 'Science', wed: 'English', thu: 'Math', fri: 'History', sat: 'Library' },
  ];

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await api.get('/students/students/');
      setStats({
        totalStudents: response.data.count || 0,
        totalStaff: 45,
        totalClasses: 24,
        attendance: 92,
      });
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-blue-600">Smart School ERP</h1>
              <p className="text-sm text-gray-600">Mosaic Elementary School - Main Dashboard</p>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-right">
                <p className="text-sm font-semibold text-gray-900">{user?.first_name} {user?.last_name}</p>
                <p className="text-xs text-gray-500">{user?.role}</p>
              </div>
              <button
                onClick={handleLogout}
                className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm font-medium transition"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <div className="bg-white rounded-lg shadow p-6 border-l-4 border-blue-500">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-gray-500 text-sm">Total Students</p>
                <p className="text-3xl font-bold text-gray-800 mt-2">{loading ? '...' : stats.totalStudents}</p>
              </div>
              <div className="text-4xl">👨‍🎓</div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-gray-500 text-sm">Total Staff</p>
                <p className="text-3xl font-bold text-gray-800 mt-2">{stats.totalStaff}</p>
              </div>
              <div className="text-4xl">👨‍🏫</div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow p-6 border-l-4 border-purple-500">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-gray-500 text-sm">Total Classes</p>
                <p className="text-3xl font-bold text-gray-800 mt-2">{stats.totalClasses}</p>
              </div>
              <div className="text-4xl">📚</div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow p-6 border-l-4 border-yellow-500">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-gray-500 text-sm">Attendance</p>
                <p className="text-3xl font-bold text-gray-800 mt-2">{stats.attendance}%</p>
              </div>
              <div className="text-4xl">✅</div>
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="bg-white rounded-lg shadow p-6 mb-6">
          <h3 className="text-lg font-bold text-gray-900 mb-4">Quick Actions</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3">
            <button
              onClick={() => navigate('/students')}
              className="flex flex-col items-center p-4 bg-blue-50 hover:bg-blue-100 rounded-lg transition"
            >
              <span className="text-3xl mb-2">👨‍🎓</span>
              <span className="text-sm font-medium text-gray-900">Students</span>
            </button>
            <button
              onClick={() => navigate('/students/add')}
              className="flex flex-col items-center p-4 bg-green-50 hover:bg-green-100 rounded-lg transition"
            >
              <span className="text-3xl mb-2">➕</span>
              <span className="text-sm font-medium text-gray-900">Add Student</span>
            </button>
            <button
              onClick={() => navigate('/staff')}
              className="flex flex-col items-center p-4 bg-purple-50 hover:bg-purple-100 rounded-lg transition"
            >
              <span className="text-3xl mb-2">👨‍🏫</span>
              <span className="text-sm font-medium text-gray-900">Staff</span>
            </button>
            <button
              onClick={() => navigate('/attendance')}
              className="flex flex-col items-center p-4 bg-yellow-50 hover:bg-yellow-100 rounded-lg transition"
            >
              <span className="text-3xl mb-2">✅</span>
              <span className="text-sm font-medium text-gray-900">Attendance</span>
            </button>
            <button
              onClick={() => navigate('/fees')}
              className="flex flex-col items-center p-4 bg-pink-50 hover:bg-pink-100 rounded-lg transition"
            >
              <span className="text-3xl mb-2">💰</span>
              <span className="text-sm font-medium text-gray-900">Fees</span>
            </button>
            <button
              onClick={() => navigate('/results')}
              className="flex flex-col items-center p-4 bg-indigo-50 hover:bg-indigo-100 rounded-lg transition"
            >
              <span className="text-3xl mb-2">📊</span>
              <span className="text-sm font-medium text-gray-900">Results</span>
            </button>
          </div>
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
          {/* Attendance Status Pie Chart */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4">Attendance Status</h3>
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie
                  data={studentDistribution}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {studentDistribution.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
            <div className="mt-4 grid grid-cols-2 gap-2 text-xs">
              {studentDistribution.slice(0, 4).map((item, index) => (
                <div key={index} className="flex items-center">
                  <div className="w-3 h-3 rounded-full mr-2" style={{ backgroundColor: item.color }}></div>
                  <span>{item.name}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Average Grades per Month */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4">Average Grades per Month</h3>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={gradesData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="month" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="average" fill="#3b82f6" />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Average Grades per Class */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4">Average Grades per Class</h3>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={attendanceData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="present" fill="#10b981" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Timetable */}
        <div className="bg-white rounded-lg shadow p-6 mb-6">
          <h3 className="text-lg font-bold text-gray-900 mb-4">Weekly Timetable - Grade 10A</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b">
                  <th className="text-left p-3 bg-gray-50">Time</th>
                  <th className="text-left p-3 bg-gray-50">Monday</th>
                  <th className="text-left p-3 bg-gray-50">Tuesday</th>
                  <th className="text-left p-3 bg-gray-50">Wednesday</th>
                  <th className="text-left p-3 bg-gray-50">Thursday</th>
                  <th className="text-left p-3 bg-gray-50">Friday</th>
                  <th className="text-left p-3 bg-gray-50">Saturday</th>
                </tr>
              </thead>
              <tbody>
                {timetableData.map((row, index) => (
                  <tr key={index} className="border-b hover:bg-gray-50">
                    <td className="p-3 font-medium">{row.time}</td>
                    <td className="p-3">
                      <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs">{row.mon}</span>
                    </td>
                    <td className="p-3">
                      <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-xs">{row.tue}</span>
                    </td>
                    <td className="p-3">
                      <span className="bg-purple-100 text-purple-800 px-2 py-1 rounded text-xs">{row.wed}</span>
                    </td>
                    <td className="p-3">
                      <span className="bg-yellow-100 text-yellow-800 px-2 py-1 rounded text-xs">{row.thu}</span>
                    </td>
                    <td className="p-3">
                      <span className="bg-pink-100 text-pink-800 px-2 py-1 rounded text-xs">{row.fri}</span>
                    </td>
                    <td className="p-3">
                      <span className="bg-indigo-100 text-indigo-800 px-2 py-1 rounded text-xs">{row.sat}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Upcoming Events & Recent Activity */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Upcoming Events */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4">Upcoming Events</h3>
            <div className="space-y-3">
              <div className="flex items-start p-3 bg-blue-50 rounded-lg">
                <div className="flex-shrink-0 w-12 h-12 bg-blue-500 rounded-lg flex items-center justify-center text-white font-bold">
                  <div className="text-center">
                    <div className="text-xs">MAY</div>
                    <div className="text-lg">28</div>
                  </div>
                </div>
                <div className="ml-4">
                  <p className="text-sm font-semibold text-gray-900">Annual Sports Day</p>
                  <p className="text-xs text-gray-500">School Ground • 9:00 AM</p>
                </div>
              </div>
              <div className="flex items-start p-3 bg-green-50 rounded-lg">
                <div className="flex-shrink-0 w-12 h-12 bg-green-500 rounded-lg flex items-center justify-center text-white font-bold">
                  <div className="text-center">
                    <div className="text-xs">JUN</div>
                    <div className="text-lg">05</div>
                  </div>
                </div>
                <div className="ml-4">
                  <p className="text-sm font-semibold text-gray-900">Parent-Teacher Meeting</p>
                  <p className="text-xs text-gray-500">Main Hall • 2:00 PM</p>
                </div>
              </div>
              <div className="flex items-start p-3 bg-purple-50 rounded-lg">
                <div className="flex-shrink-0 w-12 h-12 bg-purple-500 rounded-lg flex items-center justify-center text-white font-bold">
                  <div className="text-center">
                    <div className="text-xs">JUN</div>
                    <div className="text-lg">15</div>
                  </div>
                </div>
                <div className="ml-4">
                  <p className="text-sm font-semibold text-gray-900">Final Exams Begin</p>
                  <p className="text-xs text-gray-500">All Classes</p>
                </div>
              </div>
            </div>
          </div>

          {/* Recent Activity */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4">Recent Activity</h3>
            <div className="space-y-3">
              <div className="flex items-center p-3 bg-gray-50 rounded-lg">
                <div className="flex-shrink-0 w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                  <span className="text-blue-600 font-bold">👤</span>
                </div>
                <div className="ml-4 flex-1">
                  <p className="text-sm font-medium text-gray-900">New student registered</p>
                  <p className="text-xs text-gray-500">Ram Sharma - Grade 10A</p>
                </div>
                <span className="text-xs text-gray-400">2h ago</span>
              </div>
              <div className="flex items-center p-3 bg-gray-50 rounded-lg">
                <div className="flex-shrink-0 w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
                  <span className="text-green-600 font-bold">✅</span>
                </div>
                <div className="ml-4 flex-1">
                  <p className="text-sm font-medium text-gray-900">Attendance marked</p>
                  <p className="text-xs text-gray-500">Grade 10-A • 98% present</p>
                </div>
                <span className="text-xs text-gray-400">5h ago</span>
              </div>
              <div className="flex items-center p-3 bg-gray-50 rounded-lg">
                <div className="flex-shrink-0 w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
                  <span className="text-purple-600 font-bold">📝</span>
                </div>
                <div className="ml-4 flex-1">
                  <p className="text-sm font-medium text-gray-900">New assignment posted</p>
                  <p className="text-xs text-gray-500">Mathematics - Chapter 5</p>
                </div>
                <span className="text-xs text-gray-400">1d ago</span>
              </div>
              <div className="flex items-center p-3 bg-gray-50 rounded-lg">
                <div className="flex-shrink-0 w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center">
                  <span className="text-yellow-600 font-bold">💰</span>
                </div>
                <div className="ml-4 flex-1">
                  <p className="text-sm font-medium text-gray-900">Fee payment received</p>
                  <p className="text-xs text-gray-500">Sita Sharma - NPR 15,000</p>
                </div>
                <span className="text-xs text-gray-400">1d ago</span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default AdvancedDashboard;
