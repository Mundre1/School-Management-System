import React, { useEffect, useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
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
  FaGraduationCap 
} from 'react-icons/fa';

const ModernDashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  
  const [stats, setStats] = useState({
    students: 12478,
    teachers: 478,
    parents: 8908,
    earnings: 42800,
  });

  const [loading, setLoading] = useState(true);

  // Total Earnings Data (Monthly)
  const earningsData = [
    { month: 'Jan', earnings: 35000, expense: 25000 },
    { month: 'Feb', earnings: 28000, expense: 22000 },
    { month: 'Mar', earnings: 32000, expense: 24000 },
    { month: 'Apr', earnings: 38000, expense: 26000 },
    { month: 'May', earnings: 25000, expense: 20000 },
    { month: 'Jun', earnings: 30000, expense: 23000 },
    { month: 'Jul', earnings: 42000, expense: 28000 },
    { month: 'Aug', earnings: 35000, expense: 25000 },
    { month: 'Sep', earnings: 28000, expense: 22000 },
    { month: 'Oct', earnings: 32000, expense: 24000 },
    { month: 'Nov', earnings: 30000, expense: 23000 },
    { month: 'Dec', earnings: 35000, expense: 25000 },
  ];

  // Top Performers
  const topPerformers = [
    { name: 'Enes Schirrel', id: '4278', class: '6th Class', percentage: 98.82 },
    { name: 'Cayla Bergnaum', id: '3347', class: '8th Class', percentage: 98.72 },
    { name: 'Kathryn Hahn', id: '3943', class: '5th Class', percentage: 97.50 },
  ];

  // Attendance Data
  const attendanceStats = {
    students: 84,
    teachers: 91,
  };

  // Events Calendar
  const events = [
    { date: '08 Jan, 2023', title: 'School Annual Function', icon: '→' },
    { date: '27 Jan, 2023', title: 'Sport Competition', icon: '→' },
  ];

  // Calendar for January 2023
  const calendarDays = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, null, null, null, null],
  ];

  const highlightedDates = [8, 19, 27];

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      setLoading(true);
      
      // Fetch real student count
      const studentsRes = await api.get('/students/students/');
      const totalStudents = studentsRes.data.count || studentsRes.data.results?.length || 12478;
      
      // Fetch real staff count
      const staffRes = await api.get('/staff/staff/');
      const totalStaff = staffRes.data.count || staffRes.data.results?.length || 478;
      
      setStats(prev => ({
        ...prev,
        students: totalStudents,
        teachers: totalStaff,
        parents: totalStudents * 2, // Approximate: 2 parents per student
      }));
      
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

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-64 bg-gradient-to-b from-slate-700 to-slate-800 text-white shadow-xl">
        <div className="p-6">
          {/* Logo */}
          <div className="mb-8 flex items-center space-x-3">
            <div className="w-10 h-10 bg-white rounded-lg flex items-center justify-center">
              <FaGraduationCap className="text-slate-700 text-2xl" />
            </div>
            <span className="text-xl font-bold">SCHOOL</span>
          </div>
          
          {/* Navigation */}
          <nav className="space-y-2">
            <button className="w-full text-left px-4 py-3 rounded-lg bg-white text-slate-800 font-semibold transition flex items-center space-x-3">
              <FaClipboardCheck />
              <span>Dashboard</span>
            </button>
            <button 
              onClick={() => navigate('/students')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3"
            >
              <FaUserGraduate />
              <span>Students</span>
            </button>
            <button 
              onClick={() => navigate('/staff')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3"
            >
              <FaChalkboardTeacher />
              <span>Teachers</span>
            </button>
            <button 
              onClick={() => navigate('/attendance')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3"
            >
              <FaClipboardCheck />
              <span>Attendance</span>
            </button>
            <button 
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3"
            >
              <FaBook />
              <span>Courses</span>
            </button>
            <button 
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3"
            >
              <FaClipboardCheck />
              <span>Exam</span>
            </button>
            <button 
              onClick={() => navigate('/fees')}
              className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3"
            >
              <FaWallet />
              <span>Payment</span>
            </button>
          </nav>
        </div>

        {/* Bottom Actions */}
        <div className="absolute bottom-8 left-6 right-6 space-y-2">
          <button className="w-full text-left px-4 py-3 rounded-lg hover:bg-slate-600 transition flex items-center space-x-3">
            <FaCog />
            <span>Settings</span>
          </button>
          <button
            onClick={handleLogout}
            className="w-full text-left px-4 py-3 rounded-lg hover:bg-red-600 transition flex items-center space-x-3"
          >
            <FaSignOutAlt />
            <span>Logout</span>
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {/* Header */}
        <div className="bg-white border-b px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-gray-800">Dashboard</h1>
            </div>
            <div className="flex items-center space-x-6">
              {/* Search */}
              <div className="relative">
                <input
                  type="text"
                  placeholder="Search for students/teachers/documents..."
                  className="w-96 px-4 py-2 pl-10 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <FaSearch className="absolute left-3 top-3 text-gray-400" />
              </div>
              
              {/* Notifications */}
              <button className="relative">
                <FaBell className="text-2xl text-gray-600" />
                <span className="absolute -top-1 -right-1 w-5 h-5 bg-red-500 rounded-full text-white text-xs flex items-center justify-center">
                  3
                </span>
              </button>
              
              {/* User Profile */}
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold">
                  {user?.first_name?.charAt(0)}{user?.last_name?.charAt(0)}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="p-8">
          <div className="grid grid-cols-4 gap-6 mb-8">
            {/* Students Card */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                  <FaUserGraduate className="text-2xl text-blue-600" />
                </div>
              </div>
              <p className="text-gray-500 text-sm mb-1">Students</p>
              <p className="text-3xl font-bold text-gray-800">{stats.students.toLocaleString()}</p>
            </div>

            {/* Teachers Card */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                  <FaChalkboardTeacher className="text-2xl text-purple-600" />
                </div>
              </div>
              <p className="text-gray-500 text-sm mb-1">Teachers</p>
              <p className="text-3xl font-bold text-gray-800">{stats.teachers}</p>
            </div>

            {/* Parents Card */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                  <FaUsers className="text-2xl text-green-600" />
                </div>
              </div>
              <p className="text-gray-500 text-sm mb-1">Parents</p>
              <p className="text-3xl font-bold text-gray-800">{stats.parents.toLocaleString()}</p>
            </div>

            {/* Earnings Card */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <div className="flex items-center justify-between mb-4">
                <div className="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
                  <FaMoneyBillWave className="text-2xl text-orange-600" />
                </div>
              </div>
              <p className="text-gray-500 text-sm mb-1">Earnings</p>
              <p className="text-3xl font-bold text-gray-800">${stats.earnings.toLocaleString()}k</p>
            </div>
          </div>

          {/* Charts Section */}
          <div className="grid grid-cols-3 gap-6 mb-8">
            {/* Total Earnings Chart */}
            <div className="col-span-2 bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <div className="flex justify-between items-center mb-6">
                <h3 className="text-lg font-bold text-gray-800">Total Earnings</h3>
                <div className="flex items-center space-x-4">
                  <div className="flex items-center space-x-2">
                    <div className="w-3 h-3 bg-slate-700 rounded-full"></div>
                    <span className="text-sm text-gray-600">Earnings</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <div className="w-3 h-3 bg-yellow-400 rounded-full"></div>
                    <span className="text-sm text-gray-600">Expense</span>
                  </div>
                  <select className="border border-gray-300 rounded-lg px-3 py-1 text-sm">
                    <option>2022</option>
                    <option>2023</option>
                    <option>2024</option>
                    <option>2025</option>
                  </select>
                </div>
              </div>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={earningsData}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="earnings" fill="#334155" radius={[4, 4, 0, 0]} />
                  <Bar dataKey="expense" fill="#fbbf24" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Events Calendar */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Events Calendar</h3>
              
              {/* Events List */}
              <div className="space-y-3 mb-4">
                {events.map((event, index) => (
                  <div key={index} className="flex justify-between items-start">
                    <div>
                      <p className="text-xs text-gray-500">{event.date}</p>
                      <p className="text-sm font-semibold text-gray-800">{event.title}</p>
                    </div>
                    <span className="text-gray-400">{event.icon}</span>
                  </div>
                ))}
              </div>

              {/* Mini Calendar */}
              <div className="mt-6">
                <div className="text-center mb-2">
                  <p className="text-sm font-bold text-gray-800">January 2023</p>
                </div>
                <div className="grid grid-cols-7 gap-1 text-center text-xs">
                  {['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'].map((day) => (
                    <div key={day} className="text-gray-500 font-semibold py-1">
                      {day}
                    </div>
                  ))}
                  {calendarDays.flat().map((day, index) => (
                    <div
                      key={index}
                      className={`py-1 ${
                        day === null
                          ? ''
                          : day === 8
                          ? 'bg-blue-500 text-white rounded-full'
                          : highlightedDates.includes(day)
                          ? 'bg-red-500 text-white rounded-full'
                          : 'text-gray-700'
                      }`}
                    >
                      {day || ''}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Bottom Section */}
          <div className="grid grid-cols-3 gap-6">
            {/* Top Performers */}
            <div className="col-span-2 bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <h3 className="text-lg font-bold text-gray-800 mb-4">Top Performer</h3>
              
              <div className="space-y-4">
                {/* Table Header */}
                <div className="grid grid-cols-12 gap-4 text-sm text-gray-500 font-semibold border-b pb-2">
                  <div className="col-span-1">Photo</div>
                  <div className="col-span-3">Name</div>
                  <div className="col-span-2">ID Number</div>
                  <div className="col-span-2">Year</div>
                  <div className="col-span-2">Class</div>
                  <div className="col-span-2">Mark</div>
                </div>

                {/* Table Rows */}
                {topPerformers.map((student, index) => (
                  <div key={index} className="grid grid-cols-12 gap-4 items-center py-2 border-b">
                    <div className="col-span-1">
                      <div className="w-8 h-8 bg-gray-300 rounded-full"></div>
                    </div>
                    <div className="col-span-3">
                      <p className="text-sm font-semibold text-gray-800">{student.name}</p>
                    </div>
                    <div className="col-span-2">
                      <p className="text-sm text-gray-600">{student.id}</p>
                    </div>
                    <div className="col-span-2">
                      <p className="text-sm text-gray-600">Graduated</p>
                    </div>
                    <div className="col-span-2">
                      <p className="text-sm text-gray-600">{student.class}</p>
                    </div>
                    <div className="col-span-2">
                      <div className="flex items-center space-x-2">
                        <div className="flex-1 bg-gray-200 rounded-full h-2">
                          <div
                            className="bg-red-400 h-2 rounded-full"
                            style={{ width: `${student.percentage}%` }}
                          ></div>
                        </div>
                        <span className="text-sm font-semibold text-gray-800">
                          {student.percentage}%
                        </span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Attendance */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
              <h3 className="text-lg font-bold text-gray-800 mb-6">Attendance</h3>
              
              <div className="space-y-6">
                {/* Students Attendance */}
                <div>
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm text-gray-600">Students</span>
                    <span className="text-sm font-bold text-gray-800">{attendanceStats.students}%</span>
                  </div>
                  <div className="relative">
                    <svg className="w-32 h-32 mx-auto" viewBox="0 0 36 36">
                      <path
                        d="M18 2.0845
                          a 15.9155 15.9155 0 0 1 0 31.831
                          a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none"
                        stroke="#e5e7eb"
                        strokeWidth="3"
                      />
                      <path
                        d="M18 2.0845
                          a 15.9155 15.9155 0 0 1 0 31.831
                          a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none"
                        stroke="#3b82f6"
                        strokeWidth="3"
                        strokeDasharray={`${attendanceStats.students}, 100`}
                      />
                    </svg>
                    <div className="absolute inset-0 flex items-center justify-center">
                      <span className="text-2xl font-bold text-gray-800">{attendanceStats.students}%</span>
                    </div>
                  </div>
                </div>

                {/* Teachers Attendance */}
                <div>
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm text-gray-600">Teachers</span>
                    <span className="text-sm font-bold text-gray-800">{attendanceStats.teachers}%</span>
                  </div>
                  <div className="relative">
                    <svg className="w-32 h-32 mx-auto" viewBox="0 0 36 36">
                      <path
                        d="M18 2.0845
                          a 15.9155 15.9155 0 0 1 0 31.831
                          a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none"
                        stroke="#e5e7eb"
                        strokeWidth="3"
                      />
                      <path
                        d="M18 2.0845
                          a 15.9155 15.9155 0 0 1 0 31.831
                          a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none"
                        stroke="#fbbf24"
                        strokeWidth="3"
                        strokeDasharray={`${attendanceStats.teachers}, 100`}
                      />
                    </svg>
                    <div className="absolute inset-0 flex items-center justify-center">
                      <span className="text-2xl font-bold text-gray-800">{attendanceStats.teachers}%</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* CTA Section */}
              <div className="mt-6 bg-gradient-to-br from-slate-700 to-slate-800 rounded-xl p-4 text-white text-center">
                <p className="text-sm mb-3">Join the community and find out more...</p>
                <button className="bg-white text-slate-800 px-6 py-2 rounded-lg text-sm font-semibold hover:bg-gray-100 transition">
                  Explore now
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModernDashboard;
