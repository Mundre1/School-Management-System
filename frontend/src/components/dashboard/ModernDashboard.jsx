import React, { useEffect, useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import api from '../../services/api';
import { 
  FaUserGraduate, 
  FaChalkboardTeacher, 
  FaUsers, 
  FaMoneyBillWave, 
  FaSearch, 
  FaBell, 
  FaCog, 
  FaSignOutAlt, 
  FaBook, 
  FaClipboardCheck, 
  FaCalendarAlt, 
  FaWallet,
  FaGraduationCap,
  FaChartLine,
  FaUserCheck,
  FaFileAlt,
  FaTrophy,
  FaBullhorn,
  FaPlus,
  FaDownload,
  FaUpload,
  FaPrint
} from 'react-icons/fa';

const ModernDashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  
  const [stats, setStats] = useState({
    totalStudents: 0,
    totalTeachers: 0,
    presentToday: 0,
    totalRevenue: 0,
    pendingFees: 0,
    upcomingExams: 0,
  });

  const [loading, setLoading] = useState(true);

  // Monthly attendance data
  const attendanceData = [
    { month: 'Jan', students: 92, teachers: 95 },
    { month: 'Feb', students: 88, teachers: 93 },
    { month: 'Mar', students: 95, teachers: 97 },
    { month: 'Apr', students: 90, teachers: 94 },
    { month: 'May', students: 93, teachers: 96 },
    { month: 'Jun', students: 89, teachers: 92 },
  ];

  // Revenue data
  const revenueData = [
    { month: 'Jan', amount: 45000 },
    { month: 'Feb', amount: 52000 },
    { month: 'Mar', amount: 48000 },
    { month: 'Apr', amount: 61000 },
    { month: 'May', amount: 55000 },
    { month: 'Jun', amount: 58000 },
  ];

  // Class distribution
  const classData = [
    { name: 'Grade 1-3', value: 280, color: '#3b82f6' },
    { name: 'Grade 4-6', value: 320, color: '#8b5cf6' },
    { name: 'Grade 7-9', value: 290, color: '#ec4899' },
    { name: 'Grade 10-12', value: 250, color: '#f59e0b' },
  ];

  // Recent activities
  const recentActivities = [
    { id: 1, type: 'exam', title: 'Mid-term Exam Schedule Released', time: '2 hours ago', icon: FaFileAlt, color: 'text-blue-600' },
    { id: 2, type: 'notice', title: 'Parent-Teacher Meeting on Friday', time: '5 hours ago', icon: FaBullhorn, color: 'text-purple-600' },
    { id: 3, type: 'result', title: 'Grade 10 Results Published', time: '1 day ago', icon: FaTrophy, color: 'text-green-600' },
    { id: 4, type: 'fee', title: 'Fee Payment Reminder Sent', time: '2 days ago', icon: FaMoneyBillWave, color: 'text-orange-600' },
  ];

  // Upcoming events
  const upcomingEvents = [
    { id: 1, title: 'Annual Sports Day', date: 'Oct 15, 2025', type: 'Sports' },
    { id: 2, title: 'Science Exhibition', date: 'Oct 20, 2025', type: 'Academic' },
    { id: 3, title: 'Cultural Program', date: 'Oct 25, 2025', type: 'Cultural' },
  ];

  // Top performers
  const topPerformers = [
    { name: 'Rajesh Kumar', class: 'Grade 10', percentage: 98.5, avatar: 'RK' },
    { name: 'Priya Sharma', class: 'Grade 12', percentage: 97.8, avatar: 'PS' },
    { name: 'Amit Thapa', class: 'Grade 9', percentage: 96.2, avatar: 'AT' },
  ];

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      setLoading(true);
      
      // Fetch students
      const studentsRes = await api.get('/students/students/');
      const totalStudents = studentsRes.data.count || studentsRes.data.results?.length || 0;
      
      // Fetch staff
      const staffRes = await api.get('/staff/staff/');
      const totalStaff = staffRes.data.count || staffRes.data.results?.length || 0;
      
      // Calculate attendance
      const presentToday = Math.floor(totalStudents * 0.92);
      
      setStats({
        totalStudents,
        totalTeachers: totalStaff,
        presentToday,
        totalRevenue: 58000,
        pendingFees: 12,
        upcomingExams: 3,
      });
      
      setLoading(false);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  const attendancePercentage = stats.totalStudents > 0 
    ? ((stats.presentToday / stats.totalStudents) * 100).toFixed(1) 
    : 0;

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-4 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-700 font-semibold">Loading Dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen bg-gradient-to-br from-gray-50 to-blue-50">
      {/* Sidebar */}
      <div className="w-64 bg-gradient-to-b from-indigo-900 via-blue-900 to-indigo-800 text-white shadow-2xl">
        <div className="p-6">
          {/* Logo */}
          <div className="mb-8 text-center">
            <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mx-auto mb-3 shadow-lg">
              <FaGraduationCap className="text-indigo-900 text-3xl" />
            </div>
            <h2 className="text-xl font-bold">Itahari International</h2>
            <p className="text-blue-200 text-xs mt-1">School Management</p>
          </div>
          
          {/* Navigation */}
          <nav className="space-y-1">
            <button className="w-full text-left px-4 py-3 rounded-xl bg-white bg-opacity-20 backdrop-blur-sm font-semibold transition flex items-center space-x-3 shadow-lg">
              <FaChartLine className="text-lg" />
              <span>Dashboard</span>
            </button>
            <button 
              onClick={() => navigate('/students')}
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaUserGraduate className="text-lg" />
              <span>Students</span>
            </button>
            <button 
              onClick={() => navigate('/staff')}
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaChalkboardTeacher className="text-lg" />
              <span>Teachers</span>
            </button>
            <button 
              onClick={() => navigate('/attendance')}
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaUserCheck className="text-lg" />
              <span>Attendance</span>
            </button>
            <button 
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaBook className="text-lg" />
              <span>Courses</span>
            </button>
            <button 
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaFileAlt className="text-lg" />
              <span>Exams</span>
            </button>
            <button 
              onClick={() => navigate('/fees')}
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaWallet className="text-lg" />
              <span>Fees</span>
            </button>
            <button 
              className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3"
            >
              <FaCalendarAlt className="text-lg" />
              <span>Events</span>
            </button>
          </nav>
        </div>

        {/* Bottom Actions */}
        <div className="absolute bottom-6 left-6 right-6 space-y-2">
          <button className="w-full text-left px-4 py-3 rounded-xl hover:bg-white hover:bg-opacity-10 transition flex items-center space-x-3">
            <FaCog className="text-lg" />
            <span>Settings</span>
          </button>
          <button
            onClick={handleLogout}
            className="w-full text-left px-4 py-3 rounded-xl bg-red-500 hover:bg-red-600 transition flex items-center space-x-3 font-semibold shadow-lg"
          >
            <FaSignOutAlt className="text-lg" />
            <span>Logout</span>
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {/* Header */}
        <div className="bg-white border-b shadow-sm px-8 py-4 sticky top-0 z-10">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-gray-800">Welcome back, {user?.first_name}! 👋</h1>
              <p className="text-sm text-gray-600 mt-1">Here's what's happening with your school today</p>
            </div>
            <div className="flex items-center space-x-4">
              {/* Search */}
              <div className="relative">
                <input
                  type="text"
                  placeholder="Search..."
                  className="w-64 px-4 py-2 pl-10 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
                <FaSearch className="absolute left-3 top-3 text-gray-400" />
              </div>
              
              {/* Notifications */}
              <button className="relative p-2 hover:bg-gray-100 rounded-lg transition">
                <FaBell className="text-2xl text-gray-600" />
                <span className="absolute top-0 right-0 w-5 h-5 bg-red-500 rounded-full text-white text-xs flex items-center justify-center font-bold">
                  5
                </span>
              </button>
              
              {/* User Profile */}
              <div className="flex items-center space-x-3 pl-4 border-l">
                <div className="text-right">
                  <p className="text-sm font-semibold text-gray-800">{user?.first_name} {user?.last_name}</p>
                  <p className="text-xs text-gray-500 capitalize">{user?.role || 'Administrator'}</p>
                </div>
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold shadow-lg">
                  {user?.first_name?.charAt(0)}{user?.last_name?.charAt(0)}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Dashboard Content */}
        <div className="p-8">
          {/* Quick Actions */}
          <div className="mb-6 flex space-x-3">
            <button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition flex items-center space-x-2 shadow-md">
              <FaPlus />
              <span>Add Student</span>
            </button>
            <button className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition flex items-center space-x-2 shadow-md">
              <FaUpload />
              <span>Import Data</span>
            </button>
            <button className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition flex items-center space-x-2 shadow-md">
              <FaDownload />
              <span>Export Report</span>
            </button>
            <button className="px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 transition flex items-center space-x-2 shadow-md">
              <FaPrint />
              <span>Print</span>
            </button>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-4 gap-6 mb-8">
            {/* Total Students */}
            <div className="bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl p-6 shadow-xl text-white transform hover:scale-105 transition cursor-pointer">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-white bg-opacity-30 rounded-xl flex items-center justify-center">
                  <FaUserGraduate className="text-2xl" />
                </div>
                <span className="text-sm bg-white bg-opacity-20 px-3 py-1 rounded-full">+12%</span>
              </div>
              <p className="text-blue-100 text-sm mb-1">Total Students</p>
              <p className="text-4xl font-bold">{stats.totalStudents}</p>
              <p className="text-xs text-blue-100 mt-2">Enrolled this year</p>
            </div>

            {/* Total Teachers */}
            <div className="bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl p-6 shadow-xl text-white transform hover:scale-105 transition cursor-pointer">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-white bg-opacity-30 rounded-xl flex items-center justify-center">
                  <FaChalkboardTeacher className="text-2xl" />
                </div>
                <span className="text-sm bg-white bg-opacity-20 px-3 py-1 rounded-full">+5%</span>
              </div>
              <p className="text-purple-100 text-sm mb-1">Total Teachers</p>
              <p className="text-4xl font-bold">{stats.totalTeachers}</p>
              <p className="text-xs text-purple-100 mt-2">Active staff members</p>
            </div>

            {/* Attendance Today */}
            <div className="bg-gradient-to-br from-green-500 to-green-600 rounded-2xl p-6 shadow-xl text-white transform hover:scale-105 transition cursor-pointer">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-white bg-opacity-30 rounded-xl flex items-center justify-center">
                  <FaUserCheck className="text-2xl" />
                </div>
                <span className="text-sm bg-white bg-opacity-20 px-3 py-1 rounded-full">{attendancePercentage}%</span>
              </div>
              <p className="text-green-100 text-sm mb-1">Present Today</p>
              <p className="text-4xl font-bold">{stats.presentToday}</p>
              <p className="text-xs text-green-100 mt-2">Out of {stats.totalStudents} students</p>
            </div>

            {/* Total Revenue */}
            <div className="bg-gradient-to-br from-orange-500 to-orange-600 rounded-2xl p-6 shadow-xl text-white transform hover:scale-105 transition cursor-pointer">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-white bg-opacity-30 rounded-xl flex items-center justify-center">
                  <FaMoneyBillWave className="text-2xl" />
                </div>
                <span className="text-sm bg-white bg-opacity-20 px-3 py-1 rounded-full">+8%</span>
              </div>
              <p className="text-orange-100 text-sm mb-1">Total Revenue</p>
              <p className="text-4xl font-bold">${(stats.totalRevenue / 1000).toFixed(1)}k</p>
              <p className="text-xs text-orange-100 mt-2">This month</p>
            </div>
          </div>

          {/* Charts Section */}
          <div className="grid grid-cols-3 gap-6 mb-8">
            {/* Attendance Trend */}
            <div className="col-span-2 bg-white rounded-2xl p-6 shadow-lg">
              <div className="flex justify-between items-center mb-6">
                <div>
                  <h3 className="text-lg font-bold text-gray-800">Attendance Trend</h3>
                  <p className="text-sm text-gray-500">Monthly attendance overview</p>
                </div>
                <select className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  <option>Last 6 Months</option>
                  <option>Last Year</option>
                  <option>All Time</option>
                </select>
              </div>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={attendanceData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                  <XAxis dataKey="month" stroke="#888" />
                  <YAxis stroke="#888" />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="students" stroke="#3b82f6" strokeWidth={3} dot={{ r: 5 }} name="Students" />
                  <Line type="monotone" dataKey="teachers" stroke="#8b5cf6" strokeWidth={3} dot={{ r: 5 }} name="Teachers" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            {/* Class Distribution */}
            <div className="bg-white rounded-2xl p-6 shadow-lg">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Class Distribution</h3>
              <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                  <Pie
                    data={classData}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={80}
                    paddingAngle={5}
                    dataKey="value"
                  >
                    {classData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
              <div className="mt-4 space-y-2">
                {classData.map((item, index) => (
                  <div key={index} className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }}></div>
                      <span className="text-sm text-gray-700">{item.name}</span>
                    </div>
                    <span className="text-sm font-semibold text-gray-800">{item.value}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Revenue Chart */}
          <div className="grid grid-cols-3 gap-6 mb-8">
            <div className="col-span-2 bg-white rounded-2xl p-6 shadow-lg">
              <div className="flex justify-between items-center mb-6">
                <div>
                  <h3 className="text-lg font-bold text-gray-800">Revenue Overview</h3>
                  <p className="text-sm text-gray-500">Monthly fee collection</p>
                </div>
              </div>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={revenueData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                  <XAxis dataKey="month" stroke="#888" />
                  <YAxis stroke="#888" />
                  <Tooltip />
                  <Bar dataKey="amount" fill="#3b82f6" radius={[8, 8, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Top Performers */}
            <div className="bg-white rounded-2xl p-6 shadow-lg">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Top Performers</h3>
              <div className="space-y-4">
                {topPerformers.map((student, index) => (
                  <div key={index} className="flex items-center space-x-3 p-3 bg-gray-50 rounded-xl hover:bg-gray-100 transition cursor-pointer">
                    <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm">
                      {student.avatar}
                    </div>
                    <div className="flex-1">
                      <p className="text-sm font-semibold text-gray-800">{student.name}</p>
                      <p className="text-xs text-gray-500">{student.class}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-lg font-bold text-green-600">{student.percentage}%</p>
                      <p className="text-xs text-gray-500">Score</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Bottom Section */}
          <div className="grid grid-cols-2 gap-6">
            {/* Recent Activities */}
            <div className="bg-white rounded-2xl p-6 shadow-lg">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Recent Activities</h3>
                <button className="text-sm text-blue-600 hover:text-blue-700 font-semibold">View All</button>
              </div>
              <div className="space-y-3">
                {recentActivities.map((activity) => (
                  <div key={activity.id} className="flex items-start space-x-3 p-3 hover:bg-gray-50 rounded-xl transition cursor-pointer">
                    <div className={`w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center ${activity.color}`}>
                      <activity.icon className="text-lg" />
                    </div>
                    <div className="flex-1">
                      <p className="text-sm font-semibold text-gray-800">{activity.title}</p>
                      <p className="text-xs text-gray-500 mt-1">{activity.time}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Upcoming Events */}
            <div className="bg-white rounded-2xl p-6 shadow-lg">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Upcoming Events</h3>
                <button className="text-sm text-blue-600 hover:text-blue-700 font-semibold">View Calendar</button>
              </div>
              <div className="space-y-3">
                {upcomingEvents.map((event) => (
                  <div key={event.id} className="p-4 border-l-4 border-blue-500 bg-blue-50 rounded-lg hover:bg-blue-100 transition cursor-pointer">
                    <div className="flex justify-between items-start">
                      <div>
                        <p className="text-sm font-semibold text-gray-800">{event.title}</p>
                        <p className="text-xs text-gray-600 mt-1">{event.date}</p>
                      </div>
                      <span className="text-xs bg-blue-200 text-blue-800 px-2 py-1 rounded-full font-semibold">
                        {event.type}
                      </span>
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
