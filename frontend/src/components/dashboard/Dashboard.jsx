import React, { useEffect, useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import api from '../../services/api';

const Dashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    totalStudents: 0,
    totalStaff: 0,
    totalClasses: 0,
    attendance: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await api.get('/students/students/');
      setStats({
        ...stats,
        totalStudents: response.data.count || 0,
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

  const StatCard = ({ title, value, icon, color }) => (
    <div className={`bg-white rounded-lg shadow-md p-6 border-l-4 ${color}`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-gray-500 text-sm font-medium">{title}</p>
          <p className="text-3xl font-bold text-gray-800 mt-2">{value}</p>
        </div>
        <div className={`text-4xl ${color.replace('border', 'text')}`}>
          {icon}
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">Smart School ERP</h1>
              <p className="text-sm text-gray-600">Welcome back, {user?.first_name}!</p>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-600">
                Role: <span className="font-semibold text-blue-600">{user?.role}</span>
              </span>
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
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <StatCard
            title="Total Students"
            value={loading ? '...' : stats.totalStudents}
            icon="👨‍🎓"
            color="border-blue-500"
          />
          <StatCard
            title="Total Staff"
            value={loading ? '...' : stats.totalStaff}
            icon="👨‍🏫"
            color="border-green-500"
          />
          <StatCard
            title="Total Classes"
            value={loading ? '...' : stats.totalClasses}
            icon="📚"
            color="border-purple-500"
          />
          <StatCard
            title="Attendance Today"
            value={loading ? '...' : `${stats.attendance}%`}
            icon="✅"
            color="border-yellow-500"
          />
        </div>

        {/* Quick Actions */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Quick Actions</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <button className="bg-blue-500 hover:bg-blue-600 text-white p-4 rounded-lg transition">
              <div className="text-2xl mb-2">👨‍🎓</div>
              <div className="text-sm font-medium">Manage Students</div>
            </button>
            <button className="bg-green-500 hover:bg-green-600 text-white p-4 rounded-lg transition">
              <div className="text-2xl mb-2">👨‍🏫</div>
              <div className="text-sm font-medium">Manage Staff</div>
            </button>
            <button className="bg-purple-500 hover:bg-purple-600 text-white p-4 rounded-lg transition">
              <div className="text-2xl mb-2">✅</div>
              <div className="text-sm font-medium">Take Attendance</div>
            </button>
            <button className="bg-yellow-500 hover:bg-yellow-600 text-white p-4 rounded-lg transition">
              <div className="text-2xl mb-2">💰</div>
              <div className="text-sm font-medium">Fee Management</div>
            </button>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Recent Activity</h2>
          <div className="space-y-4">
            <div className="flex items-center p-3 bg-gray-50 rounded-lg">
              <div className="flex-shrink-0 w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                <span className="text-blue-600 font-bold">👤</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-900">New student registered</p>
                <p className="text-xs text-gray-500">2 hours ago</p>
              </div>
            </div>
            <div className="flex items-center p-3 bg-gray-50 rounded-lg">
              <div className="flex-shrink-0 w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
                <span className="text-green-600 font-bold">✅</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-900">Attendance marked for Grade 10-A</p>
                <p className="text-xs text-gray-500">5 hours ago</p>
              </div>
            </div>
            <div className="flex items-center p-3 bg-gray-50 rounded-lg">
              <div className="flex-shrink-0 w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
                <span className="text-purple-600 font-bold">📝</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-900">New assignment posted</p>
                <p className="text-xs text-gray-500">1 day ago</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
